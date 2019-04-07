# -*- coding: utf-8 -*-
from __future__ import absolute_import
import copy
from mais.game import Game
from mais.record import Record


class League(Record):
    """
    Mais doesn't write anything back to this database, so we only need to
    implemnt the read methods.
    """

    def initSeason(self):
        self.standings = copy.deepcopy(self.teams)

    def initStandings(self, team, season, competition, start, log):
        """
        This looks up a team's results prior to the simulation start date.

        SELECT COUNT(g.ID) AS GP, 
          SUM(IF(h.team3ltr = 'CLB',IF(HScore>AScore,1,0),IF(AScore>HScore,1,0))) AS Wins, 
          SUM(IF(HScore=AScore,1,0)) AS Draws,
          SUM(IF(h.team3ltr = 'CLB',IF(HScore<AScore,1,0),IF(AScore<HScore,1,0))) AS Losses
        FROM tbl_games g
        INNER JOIN tbl_teams h ON g.HTeamID = h.ID
        INNER JOIN tbl_teams a ON g.ATeamID = a.ID
        WHERE (h.team3ltr = 'CLB' OR a.team3ltr = 'CLB')
          AND YEAR(MatchTime) = 1996
          AND MatchTime < '1996-07-01'
        """
        sql = ('SELECT COUNT(g.ID) AS GP, '
               '  SUM(IF(h.team3ltr = %s,IF(HScore>AScore,1,0),IF(AScore>HScore,1,0))) AS Wins, '
               '  SUM(IF(HScore=AScore,1,0)) AS Draws, '
               '  SUM(IF(h.team3ltr = %s,IF(HScore<AScore,1,0),IF(AScore<HScore,1,0))) AS Losses '
               'FROM tbl_games g '
               'INNER JOIN tbl_teams h ON g.HTeamID = h.ID '
               'INNER JOIN tbl_teams a ON g.ATeamID = a.ID '
               'INNER JOIN lkp_matchtypes m on g.MatchTypeID = m.ID '
               'WHERE (h.team3ltr = %s OR a.team3ltr = %s) '
               '  AND m.Abbv = %s '
               '  AND YEAR(MatchTime) = %s '
               '  AND MatchTime < %s')
        rs = self.db.query(sql, (
            team['Abbv'],
            team['Abbv'],
            team['Abbv'],
            team['Abbv'],
            competition,
            season,
            start
        ))
        if (rs.with_rows):
            records = rs.fetchall()
        for item in records:
            if( item[0] > 0):
                team['GP'] = item[0]
                team['W'] = item[1]
                team['D'] = item[2]
                team['L'] = item[3]
                team['Points'] = (3 * team['W']) + team['D']
        return team

    def lookupTeamsBySeason(self, season, competition, start, log):
        """
        This looks up all team records that competed in a competition for a
        given year.
        """
        log.message('Looking up teams')
        self.teams = {}

        sql = ('SELECT HTeamID AS ID, t.team3ltr '
               'FROM tbl_games g '
               'INNER JOIN tbl_teams t ON g.HTeamID = t.ID '
               'INNER JOIN lkp_matchtypes m ON g.MatchTypeID = m.ID '
               'WHERE YEAR(matchtime) = %s '
               '  AND m.Abbv = %s '
               'UNION '
               'SELECT ATeamID AS ID, t.team3ltr '
               'FROM tbl_games g '
               'INNER JOIN tbl_teams t ON g.ATeamID = t.ID '
               'INNER JOIN lkp_matchtypes m ON g.MatchTypeID = m.ID '
               'WHERE YEAR(matchtime) = %s '
               '  AND m.Abbv = %s '
               'GROUP BY ID '
               'ORDER BY team3ltr')
        rs = self.db.query(sql, (
            season,
            competition,
            season,
            competition,
        ))
        if (rs.with_rows):
            records = rs.fetchall()
        for item in records:
            # Default team data
            team = {}
            team['ID'] = item[0]
            team['Abbv'] = item[1]
            team['Points'] = 0
            team['W'] = 0
            team['D'] = 0
            team['L'] = 0
            team['GP'] = 0
            # Look up actual data prior to start date
            team = self.initStandings(team, season, competition, start, log)
            self.teams[item[1]] = team

        self.team_count = len(records)
        log.message('Found ' + str(self.team_count) + ' teams')

        return self

    def printStandings(self):
        output = 'Team   Pts    GP\n'
        for item in self.teams:
            output += self.teams[item]['Abbv'].ljust(4) + '   ' +\
                      str(self.teams[item]['Points']).rjust(3) + '   ' +\
                      str(self.teams[item]['GP']).rjust(3) + '\n'

        return output

    def simulateSeason(self, games, model, log):

        self.initSeason()

        for i in range(games.game_count):
            log.message(str(games.games[i]))
            homeAbbv = games.games[i]['Home']
            awayAbbv = games.games[i]['Away']

            # For now, we pretend the home team always wins
            game = Game()
            result = game.simulateResult(games.games[i], model)
            log.message(str(result))

            # Update standings based on result
            self.updateStandings(homeAbbv, awayAbbv, result)

        return self

    def outputLine(self, field, collection):
        # This groups a given field, from a given dictionary, into a comma-
        # separated list in a string, which is suitable for writing to a log
        line = ''
        for item in collection:
            line += str(collection[item][field]) + ','
        return line

    def updateStandings(self, home, away, result):
        # This updates the standings based on the received result
        self.standings[home]['GP'] += 1
        self.standings[away]['GP'] += 1
        if('home' == result):
            self.standings[home]['Points'] += 3
        elif('draw' == result):
            self.standings[home]['Points'] += 1
            self.standings[away]['Points'] += 1
        elif('away' == result):
            self.standings[away]['Points'] += 3

# -*- coding: utf-8 -*-
from __future__ import absolute_import
import copy
from mais.record import Record


class League(Record):
    """
    Mais doesn't write anything back to this database, so we only need to
    implemnt the read methods.
    """

    def lookupTeamsBySeason(self, season, competition, log):
        """
        This looks up all team records that competed in a competition for a
        given year.
        """
        log.message('Looking up teams from ' + str(season) +
                    ' in ' + str(competition))
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
            team = {}
            team['ID'] = item[0]
            team['Abbv'] = item[1]
            team['Points'] = 0
            team['W'] = 0
            team['D'] = 0
            team['L'] = 0
            team['GP'] = 0
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

    def simulateSeason(self, games, log):

        self.standings = copy.deepcopy(self.teams)
        for i in range(games.game_count):
            log.message(str(games.games[i]))
            homeAbbv = games.games[i]['Home']
            awayAbbv = games.games[i]['Away']

            # For now, we pretend the home team always wins

            # Update standings based on result
            self.standings[homeAbbv]['GP'] += 1
            self.standings[homeAbbv]['Points'] += 3
            self.standings[awayAbbv]['GP'] += 1
            log.message(str(homeAbbv))
            # self.standings[homeID]['GP'] += 1
        return self

    def summarize(self, output):
        # This runs over the standings dictionary after a simulation pass has
        # finished, and writes out each team's point total in a single line
        # of the output file.
        # TODO: find a more pythonic way of doing this...
        line = ''
        for i in self.standings:
            line += str(self.standings[i]['Points']) + ','
        output.message(line)
        return self

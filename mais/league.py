# -*- coding: utf-8 -*-
from __future__ import absolute_import
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
        self.teams = []

        sql = ('SELECT HTeamID, t.team3ltr '
               'FROM tbl_games g '
               'INNER JOIN tbl_teams t ON g.HTeamID = t.ID '
               'INNER JOIN lkp_matchtypes m ON g.MatchTypeID = m.ID '
               'WHERE YEAR(matchtime) = %s '
               '  AND m.Abbv = %s '
               'GROUP BY t.ID '
               'ORDER BY HTeamID')
        rs = self.db.query(sql, (
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
            log.message(str(item))
            self.teams.append(team)

        self.team_count = len(records)

        return self

    def printStandings(self):
        output = 'Team   Pts    GP\n'
        for item in self.teams:
            output += item['Abbv'].ljust(4) + '   ' +\
                      str(item['Points']).rjust(3) + '   ' +\
                      str(item['GP']).rjust(3) + '\n'

        return output

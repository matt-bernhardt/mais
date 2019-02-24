# -*- coding: utf-8 -*-
from __future__ import absolute_import
from mais.record import Record


class Team(Record):
    """
    Mais doesn't write anything back to this database, so we only need to
    implemnt the read methods.
    """

    def lookupBySeason(self, season, competition):
        """
        This looks up all team records that competed in a competition for a
        given year.
        """
        teams = []

        sql = ('SELECT HTeamID, t.team3ltr '
               'FROM tbl_games g '
               'INNER JOIN tbl_teams t ON g.HTeamID = t.ID '
               'WHERE YEAR(matchtime) = %s '
               '  AND MatchTypeID = %s '
               'GROUP BY t.ID '
               'ORDER BY HTeamID')
        rs = self.db.query(sql, (
            season,
            competition,
        ))
        if (rs.with_rows):
            records = rs.fetchall()
        for item in records:
            teams.append(item[0])

        return teams
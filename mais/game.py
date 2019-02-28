# -*- coding: utf-8 -*-
from __future__ import absolute_import
from mais.record import Record


class Game(Record):
    """
    Mais doesn't write anything back to this database, so we only need to
    implemnt the read methods.
    """

    def lookupGamesBySeason(self, season, competition, log):
        """
        This looks up all team records that competed in a competition for a
        given year.
        """
        log.message('Looking up games from ' + str(season) + ' in ' + str(competition))
        self.games = []

        sql = ("SELECT g.ID, h.team3ltr AS Home, a.team3ltr AS Away "
               "FROM tbl_games g "
               "INNER JOIN tbl_teams h on g.HTeamID = h.ID "
               "INNER JOIN tbl_teams a on g.ATeamID = a.ID "
               "INNER JOIN lkp_matchtypes m ON g.MatchTypeID = m.ID "
               "WHERE YEAR(g.MatchTime) = %s "
               "AND m.Abbv = %s "
               "ORDER BY g.MatchTime ASC")
        rs = self.db.query(sql, (
            season,
            competition,
        ))
        if (rs.with_rows):
            records = rs.fetchall()
        for item in records:
            game = {}
            game['ID'] = item[0]
            game['Home'] = item[1]
            game['Away'] = item[2]
            self.games.append(game)
        self.game_count = len(records)
        log.message('Found ' + str(self.game_count) + ' games')

        return self

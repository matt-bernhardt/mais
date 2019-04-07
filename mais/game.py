# -*- coding: utf-8 -*-
from __future__ import absolute_import
import numpy as np
from mais.record import Record


class Game(Record):
    """
    Mais doesn't write anything back to this database, so we only need to
    implemnt the read methods.
    """

    def calculateThreshold(self, model):
        """
        This will eventually calculate different values for the home and draw
        thresholds based on parameters passed to it. For now, it just uses a
        1/3 1/3 1/3 distribution.
        """
        threshold = {}
        threshold['home'] = 0.3333
        threshold['draw'] = 0.6667
        return threshold

    def lookupGamesBySeason(self, season, competition, start, log):
        """
        This looks up all game records that took place in a competition
        during a given season after the chosen start date.
        """
        log.message('Looking up games')
        self.games = []

        sql = ("SELECT g.ID, h.team3ltr AS Home, a.team3ltr AS Away "
               "FROM tbl_games g "
               "INNER JOIN tbl_teams h on g.HTeamID = h.ID "
               "INNER JOIN tbl_teams a on g.ATeamID = a.ID "
               "INNER JOIN lkp_matchtypes m ON g.MatchTypeID = m.ID "
               "WHERE YEAR(g.MatchTime) = %s "
               "  AND MatchTime >= %s "
               "  AND m.Abbv = %s "
               "ORDER BY g.MatchTime ASC")
        rs = self.db.query(sql, (
            season,
            start,
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

    def simulateResult(self, context, model):
        """
        This calculates the result to a game. Possible return values are
        'home', 'draw', and 'away'
        """

        # Set the win/draw thresholds according to the selected model
        threshold = self.calculateThreshold(model)

        # Set result based on random value
        value = np.random.random(1)[0]
        result = 'away'
        if(value <= threshold['home']):
            result = 'home'
        elif(value <= threshold['draw']):
            result = 'draw'

        return result

# -*- coding: utf-8 -*-
from __future__ import absolute_import
import numpy as np
from mais.record import Record


class Game(Record):
    """
    Mais doesn't write anything back to this database, so we only need to
    implemnt the read methods.
    """

    def calculateThreshold(self, model, homedata, awaydata):
        """
        This implements a pythonic switch statement to return the relevant
        result thresholds.
        Source: Jaxenter.com 's article "How to implement a switch-case
        statement in Python'"
        """
        switcher = {
            'v0': self.modelV0,
            'v1': self.modelV1,
            'v2': self.modelV2
        }
        function = switcher.get(model, lambda: modelV1)
        gamecounts = function(homedata, awaydata)
        gamecounts['total'] = (gamecounts['home']
                               + gamecounts['draw']
                               + gamecounts['away'])
        gamecounts['homedraw'] = gamecounts['home'] + gamecounts['draw']
        threshold = {}
        threshold['home'] = gamecounts['home'] / gamecounts['total']
        threshold['draw'] = gamecounts['homedraw'] / gamecounts['total']
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

    def modelV0(self, homedata, awaydata):
        """
        This is an extremely naive model which sets each game result as
        equally likely: a 1/3 1/3 1/3 distribution.
        """
        # We don't use home or away data in this model.
        homedata = ""
        awaydata = ""
        data = {}
        data['home'] = 1
        data['draw'] = 1
        data['away'] = 1
        return data

    def modelV1(self, homedata, awaydata):
        """
        The v1 model is the first one that I started using, which is based on
        actual home field advantage in MLS - across all teams and from 2011 -
        2017.
        """
        # We don't use home or away data in this model.
        homedata = ""
        awaydata = ""
        data = {}
        data['home'] = 972.0
        data['draw'] = 533.0
        data['away'] = 450.0
        return data

    def modelV2(self, homedata, awaydata):
        """
        The v2 model is the second one that I started using, which is based on
        a combination of home field advantage and team PPG at kickoff. It uses
        data from home games between 2011 and 2018.
        """
        # Calculate PPG, because we have not yet.
        homePPG = 0.0
        awayPPG = 0.0
        if (homedata['GP'] > 0):
            homePPG = homedata['Points'] / homedata['GP']
        if (awaydata['GP'] > 0):
            awayPPG = awaydata['Points'] / awaydata['GP']
        # Default values (if PPG are equal)
        data = {}
        data['home'] = 58.0
        data['draw'] = 26.0
        data['away'] = 33.0
        if (homePPG > awayPPG):
            # If home team is better...
            data['home'] = 481.0
            data['draw'] = 229.0
            data['away'] = 171.0
        elif (homePPG < awayPPG):
            # If away team is better...
            data['home'] = 433.0
            data['draw'] = 278.0
            data['away'] = 246.0

        return data

    def simulateResult(self, context, homedata, awaydata, model):
        """
        This calculates the result to a game. Possible return values are
        'home', 'draw', and 'away'
        """

        # Set the win/draw thresholds according to the selected model
        threshold = self.calculateThreshold(model, homedata, awaydata)

        # Set result based on random value
        value = np.random.random(1)[0]
        result = 'away'
        if(value <= threshold['home']):
            result = 'home'
        elif(value <= threshold['draw']):
            result = 'draw'

        return result

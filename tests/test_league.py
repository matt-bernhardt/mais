# -*- coding: utf-8 -*-
from __future__ import absolute_import
import pytest
from mais.game import Game
from mais.league import League
from mais.log import Log


def test_league_init():
    l = League()
    # object types
    assert isinstance(l, League)
    assert isinstance(l.data, dict)
    # Default values
    assert l.data['ID'] == 0


def test_league_connection():
    l = League()
    assert hasattr(l, 'db') is False
    l.connectDB()
    assert hasattr(l, 'db')
    l.disconnectDB()
    assert hasattr(l, 'db') is False


def test_league_initSeason():
    log = Log('test.log')
    l = League()
    l.connectDB()
    l.lookupTeamsBySeason(1996, 'mls', '1996-01-01', log)
    assert l.teams['CLB']['GP'] == 0
    assert l.teams['CLB']['W'] == 0
    l.lookupTeamsBySeason(1996, 'mls', '1996-06-01', log)
    assert l.teams['CLB']['GP'] == 9
    assert l.teams['CLB']['W'] == 3


def test_league_lookupTeamsBySeason():
    log = Log('test.log')
    l = League()
    l.connectDB()
    l.lookupTeamsBySeason(1900, 'mls', '1900-01-01', log)
    assert len(l.teams) == 0
    l.lookupTeamsBySeason(1996, 'foo', '1996-01-01', log)
    assert len(l.teams) == 0
    l.lookupTeamsBySeason(1996, 'mls', '1996-01-01', log)
    assert len(l.teams) == 10


def test_league_outputLine():
    log = Log('test.log')
    l = League()
    l.connectDB()
    l.lookupTeamsBySeason(1996, 'mls', '1996-01-01', log)
    line = l.outputLine('Abbv', l.teams)
    assert line == 'CLB,COL,DAL,DC,KC,LA,NE,NY,SJ,TB,'


def test_league_printStandings():
    log = Log('test.log')
    l = League()
    l.connectDB()
    l.lookupTeamsBySeason(1900, 'foo', '1900-01-01', log)
    output = l.printStandings()
    assert output == 'Team   Pts    GP\n'
    l.lookupTeamsBySeason(1996, 'mls', '1996-01-01', log)
    output = l.printStandings()
    assert len(output) > 0


def test_league_simulateSeason():
    log = Log('test.log')
    model = 'v0'
    g = Game()
    g.connectDB()
    g.lookupGamesBySeason(1996,'mls', '1996-01-01', log)
    l = League()
    l.connectDB()
    l.lookupTeamsBySeason(1996, 'mls', '1996-01-01', log)
    l.simulateSeason(g, model, log)
    assert l.standings['CLB']['GP'] == 32

def test_league_updateStandings():
    log = Log('test.log')
    l = League()
    l.connectDB()
    l.lookupTeamsBySeason(1996, 'mls', '1996-01-01', log)
    l.initSeason()
    # Initial
    assert l.standings['SJ']['GP'] == 0
    assert l.standings['SJ']['Points'] == 0
    assert l.standings['DC']['Points'] == 0
    # Home win
    l.updateStandings('SJ', 'DC', 'home')
    assert l.standings['SJ']['GP'] == 1
    assert l.standings['DC']['GP'] == 1
    assert l.standings['SJ']['Points'] == 3
    assert l.standings['DC']['Points'] == 0
    # Away win
    l.initSeason()
    l.updateStandings('SJ', 'DC', 'away')
    assert l.standings['SJ']['GP'] == 1
    assert l.standings['DC']['GP'] == 1
    assert l.standings['SJ']['Points'] == 0
    assert l.standings['DC']['Points'] == 3
    # Draw
    l.initSeason()
    l.updateStandings('SJ', 'DC', 'draw')
    assert l.standings['SJ']['GP'] == 1
    assert l.standings['DC']['GP'] == 1
    assert l.standings['SJ']['Points'] == 1
    assert l.standings['DC']['Points'] == 1

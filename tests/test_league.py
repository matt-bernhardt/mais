# -*- coding: utf-8 -*-
from __future__ import absolute_import
import pytest
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


def test_league_lookupTeamsBySeason():
    log = Log('test.log')
    l = League()
    l.connectDB()
    l.lookupTeamsBySeason(1900, 'mls', log)
    assert len(l.teams) == 0
    l.lookupTeamsBySeason(1996, 'foo', log)
    assert len(l.teams) == 0
    l.lookupTeamsBySeason(1996, 'mls', log)
    assert len(l.teams) > 0


def test_league_outputLine():
    log = Log('test.log')
    l = League()
    l.connectDB()
    l.lookupTeamsBySeason(1996, 'mls', log)
    line = l.outputLine('Abbv', l.teams)
    assert line == 'CLB,COL,DAL,DC,KC,LA,NE,NY,SJ,TB,'


def test_league_printStandings():
    log = Log('test.log')
    l = League()
    l.connectDB()
    l.lookupTeamsBySeason(1900, 'foo', log)
    output = l.printStandings()
    assert output == 'Team   Pts    GP\n'
    l.lookupTeamsBySeason(1996, 'mls', log)
    output = l.printStandings()
    assert len(output) > 0

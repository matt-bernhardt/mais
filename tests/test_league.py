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
    l = League()
    l.connectDB()

    #

# -*- coding: utf-8 -*-
from __future__ import absolute_import
import pytest
from mais.game import Game
from mais.log import Log


def test_game_init():
    g = Game()
    # object types
    assert isinstance(g, Game)
    assert isinstance(g.data, dict)
    # Default values
    assert g.data['ID'] == 0


def test_game_connection():
    g = Game()
    assert hasattr(g, 'db') is False
    g.connectDB()
    assert hasattr(g, 'db')
    g.disconnectDB()
    assert hasattr(g, 'db') is False


def test_game_lookupGamesBySeason():
    log = Log('test.log')
    g = Game()
    g.connectDB()
    g.lookupGamesBySeason(1900, 'mls', log)
    assert len(g.games) == 0
    g.lookupGamesBySeason(1996, 'foo', log)
    assert len(g.games) == 0
    g.lookupGamesBySeason(1996, 'mls', log)
    assert len(g.games) == 160

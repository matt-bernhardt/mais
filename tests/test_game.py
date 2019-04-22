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


def test_game_calculateThreshold():
    log = Log('test.log')
    model = 'v0'
    g = Game()
    # This tests the ability to get back different models based on a passed
    # parameter.
    threshold = g.calculateThreshold(model)
    assert threshold['home'] == 0.3333
    model = 'v1'
    threshold = g.calculateThreshold(model)
    assert threshold['home'] == 972.0 / 1955.0


def test_game_lookupGamesBySeason():
    log = Log('test.log')
    g = Game()
    g.connectDB()
    g.lookupGamesBySeason(1900, 'mls', '1900-01-01', log)
    assert len(g.games) == 0
    g.lookupGamesBySeason(1996, 'foo', '1996-01-01', log)
    assert len(g.games) == 0
    g.lookupGamesBySeason(1996, 'mls', '1996-01-01', log)
    assert len(g.games) == 160


def test_game_modelV0():
    log = Log('test.log')
    model = 'v0'
    g = Game()
    threshold = g.modelV0()
    assert threshold['home'] == 0.3333
    assert threshold['draw'] == 0.6667


def test_game_modelV1():
    log = Log('test.log')
    model = 'v1'
    g = Game()
    threshold = g.modelV1()
    assert threshold['home'] == 972.0 / 1955.0
    assert threshold['draw'] == 1505.0 / 1955.0


def test_game_simulateResult():
    log = Log('test.log')
    model = 'v0'
    g = Game()
    context = {}
    # This is hacky, but should generally protect against unexpected results
    # being returned. I'm not so concerned here about testing randomness, or
    # specific distributions of results. That is numpy's problem.
    assert g.simulateResult(context, model) in ['home', 'draw', 'away']
    assert g.simulateResult(context, model) in ['home', 'draw', 'away']
    assert g.simulateResult(context, model) in ['home', 'draw', 'away']
    assert g.simulateResult(context, model) in ['home', 'draw', 'away']
    assert g.simulateResult(context, model) in ['home', 'draw', 'away']
    assert g.simulateResult(context, model) in ['home', 'draw', 'away']

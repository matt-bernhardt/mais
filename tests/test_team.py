# -*- coding: utf-8 -*-
from __future__ import absolute_import
import pytest
from mais.team import Team
from mais.log import Log


def test_team_init():
    t = Team()
    # object types
    assert isinstance(t, Team)
    assert isinstance(t.data, dict)
    # Default values
    assert t.data['ID'] == 0


def test_team_connect():
    t = Team()
    assert hasattr(t, 'db') is False
    t.connectDB()
    assert hasattr(t, 'db')


def test_team_disconnect():
    t = Team()
    t.connectDB()
    assert hasattr(t, 'db')
    t.disconnectDB()
    assert hasattr(t, 'db') is False


def test_team_lookupBySeason():
    t = Team()
    t.connectDB()

    #

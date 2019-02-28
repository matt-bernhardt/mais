# -*- coding: utf-8 -*-
from __future__ import absolute_import
import pytest
from mais.record import Record
import datetime


def test_record_init():
    r = Record()
    # object types
    assert isinstance(r, Record)
    assert isinstance(r.data, dict)
    # Default values
    assert r.data['ID'] == 0


def test_record_connect():
    r = Record()
    assert hasattr(r, 'db') is False
    r.connectDB()
    assert hasattr(r, 'db')


def test_record_disconnect():
    r = Record()
    r.connectDB()
    assert hasattr(r, 'db')
    r.disconnectDB()
    assert hasattr(r, 'db') is False

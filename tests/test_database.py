# -*- coding: utf-8 -*-
from __future__ import absolute_import
from mais.database import Database


def test_database_init():
    d = Database()
    assert d.cnx == ''
    assert d.cursor == ''


def test_database_query():
    d = Database()
    d.connect()
    # Inserts
    sql = ('INSERT INTO tbl_games '
           '(MatchTime, MatchTypeID) '
           'VALUES '
           '(%s, %s)')
    params = ('1960-01-01 19:30:00', 1, )
    rs = d.query(sql, params)
    assert d.warnings() is None
    # Updates
    sql = ('UPDATE tbl_games '
           'SET HteamID = %s '
           'WHERE MatchTime = %s AND MatchTypeID = %s')
    rs = d.query(sql, (1, '1960-01-01 19:30:00', 1, ))
    assert d.warnings() is None
    # Selects
    sql = ('SELECT ID '
           'FROM tbl_games '
           'WHERE MatchTime = %s AND MatchTypeID = %s')
    rs = d.query(sql, params)
    if (rs.with_rows):
        records = rs.fetchall()
    for term in records:
        needleID = records[0][0]
    assert needleID > 0
    assert d.warnings() is None
    # Deletes
    sql = ('DELETE FROM tbl_games '
           'WHERE MatchTime = %s AND MatchTypeID = %s')
    rs = d.query(sql, params)
    assert d.warnings() is None
    d.disconnect()


def test_database_convertDate():
    d = Database()
    testDate = (1996, 4, 13, 19, 30, 0, 0, 0, 0)
    assert d.convertDate(testDate) == '1996-04-13 19:30:00'

def test_database_lastInsertID():
    d = Database()
    d.connect()
    # LAST_INSERT_ID() is zero if you haven't done anything yet
    assert d.lastInsertID() == 0
    sql = ('INSERT INTO tbl_games '
           '(MatchTime, MatchTypeID) '
           'VALUES '
           '(%s, %s)')
    params = ('1960-01-01 19:30:00', 1, )
    d.query(sql, params)
    # Now that we've inserted something, LAST_INSERT_ID() should be positive
    assert d.lastInsertID() > 0
    # Clean up our mess
    sql = ('DELETE FROM tbl_games '
           'WHERE MatchTime = %s AND MatchTypeID = %s')
    rs = d.query(sql, params)

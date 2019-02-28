# -*- coding: utf-8 -*-
from __future__ import absolute_import
from mais.database import Database


class Record():

    def __init__(self):
        self.data = {}
        self.data["ID"] = 0

    def connectDB(self):
        self.db = Database()
        self.db.connect()

    def disconnectDB(self):
        self.db.disconnect()
        del self.db

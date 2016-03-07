# -*- coding: utf-8 -*-

from django.db import connection

class row(object):
    def __init__(self, row, columns):
        self._columns = columns
        self._rowdict = dict(zip(columns, row))
        print self._rowdict


    def keys(self):
        return self._columns


    def __getattr__(self, attr):
        return self._rowdict[attr]

    def __getitem__(self, item):
        return self._rowdict[item]


class dataSet(object):
    def __init__(self, data, columns ):
        self._data = data
        self._columns = columns


    def __getitem__(self, item):
        return row(self._data[item], self._columns)


class db(object):

    def __init__(self):
        self._cursor = connection.cursor()

    def select(self, sql):
        print sql
        self._cursor.execute(sql)
        columns = [col[0].lower() for col in self._cursor.description]
        print "列名", columns
        return dataSet(self._cursor.fetchall(), columns)


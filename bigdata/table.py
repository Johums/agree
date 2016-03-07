# -*- coding: utf-8 -*-

from utils import db

class table(object): """get table struct info""" def __init__(self, table):
    self._table = table.upper()

        if self._table.find(".") > 0:
            self._owner, self._table = self._table.split(".")
       else:
            self._owner = ""

        # print "对象: ", self.ower
        # print self.primaryKey
        # print self.indexs

    def __repr__(self):
        return self._table

    @property
    def owner(self):
        """get table ower """
        if not hasattr(self, "_owner") or self._owner == "":
            sql = """
            SELECT owner FROM all_tables WHERE table_name = '{self._table}'
            """.format(self = self)

            ret = db().select(sql)
            owner = ret[0].owner

            if self._owner and self._owner != owner:
                raise ValueError("表所对应的用户不一致!")

            self._owner = owner

        return self._owner

    @property
    def column(self):
        """return column info"""
        if not hasattr(self, "_column"):
            sql = """
            SELECT t1.column_name,
                   t1.data_type,
                   t1.data_length,
                   t1.nullable,
                   t2.comments
              FROM all_tab_columns t1
             INNER JOIN all_col_comments t2
                ON t1.table_name = t2.table_name
               AND t1.column_name = t2.column_name
             WHERE t1.owner = '{self._ower}'
               AND t1.table_name = '{self._table}'
            ORDER BY column_id
            """.format(self = self)
            ret = db().select(sql)
            self._column = ret
        return self._column


    @property
    def primaryKey(self):
        if not hasattr(self, "_pkinfo"):
            sql = """
            SELECT cu.*
              FROM all_cons_columns cu, all_constraints au
             WHERE cu.constraint_name = au.constraint_name
               and au.constraint_type = 'P'
               and au.table_name = '{self._table}'
             ORDER BY POSITION
            """.format(self = self)
            ret = db().select(sql)
            self._pkinfo = ret
            self._pkcol = list()
            if ret:
                self._pkcol = map(lambda x: x["column_name"], self._pkinfo)
        return self._pkinfo


    @property
    def indexs(self):
        if not hasattr(self, "_index"):
            sql = """
            SELECT index_name
              FROM all_indexes
            WHERE table_name = '{self._table}'
            and owner = '{self._owner}'
            """.format(self = self)

            ret = db().select(sql)
            self._index = list()
            if ret:
                self._index = map(lambda x: x["index_name"], ret)
        return self._index


    def getWhereList(self):
        return self._whereList


    def setWhereList(self, whereList):
        if not isinstance(whereList, list) :
            raise TypeError("类型异常")
        self._whereList = whereList

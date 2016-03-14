# -*- coding: utf-8 -*-

import ConfigParser

class iteminfo(object):

    def __init__(self, items, options):
        self._options = options
        self._itemdict = dict(items)


    def __getattr__(self, attr):
        if not attr in self._options:
            raise ValueError("{0} 不在 {1}里面".format(attr, self._options))
        return self._itemdict[attr]


class baseparser(object):

    def __init__(self, filename):
        self._parser = ConfigParser.ConfigParser()
        self._parser.read(filename)


    @property
    def sections(self):
        if not hasattr(self, "_sections"):
            self._sections = self._parser.sections()
        return self._sections


    def options(self, section):
        if not hasattr(self, "_options"):
            self._options = self._parser.options(section)
        return self._options


    def __getitem__(self, section):
        if section not in self.sections:
            raise ValueError("不存在{0}节点".format(section))
        return iteminfo(self._parser.items(section), self.options(section))


if __name__ == '__main__':
    parser = baseparser("../conf/db.conf")
    print parser["devop_env"].host

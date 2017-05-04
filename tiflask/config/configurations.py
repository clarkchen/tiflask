# -*- coding:utf-8 -*-
__author__ = 'clarkchen'

import os
root = os.path.dirname(__file__)

import sys
py_version = sys.version[0]

try:

    import ConfigParser as config_parser
except Exception:
    import configparser as config_parser

class WecashConfig:
    def __init__(self):
        """
        输入 test 或者是 local
        :param config_dir:
        :return:
        """
        config_dir = "local"
        config = config_parser.ConfigParser()
        if sys.version[0] == "2":
            config.readfp(open("{0}/{1}/defaults.cfg".format(root, config_dir)))
        if sys.version[0] == "3":
            config.read_file(open("{0}/{1}/defaults.cfg".format(root, config_dir)))

        self.config = config

    def get(self, key, field):
        return self.config.get(key, field)

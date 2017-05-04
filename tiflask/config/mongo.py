# -*- coding:utf-8 -*-
__author__ = 'clarkchen'



class MongoConfig(object):
    def __init__(self, wecash_config, db_config_name):
        self.__set_up_configurations(wecash_config, db_config_name)

    def __set_up_configurations(self, wecash_config, db_config_name):
        self.host = wecash_config.get(db_config_name, 'host')
        self.user = wecash_config.get(db_config_name, 'user')
        self.passwd = wecash_config.get(db_config_name, 'passwd')
        self.db_name = wecash_config.get(db_config_name, 'db_name')


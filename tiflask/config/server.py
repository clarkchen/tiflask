# -*- coding:utf-8 -*-
__author__ = 'clarkchen'


class ServerConfig:
    def __init__(self, wecash_config, server_key):
        self.__set_up_configurations(wecash_config, server_key)

    def __set_up_configurations(self, wecash_config, server_key):
        self.port = wecash_config.get(server_key, 'port')
        self.version = wecash_config.get(server_key, 'version')
        self.project_name = wecash_config.get(server_key, "project_name")
        self.elk_sign = wecash_config.get(server_key, "elk_sign")
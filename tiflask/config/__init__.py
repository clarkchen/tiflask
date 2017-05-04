# -*- coding:utf-8 -*-
__author__ = 'clarkchen'

from .configurations import WecashConfig

wecash_config = WecashConfig()


from .server import *
server_config = ServerConfig(wecash_config, 'server-config')

from .mysql import *
mysql_user_config = MysqlConfig(wecash_config, "mysql_user_info")

from .mongo import *
mongo_article_config = MongoConfig(wecash_config,"mongodb_article")

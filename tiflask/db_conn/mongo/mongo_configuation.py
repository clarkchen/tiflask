# -*- coding:utf-8 -*-


__author__ = 'clarkchen'
from pymongo import MongoClient
from tiflask.config import *
from signal import *
import sys
import atexit


def _init_client(mongo_config, **kwargs):
    """
    初始化 Mongo Client 全局针对一个db只需要生成一次就行
    每个 MongoClient 自带线程池
    :return:
    """
    client = MongoClient(mongo_config.host, **kwargs)
    db = getattr(client, mongo_config.db_name)
    db.authenticate(mongo_config.user, mongo_config.passwd)
    db_name = mongo_config.db_name
    return client, getattr(client, db_name)



def get_collection(db, collection_name):
    """
    初始化到某一个具体的 Collection，需要每次动态调用
    :param collection_name: 需要用户自己来指定
    :return:
    """
    return getattr(db, collection_name)



common_settings = {
    "serverSelectionTimeoutMS": 10*1000, # 初次建立连接的时候, 默认连接时长, 如果 mongo挂了 这里就是最大连接时长, ms为单位
    "connectTimeoutMS":10*1000, # 心跳检测中,最长响应时间
    "socketTimeoutMS":10*1000,# 已经建立了的连接, 执行一次查询最大等候时间
    "maxPoolSize":100,
    "minPoolSize":0,
    "waitQueueMultiple":10,
}


# 连接文章的Mongo客户端
client_to_mongo, article_db = _init_client(mongo_article_config, **common_settings)  # 线程池


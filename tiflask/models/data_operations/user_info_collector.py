# -*- coding:utf-8 -*-
from tiflask.objects import UserInfo

__author__ = 'clarkchen'
from tiflask.dao import UserInfoDao, ArticleInfoDao
import logging
from tiflask.utils import is_blank


class UserInfoCollector(object):
    def __init__(self ):
        self.logger = logging.getLogger(type(self).__name__)
        # 数据访问类
        self.user_dao = UserInfoDao()
        self.article_dao = ArticleInfoDao()

    def prepare_user_info(self, phone):
        """
        收集用户基本信息 和 用户的阅读信息 和文章信息
        :return:
        """
        # 读取基本信息
        user_info = self.user_dao.get_user_base_info(phone)

        # 读取阅读关系
        article_list = self.user_dao.get_user_article_relation(user_info.id)
        user_info.articles = article_list

        # 读取文章内容
        article_id_list = [x.article_id for x in user_info.get_article_iterator()]
        ret_list = self.article_dao.get_article_info(article_id_list)
        a_dict = user_info.articles
        for item in ret_list:
            if item.article_id in a_dict:
                a_dict[item.article_id].article = item

        return user_info
# -*- coding:utf-8 -*-
import arrow as ar
import logging
from tiflask.utils import *

from tiflask.objects import UserInfo
__author__ = 'clarkchen'


class FeatureGenerator(object):
    def __init__(self ):
        self.logger = logging.getLogger(type(self).__name__)

    def get_features(self, user_info):
        """
        用户总共阅读过多少篇文章 read_article_num
        总共阅读过多少类的文章  read_article_type_num
        最近3个月总共阅读过多少文章  recent_3_read_article_num
        最近三个月总共阅读过多少类别的文章  recent_3_read_article_type_num

        :param user_info:
        :return:
        """

        assert isinstance(user_info, UserInfo)

        recent_3_month = ar.get(get_today() - datetime.timedelta(days=30*3)).naive

        read_article_num = 0
        read_article_type_num = set()
        recent_3_read_article_num = 0
        recent_3_read_article_type_num = set()

        for article_item in user_info.get_article_iterator():
            read_article_num+=1
            a_type = article_item.article.article_type
            read_article_type_num.add(a_type)
            read_time = article_item.create_time
            if read_time>recent_3_month:
                recent_3_read_article_num += 1
                recent_3_read_article_type_num.add(a_type)

        features = {}
        features["read_article_num"] = read_article_num

        features["read_article_type_num"] = len(read_article_type_num)

        features["recent_3_read_article_num"] = recent_3_read_article_num

        features["recent_3_read_article_type_num"] = len(recent_3_read_article_type_num)

        self.logger.info("user {user_id}, phone {phone}, features is {features}".format(user_id = user_info.id, phone=user_info.phone, features=features))

        return features




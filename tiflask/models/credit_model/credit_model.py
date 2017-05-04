# -*- coding:utf-8 -*-
__author__ = 'clarkchen'

import logging
from tiflask.objects import UserInfo



class CreditModel(object):
    def __init__(self ):
        self.logger = logging.getLogger(type(self).__name__)

    def cal_score(self, user_info, features):
        """
        返回用户有多喜欢阅读的分值
        :param user_info:
        :return:
        """
        assert isinstance(user_info, UserInfo)

        score =features["read_article_num"]  * 5 +  features["read_article_type_num"] *3 + features["recent_3_read_article_num"] *6 + features["recent_3_read_article_type_num"]*8

        self.logger.info("user {user_id}, phone {phone}, score is {score}".format(user_id = user_info.id, phone=user_info.phone, score=score))

        return score


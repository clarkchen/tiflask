# -*- coding:utf-8 -*-
__author__ = 'clarkchen'

import logging
from tiflask.db_conn import user_db
from tiflask.utils import is_blank

from tiflask.objects import UserInfo, UserArticleRelation

class UserInfoDao(object):
    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)

    def get_user_base_info(self, phone):
        """
        根据用户电话获得用户信息
        :param phone:
        :return:
        """
        ret = None
        try:
            sql = """
                select id, name, reg_date, phone, province,
                city from user_info where phone = :phone
            """
            result_iter = user_db.query(sql, phone=phone)
            result = [x for x in result_iter]
            if isinstance(result, list) and len(result)>0:
                ret = result[0]
                ret = UserInfo(ret)
        except Exception as e:
            self.logger.exception(e)
        finally:
            return ret

    def get_user_article_relation(self, user_id):
        """
           根据用户ID获得用户的阅读情况
        :param phone:
        :return:
        """
        ret = None

        try:
           sql = """
                select id, user_id, article_id, create_time from user_read_article where user_id = :user_id
           """
           result_iter = user_db.query(sql, user_id=user_id)
           result = [x for x in result_iter]
           if isinstance(result, list) and len(result)>0:
                ret = [UserArticleRelation(x) for x in result]
        except Exception as e:
            self.logger.exception(e)
        finally:
            return ret

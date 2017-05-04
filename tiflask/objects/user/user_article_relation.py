# -*- coding:utf-8 -*-
import datetime

__author__ = 'clarkchen'

from tiflask.objects import ArticleItem
from tiflask.utils import show_getter_setter_method, convert_str_to_time

class UserArticleRelation(object):
    """
    article 结构
    {
        "_id" : ObjectId("55a4053c1996630412cadc0e"),
        "title" : "港媒称吉林与朝接壤农村成朝鲜新娘聚居地",
        "content" : "香港《东方日报》7月10日报道，朝鲜政府关闭正常的涉外登记渠道，令这些女性只能偷渡赴中国。朝鲜女性因偷渡到中国，大多是嫁给条件差的中国人。",
        "author_phone" : "18500195632"
    }
    """
    def __init__(self, user_info):
        """Convert a dictionary to a class
        @param :adict Dictionary
        """
        if not isinstance(user_info, dict):
            return
        self._id = user_info.get("id")
        self._user_id = user_info.get("user_id")
        self._article_id = user_info.get("article_id")
        self._create_time = user_info.get("create_time")
        self._article = None

    @property
    def create_time(self):
        if not isinstance(self._create_time, datetime.datetime):
            self._create_time = convert_str_to_time(self._create_time)
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


    @property
    def article_id(self):
        return self._article_id

    @article_id.setter
    def article_id(self, value):
        self._article_id = str(value)


    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def article(self):
        return self._article if isinstance(self._article, ArticleItem) else None

    @article.setter
    def article(self, value):
        assert isinstance(value, ArticleItem)
        self._article = value


if __name__ == '__main__':
    print (show_getter_setter_method(UserArticleRelation({})))
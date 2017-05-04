# -*- coding:utf-8 -*-
__author__ = 'clarkchen'

import logging
from tiflask.utils import is_blank, show_getter_setter_method

"""
Mongo 数据库中对于单篇文章的抽象类
"""


class ArticleItem(object):
    """
    article 结构
    {
        "_id" : ObjectId("55a4053c1996630412cadc0e"),
        "title" : "港媒称吉林与朝接壤农村成朝鲜新娘聚居地",
        "content" : "香港《东方日报》7月10日报道，朝鲜政府关闭正常的涉外登记渠道，令这些女性只能偷渡赴中国。朝鲜女性因偷渡到中国，大多是嫁给条件差的中国人。",
        "author_phone" : "18500195632"
    }
    """
    def __init__(self, article_json):
        """Convert a dictionary to a class
        @param :adict Dictionary
        """
        if not isinstance(article_json, dict):
            return
        self._title = article_json.get("title")
        self._content = article_json.get("content")
        self._author_phone = article_json.get("author_phone")
        self._article_type = article_json.get("type")
        self._article_id = article_json.get("article_id")

    def is_blank(self):
        return is_blank(self.title)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, input_title):
        if "nice" in input_title:
            self._title = input_title.replace("nice", "you")
        else:
            self._title = input_title

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, input_c):
        self._content = input_c

    @property
    def author_phone(self):
        return self._author_phone

    @author_phone.setter
    def author_phone(self,value):
        self._author_phone = value

    @property
    def article_id(self):
        return self._article_id

    @article_id.setter
    def article_id(self, value):
        self._article_id = value

    @property
    def article_type(self):
        return self._article_type

    @article_type.setter
    def article_type(self, value):
        self._article_type = value

if __name__ == '__main__':
    print (show_getter_setter_method(ArticleItem({})))
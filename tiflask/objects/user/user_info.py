# -*- coding:utf-8 -*-

from .user_article_relation import UserArticleRelation
from tiflask.utils.gsetter import show_getter_setter_method

__author__ = 'clarkchen'



class UserInfo(object):
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
        self._name = user_info.get("name")
        self._reg_date = user_info.get("reg_date")
        self._phone = user_info.get("phone")

        self._province = user_info.get("province")
        self._city = user_info.get("city")
        self._articles = {}

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def reg_date(self):
        return self._reg_date

    @reg_date.setter
    def reg_date(self, value):
        self._reg_date = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def articles(self):
        return self._articles

    @articles.setter
    def articles(self, value):
        self._articles = {x.id: x for x in value if isinstance(x, UserArticleRelation)}

    def get_article_iterator(self):
        """
        文档的迭代器
        :return:
        """
        for item in self._articles.values():
            if not isinstance(item, UserArticleRelation): continue
            yield item

if __name__ == '__main__':
    print (show_getter_setter_method(UserInfo({})))
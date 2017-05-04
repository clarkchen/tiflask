# -*- coding:utf-8 -*-

__author__ = 'clarkchen'

from tiflask.db_conn import get_collection, article_db
from tiflask.utils import *

from tiflask.objects import ArticleItem


class ArticleInfoDao(object):
    demo_article_collection = None

    def get_article_collection(self):
        if self.demo_article_collection is None:
            self.demo_article_collection = get_collection(article_db, "demo_articles")
        return self.demo_article_collection

    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)

    def get_article_info(self, article_ids):
        """
        从给定的文章id 中获取文章的具体内容
        :param article_ids: 文章编号
        :return: 
        """
        ret_list = None
        try:
            mongo_iter = self.get_article_collection().find({"article_id": {"$in": article_ids}})
            ret_list = [ArticleItem(x) for x in mongo_iter]
        except Exception as e:
            self.logger.exception(e)
        finally:
            return ret_list

if __name__ == '__main__':
    dao = ArticleInfoDao()
    print (dao.get_article_info([1,2]))
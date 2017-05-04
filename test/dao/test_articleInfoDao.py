from unittest import TestCase

from tiflask.dao import ArticleInfoDao


class TestArticleInfoDao(TestCase):
    def test_get_article_info(self):
        """
        difldjflkjdkfjaskdf
        :return:
        """
        article_id = 1
        article_dao = ArticleInfoDao()
        article_list = article_dao.get_article_info([article_id])
        for one_article in article_list:
            print (one_article.title)
            self.assertIsNotNone(one_article.content)

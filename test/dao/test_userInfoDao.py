from unittest import TestCase

from tiflask.dao import UserInfoDao


class TestUserInfoDao(TestCase):
    def test_get_user_article_relation(self):
        dao = UserInfoDao()
        phone = "18500195632"
        user_info = dao.get_user_base_info(phone)
        # print (user_info.phone)
        self.assertIsNotNone(user_info.phone)
        user_id = user_info.id

        relation_info_list = dao.get_user_article_relation(user_id)
        for x in relation_info_list:
            print(x.article_id)
            self.assertIsNotNone(x.article_id)

    def test_get_user_base_info(self):
        dao = UserInfoDao()
        phone = "18500195632"
        user_info = dao.get_user_base_info(phone)
        print(user_info.phone)
        self.assertIsNotNone(user_info.phone)
from unittest import TestCase

from tiflask.app import app
import json

class TestUserInfoController(TestCase):
    def setUp(self):
        self.app = app.test_client(use_cookies=False)

    def test_get(self):
        ret = self.app.get("/api/user_score")
        print (ret.data)

    def test_post(self):
        param_data = {"phone": "18500195632"}

        ret = self.app.post("/api/user_score", data=param_data)
        print(ret.data)
# -*- coding:utf-8 -*-
__author__ = 'clarkchen'
from unittest import TestCase
import requests, json
from tiflask.utils import *


class TestService(TestCase):
    def setUp(self):
        print("testing TestService")

    def test_local_service_post(self):
        url = "http://127.0.0.1:5000/api/user_score"
        data = {"phone": "18500195632"}

        ret_value = requests.post(url, json=data)
        clark = json.loads(ret_value.text, encoding="utf-8")
        # encode_to_utf8(clark)
        print(json.dumps(clark), ret_value.status_code)

    def test_local_service_get(self):
        url = "http://127.0.0.1:5000/api/user_score"
        data = {"phone": "18500195632"}

        ret_value = requests.get(url, json=data)
        print(ret_value.status_code)
        clark = json.loads(ret_value.text, encoding="utf-8")
        print(json.dumps(clark), ret_value.status_code)

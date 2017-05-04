# -*- coding:utf-8 -*-
from multiprocessing.dummy import Pool

__author__ = 'clarkchen'
from unittest import TestCase
import requests, json
from tiflask.utils import *
import arrow as ar

def send_request(url, data):
    ret_value = requests.post(url, json=data)
    return json.loads(ret_value.text)

class TestService(TestCase):
    def setUp(self):
        print("testing TestService")
        self.pool_size = 20

    def test_local_service_post_multi(self):
        # url = "http://192.168.121.33:5080/api/user_score"
        url = "http://127.0.0.1:5000/api/user_score"
        data = {"phone": "18500195632"}
        pool = Pool(self.pool_size)
        start = ar.get()
        result = [pool.apply_async(send_request, args=(url, data))for x in range(10*self.pool_size)]

        pool.close()
        pool.join()
        result_set = set()
        for i, x in enumerate( result):
            result = x.get()
            print(i)
            result_set.add(json.dumps(result.get("data")))

        end = ar.get()
        print("total consume time is {sec} result set len is {l}".format(sec = (end-start).seconds, l=len(result_set)))

        for x in result_set:
            print("-"*20)
            print(x)
        # 直接运行 threaded 模式 total consume time is 37 result set len is 1
        # gunicorn模式 thread 模式 total consume time is 12 result set len is 1
        # gunicorn模式 total consume time is 47 result set len is 1
# -*- coding:utf-8 -*-
from unittest import TestCase

from tiflask.utils import clear_address, is_zhixia

__author__ = 'clarkchen'


class TestClear_address(TestCase):
    def test_clear_address(self):
        city = u"北京,朝阳"
        print(",".join(clear_address(city).values()))
        print (is_zhixia(city))
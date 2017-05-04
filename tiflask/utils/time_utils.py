# -*- coding:utf-8 -*-
import logging

__author__ = 'clarkchen'
import datetime
import time
import traceback

logger = logging.getLogger("timeUtils")


def get_now():
    return datetime.datetime.now()

def get_today():
    """
    return date
    :return:
    """
    return datetime.date.today()

def is_time_type(input_date):
    """
    判定是否是日期类
    :param input_date:
    :return:
    """
    return isinstance(input_date, datetime.date) or isinstance(input_date, datetime.datetime)

def get_max_date():
    return datetime.datetime.max

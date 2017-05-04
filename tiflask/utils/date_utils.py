# -*- coding:utf-8 -*-
__author__ = 'clarkchen'
import datetime
import logging

logger = logging.getLogger("date_utils")


def convert_str_to_time(time_str):
    if time_str.find("CST") != -1:
        try:
            # demo 'Sun Apr 12 16:09:00 CST 2015'
            format_time = "%a %b %d %H:%M:%S CST %Y"
            trans_time = datetime.datetime.strptime(time_str, format_time)
            return trans_time
        except Exception as e:
            logger.exception(e)
            return None
    elif time_str.find("UTC") != -1:
        try:
            # demo 'Sun Apr 12 16:09:00 CST 2015'
            format_time = "%a %b %d %H:%M:%S UTC %Y"
            trans_time = datetime.datetime.strptime(time_str, format_time)
            return trans_time
        except Exception as e:
            logger.exception(e)
            return None
    elif time_str.find(' ') != -1 and len(time_str) > 10:
        try:
            trans_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            return trans_time
        except Exception as e:
            logger.exception(e)
            return None
    else:
        try:
            trans_time = datetime.datetime.strptime(time_str, "%Y-%m-%d")
            return trans_time
        except Exception as e:
            logger.exception(e)
            return None


def convert_time_to_date_str(time_obj, format="%Y-%m-%d"):
    """
    :param time_obj: datetime 类型的变量, 精确到日
    :return:
    """
    return time_obj.strftime(format)


def convert_time_to_time_str(time_obj, format="%Y-%m-%d %H:%M:%S"):
    """
    :param time_obj: datetime 类型的变量，精确到分钟
    :return:
    """
    return time_obj.strftime(format)

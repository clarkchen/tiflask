# -*- coding:utf-8 -*-
from flask import jsonify

from tiflask.config import server_config
from tiflask.utils import is_blank, get_now, convert_time_to_time_str

__author__ = 'clarkchen'


def return_value(controller_fun):
    """
    返回参数
    :param controller_fun:  控制层函数
    :return:
    """
    def __decorator(*args, **kwargs):
        ret_value = {
            "version": server_config.version,
            "success": 0,
            "message": u"fail query"
        }
        ret_data, code = controller_fun(*args, **kwargs)

        if is_blank(ret_data):
            ret_value["data"] = {}
        else:
            ret_value["success"] = 1
            ret_value["message"] = u"succ query"
            ret_value["data"] = ret_data
            ret_value["update_time"] = convert_time_to_time_str(get_now())
        return ret_value, code
    return __decorator
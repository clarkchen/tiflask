# -*- coding: utf-8 -*-
'''
Created on 27 Jan 2015
@version: 1.0
@author: chenxi
'''
import logging
import os
import sys
import sys


from .checker import is_blank, is_str
from .file_utils import read_json_from_file, project_dir

logger = logging.getLogger("locationUtil")
input_json = "{0}/utils/location_data/city_province_info.json".format(project_dir)
city_province_dict = read_json_from_file(input_json)
# encode_to_utf8(city_province_dict)

provinces = set(['北京', '天津', '重庆', '上海', '河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北',
                 '湖南', '广东', '海南', '四川', '贵州', '云南', '陕西', '甘肃', '青海', '台湾', '内蒙古', '广西', '西藏', '宁夏', '新疆', '香港', '澳门'])


def get_city_from_add_dict(addr_dict):
    """
    :param addr_dict: 处理过的地理位置的dict
    :return:
    """
    if not isinstance(addr_dict, dict): return None
    if is_zhixia(addr_dict.get("province")):
        return addr_dict.get("province")
    return addr_dict.get("city")


def is_address_dict_equal(add_dict1, add_dict2):
    one_prov = add_dict1.get('province')
    one_city = add_dict1.get('city')
    if one_prov == add_dict2.get("province") and one_city == add_dict2.get("city"):
        return True

    if is_zhixia(one_prov) and one_prov == add_dict2.get("province"):
        return True

    return False


def is_zhixia(addr):
    if not is_str(addr): return False
    provinces = ['北京', '天津', '重庆', '上海']
    for x in provinces:
        if x in addr:
            return True
    return False


def math_province(addr):
    for x in provinces:
        if x in addr:
            return x
    return None


def math_city(addr):
    ret = dict()
    possible_dict = dict()
    for city_key, value in city_province_dict.items():
        if city_key not in addr or len(city_key) <= len('汉'): continue
        if isinstance(value, tuple) or isinstance(value, list):
            province = value[0]
            city = value[1]
        elif isinstance(value, str):
            province = value
            city = city_key
        value = {"province": province, "city": city}
        possible_dict[city_key] = value
        break

    min_index = len(addr)
    # 可能有多重地名，比如坑爹的O2O
    # 中国,合肥市,庐阳区,徽州大道,
    for city_key, value in possible_dict.items():
        if min_index > addr.find(city_key):
            ret = value
            min_index = addr.find(city_key)

    return ret


def clear_address(address):
    """
    将地址信息中的 省，自治区，市 这样的词去掉，而且只保留到地级市
    :param address:
    :return:
    """
    province = "未知"
    city = "未知"
    if is_blank(address):
        return {}

    if not isinstance(address, str):
        return {"province": province, "city": city}

    provice_title = ["省", "自治区"]
    city_title = ["市", "区", "盟", "地区", "县", "乡", "镇", "村", " "]

    ret = address
    for x in provice_title:
        if x in ret:
            ret = ret.replace(x, ",")

    for x in city_title:
        if x in ret:
            ret = ret.replace(x, ",")

    if ',' not in ret or len(ret.split(',')) < 3:
        province = math_province(ret)
        if province is not None:
            ret = ret.replace(province, province + ",")
        if len(ret.split(',')) < 2:
            return math_city(ret)

    if "," in ret:
        res = ret.split(',')
        i = 0
        while i < len(res):
            if res[i] == "":
                i += 1
                continue
            province = res[i]
            if province not in provinces:
                province = math_province(province)
            i += 1
            break

        while i < len(res):
            if res[i] == "":
                i += 1
                continue
            city = res[i]
            i += 1
            break

    return {"province": province, "city": city}



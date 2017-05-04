# -*- coding:utf-8 -*-
import json

__author__ = 'clarkchen'


def read_lines(fpath):
    f = open(fpath, 'r')
    rt = f.readlines()
    f.close()
    return rt


def read_from_file(fpath):
    f = open(fpath, 'r')
    rt = f.read()
    f.close()
    return rt


def read_json_from_file(fpath):
    content = read_from_file(fpath)
    return json.loads(content)


def write_to_file(fpath, content):
    f = open(fpath, 'w')
    f.write(content)
    f.close()


import os

project_dir = os.path.dirname(os.path.abspath(__file__)) + "/.."
project_dir = os.path.normpath(project_dir)
project_name = os.path.basename(project_dir)


def get_data_output_file(module_path):
    """
    :param module_path: 文件中的Module的路径
    :return: data 文件夹中对应的生成路径
    """
    if project_dir not in module_path:
        return module_path
    start = module_path.index(project_name) + len(project_name)
    return module_path[:start] + "/data" + module_path[start:]

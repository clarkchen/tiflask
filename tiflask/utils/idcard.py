# -*- coding:utf-8 -*-
__author__ = 'clarkchen'
import datetime


def get_age(id):
    this_year = datetime.datetime.now().year
    if len(id) == 18:
        return this_year - int(id[6:6+4])+1
    elif len(id) == 15:
        return this_year - (1900 + int(id[7:7+2]))


def get_male(id):
    if len(id) == 18:
        sig = int (id[-2])
        return '男' if sig % 2 == 1 else '女'
    elif len(id)==15:
        sig = int(id[-1])
        return '男' if sig % 2 == 1 else '女'

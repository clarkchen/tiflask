# -*- coding:utf-8 -*-
__author__ = 'clarkchen'


def is_blank(value):
    """
    判断各种类型的变量是否为 空变量
    :param value:
    :return:
    """
    if not value:
        return True
    if type(value) == bytes and (value.strip() is '' or value == "None" or value == "null"):
        return True
    if type(value) == str and (value.strip() is u'' or value == u"None" or value == u"null"):
        return True
    if type(value) == list and len(value) == 0:
        return True
    if type(value) == dict and len(value) == 0:
        return True

    return False


def is_str(value):
    return isinstance(value, str) or isinstance(value, bytes)


if __name__ == '__main__':
    print(is_blank(""))
    print(is_blank(u""))

# -*- coding:utf-8 -*-
__author__ = 'clarkchen'


def show_getter_setter_method(input_object):
    """
    批量输出某一类别下的Getter 和 Setter 方法
    :param input_object:
    :return:
    """
    template = '''
@property
def {key}(self):
    return self._{key}

@{key}.setter
def {key}(self, value):
    self._{key} = value
'''
    ret = []
    for key in input_object.__dict__:
        if "logger" in key: continue
        input_key = key
        if "_" == key[0]:
            input_key = key[1:]

        ret.append( template.format(key=input_key))
    return  "\n".join(ret)



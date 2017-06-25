# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2017-06-24 23:05:10
# @Last Modified by:   Marte
# @Last Modified time: 2017-06-25 00:31:58
#
# 只要创建对象就调用
class Dog(object):
    def __new__(self):
        print('1111')
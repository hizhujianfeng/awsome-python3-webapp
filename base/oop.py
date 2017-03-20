#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from types import MethodType


class Student(object):
    pass


s = Student()
s.name = 'Nice'  # 动态给实例一个属性
print("s.name = "+s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)
print("s.age = "+str(s.age))


# 给实例绑定的方法，对于另外一个实例不起作用
s2 = Student()
# s2.set_age(22)  # 报错





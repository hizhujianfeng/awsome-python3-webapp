#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    # __slots__变量，来限制该class实例能添加的属性
    __slots__ = ('name', 'age', 'score')  # tuple定义允许绑定的属性名称


s = Student()
s.name = 'mack'
s.age = 23
s.score = 99


# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 999

print(g.score)
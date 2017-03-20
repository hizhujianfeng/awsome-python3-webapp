#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    # 添加必须绑定的属性
    def __init__(self):
        self._score = None
        self._birth = None

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


s = Student()
s.birth = 1990
print(s.age)

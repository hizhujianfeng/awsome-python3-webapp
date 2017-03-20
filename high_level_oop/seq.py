#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
序列化
Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。
"""
import pickle
import json


# d = dict(name='Bob', age=20, score=88)
# print(d)
# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()

f = open('dump.txt', 'rb')
# load() 和 loads() 区别
# e = pickle.load(f)
# f.close()
#
# print(e)

#
# d = dict(name='Bob', age=20, score=88)
# # dump() 返回file-like Object  ，  dumps()方法返回一个str
# json_str = json.dumps(d)
#
# print(json_str)
#
# new_d = json.loads(json_str)
# print(d)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def print_student(self):
        print('name=%s' % self.name)


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score,
    }


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

s = Student('Bob', 22, 100)
# 对象  序列化为 JSON
json_str = json.dumps(s, default=student2dict)
print('序列化：'+json_str)
# JSON 序列化为 对象

print('反序列化：')
print(json.loads(json_str, object_hook=dict2student))

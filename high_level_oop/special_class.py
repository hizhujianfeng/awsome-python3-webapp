#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""定制类

Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类
__str__, __iter__, __getitem__, __getattr__, __call__
"""


# __str__ 默认打印类的字符串
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object(name: %s)' % self.name

    __repr__ = __str__

    def __getattr__(self, item):
        if item == 'score':
            return 99
        if item == 'age':
            return lambda: 22
        raise AttributeError('\Student\' object has no attribute \'%s\'' % item)

    def __call__(self):
        print('My name is %s' % self.name)

s = Student('Mack')
# s()
print(callable(max))
print(callable(Student('Jack')))


# __iter__ 让类变得可迭代 iterable
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a+self.b  # 计算下一个值
        if self.a > 10000:  # 退出循环的值
            raise StopIteration
        return self.a  # 返回下一个值

    def __getitem__(self, item):

            if isinstance(item, int):  # item是索引
                a, b = 1, 1
                for x in range(item):
                    a, b = b, a + b
                return a

            if isinstance(item, slice):  # 是切片
                start = item.start
                stop = item.stop
                if start is None:
                    start = 0
                a, b = 1, 1
                ll = []
                for x in range(stop):
                    if x >= start:
                        ll.append(a)
                    a, b = b, a + b
                return ll


# for n in Fib():
#     print(n)

# f = Fib()
# print(f[5:10:2])

# s = Student('jack')
# print(s.score)
# print(s.age())
# print(s.abc)


# 完全动态的情况作调用 GET /users/:user/repos
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        if path == 'users':
            return lambda user: Chain('%s/users/%s' % (self._path, user))
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().users('michael').repos)









#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from functools import reduce
import functools


# 自定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 空函数，占位
def nop():
    pass


# X*Y
def multiply(x, y):
    return x*y


# 测试函数返回值为'truple'
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# x的n次幂
def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


# 默认参数
def enroll(name, gender='男', city='兰州'):
    print("name:"+name)
    print("gender:" + gender)
    print("city:" + city)
    return


# 默认参数必须指向不变对象
def add_end(l=None):
    if l is None:
        l = []
    l.append("END")
    print(l)
    return l


# 可变参数 a的平方+b的平方  list or truple
def calc(*numbers):
    sums = 0
    for n in numbers:
        sums = sums + n * n
    return sums


# 关键字参数 dict
def person(name, age, **kw):
    print('start----name:', name, 'age:', age, 'others:', kw)
    kw.clear()
    print('end----name:', name, 'age:', age, 'others:', kw)


# 命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)


# 参数组合
def f1(a, b, c=0, *args, **kwargs):
    print('a=', a, 'b=', b, 'c=', c, 'args =', args, 'kwargs =', kwargs)


def f(a, b, c=0, *, d, **kwargs):
    print('a=', a, 'b=', b, 'c=', c, 'd =', d, 'kwargs =', kwargs)


# 递归函数
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


# Fibonacci
def fib(max_num):
    n, a, b = 0, 0, 1
    while n < max_num:
        # print(b)
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


# 高阶函数
def higher_func(x, y, f):
    return f(x) + f(y)


# map/reduce
def f2(x):
    return x * x


# reduce
def add(x, y):
    return x + y


def fn(x, y):
    return x * 10 + y


# def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2int(out_str):
    def fnx(x, y):
        return x * 10 + y

    def char2num2(in_str):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[in_str]

    return reduce(fnx, map(char2num2, out_str))


# def str2int2(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def normalize(name):
    name = name[0].upper() + name.lower()[1:len(name)]
    return name


def prod(l):
    return reduce(lambda x, y: x * y, l)


def str2float(s):
    dot_position = s.find('.')
    divisor = len(s) - dot_position - 1
    s = s.replace('.', '')

    def char2num(n):
        result = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[n]
        return result

    return reduce(lambda x, y: x * 10 + y, map(char2num, s)) / math.pow(10, divisor)


def is_odd(n):
    return n % 2 == 1


def not_empty(s):
    return s and s.strip()


def odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 回数，所有 反向切割
def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return n


# 返回函数
def lazy_sum(*args):
    def sum_test():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum_test


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


def log1(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper

#
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
#
# @log('execute')
# def now():
#     print('2016-12-12')
#
#
# @log1
# def now1():
#     print('2016-12-12')
#
#
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('test')
def now():
    print('2016-12-12')












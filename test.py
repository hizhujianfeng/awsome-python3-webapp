#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base.my_lib import *

# from collections import Iterator
# print ("hello,world")

# 多个字符串
# print('hello','world','!')
# print(100)
# print(100-50)
# name = input()
# print(name)
# print('请输入你的姓名：')
# name = input()
# print('您的姓名是',name)

# 缩进为四个空格
# a = 100
# if a > 100:
#     print(a)
# else:
#     print(-a)
#


# print(r'I\'m  \\ \"ok\"....')
#
# print(R'''line1
# line2
# line3''')

# a = 1
# b =a 
# a='abc'
# print(b)
# print(10/3)
# print(10//3)
# print(10%3)


#
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
#
# print(s3)
# print(s4)

# print('中文haha')
# print(ord('朱'))
# print(chr(26417))
#
#
# print('你好'.encode('utf-8'))
#
# print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf-8'))
#
# x = len(b'\xe4\xbd\xa0\xe5\xa5\xbd')
# y = len('你好')
#
# print(x)
# print(y)


# str = 'Hi, %d, you have $%.2f.' % (22, 3.021547)
# print(str)

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])

# list =['a','b','c']
# list.append('d')
# list.insert(4,'e')
# list.pop(0)
# list[0]='f'
# print(list)
# print(len(list))

# tuple=('abc','edf','jkl')
# tuple[1]
# print(tuple[1])


# age = 18
# if age >= 20:
#     print(age)
# elif age > 0 and age < 2    0:
#     print('You are too young!')


# height = 1.75
# weight = 80.5
# bmi = 80.5/(1.75*1.75);
# print(bmi);
# if bmi <= 18.5:
#     print('太瘦了')
# elif bmi <=25:
#     print('正常')
# elif bmi <= 28:
#     print('过重')
# elif bmi <= 25:
#     print('肥胖')
# elif bmi <= 32:
#     print('正常')
# else:
#     print('严重肥胖')

# list = range(101);
# sum = 0
# for x in list:
#     sum = sum+x
# print(sum)


# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 1
# print(sum)

# dictionary
# map key-value
# d = {'mary': 90, 'john': 90, 'bob': 90}
# print(d['mary'])
# d['sara'] = 100
# print(d)
#
# if 'mary' in d:
#     print(d['mary'])
#
# print(d.get('bob'))
# d.pop('bob')
# print(d.get('bob'))


# 函数

# print(abs(-10))
# print(max(1, 2, 3))
# print(int('2222'))
# print(float('2222'))
# print(str(123))
#
#
# a = max
# print(a(1, 2, 3))
#
# print(hex(123))


# print(my_abs(10))
# print(multiply(10,10))
# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)
#
# print(power(2, 3))
# print(power(2))

# 默认参数
# enroll('朱剑锋','男');
# enroll('朱剑锋','男','平凉')
#
# enroll('朱剑锋',city='庄浪')
# enroll('朱剑锋','男')

# add_end()
# add_end()


# nums = (1, 2, 3)
# numList = [1, 1, 1]
# calc(*nums)
# calc(*numList)
# kw = {'gender': '男', 'address': '兰州'}
# person('朱剑锋', 25, **kw)
# print(kw)

# person('jack', 24, city='lanzhou', job='softEngineer')
# def f1(a, b, c=0, *args, **kwargs):
# def f2(a, b, c=0, *, d, **kwargs):

# f1(1, 2)
# f1(1, 2, c=3)
# f1(1, 2, 3, 4, 5)
# f1(1, 2, 3, 4, 5, name='mary')
#
#
# f2(1, 2, d=99, ext=None)

# 默认参数、可变参数、关键字参数、命名关键字参数
# args = (1, 2, 3, 4)
# kwargs = {'d': 99, 'x': '#'}
# f1(*args, **kwargs)
#
#
# args = (1, 2, 3)
# kwargs = {'d': 99, 'x': '#'}
# f2(*args, **kwargs)


# 递归函数
# print(fact(100))

# l = []
# n = 1
# while n < 101:
#     l.append(n)
#     n += 1
#
# print(l)

# 切片 、截取
# L = list(range(100))
# print(L[0:3])
# print(L[:3])
# print(L[-10:])
#
# print(L[0:10:2])
# print(L[::10])
# print(L[::])
#
# print((1, 2, 3, 4, 5, 6, 7, 8)[:3])
#
# print('x123456'[:3])


# 迭代


# from collections import Iterable
#
# if isinstance((1, 3), Iterable):
#     print('true')
#
# else:
#     print('false')


# x = (1, 2, 3)
# y = [1, 2, 3]
# z = {'name': 'mary', 'age': 24}
#
# for n in y:
#     print(n)
#
# for key in z:
#     print(key)
#
# for value in z.values():
#     print(value)
#
# for key, value in z.items():
#     print(key, ':', value)
#
# for index, value in enumerate(y):
#     print(index, '-', value)

# 列表生成式
# L = []
# for x in range(1, 11):
#     L.append(x*x)
# print(L)
#
# L = [x * x for x in range(1, 11)]
# print(L)
#
#
# L = [x * x for x in range(1, 11) if x % 2 == 0]
# print(L)
#
#
# L = [m + n for m in 'ABC' for n in '123']
# print(L)
#
#
# L = [d for d in os.listdir('.')]
# print(L)


# d = {'x': 'A', 'y': 'B', 'z': 'C', 'w': 'D'}
# L = [k+'='+v for k, v in d.items()]
# print(L)
#
# L = ['Hello', 'World', 'IBM', 'Apple']
# x = []
# [x.append(s.lower()) for s in L]
#
# print(x)
#
#
# print(isinstance('123', str))


# g = (x * x for x in range(10))
# for n in g:
#     print(n)
# print(next(g))

# f = fib(6)
# print(next(f))


# print(isinstance(iter([]), Iterator))
# print(isinstance(iter('abc'), Iterator))
#
# for x in [2, 3, 4, 5]:
#     pass


# x = higher_func(1, -1, abs)
# print(x)


m = map(f, [1, 2, 3])
# print(m)
# print(list(m))

# r = reduce(add, [1, 2, 3])
# print(r)
#
# rr = reduce(fn, [2, 4, 6])
# print(rr)


# reduce(fn, map(char2num, '13579'))


str_int = str2int('234')

# print(str_int)


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
# print(L2)


# print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))
# print(list(filter(not_empty,  ['A', '', 'B', None, 'C', '  '])))


odd = odd_iter()
# print(next(odd))
# print(next(odd))
# print(next(odd))
# print(next(odd))
# print(next(odd))


# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break


# output = filter(is_palindrome, range(1, 1000))
# print(list(output))
#
#
# dictionary = {'A': 1, 'B': 2}
# print(dictionary['B'])


# print(sorted([36, 5, -12, 9, -21]), abs)
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# f = lazy_sum(1, 2, 3, 4)
# f1 = lazy_sum(1, 2, 3, 4)
# f2 = lazy_sum(1, 2, 3, 4)
# print(f1 == f2)


# y = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(y)


# print(now.__name__)
#
#
# int2 = functools.partial(int, base=2)
# print(int2('1000000'))
#
#
# base.test()
# print(base)



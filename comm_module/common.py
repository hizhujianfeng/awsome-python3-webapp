#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
常用内建模块

"""
from datetime import datetime, timedelta, timezone
# 获取当前日期和时间
now = datetime.now()
print(now)
print(type(now))

dt = datetime(2017, 5, 12, 15, 4, 33 )
print(dt)
# 小数位为毫秒数
tt = dt.timestamp()
print(tt)

# 字符串格式为日期
cday = datetime.strptime('2017-05-12 15:53:01', '%Y-%m-%d %H:%M:%S')
print(cday)

# 日期转换为字符串
now = datetime.now()
print(now.strftime('%Y-%m-%d'))

#  日期加减法 timedelta
print(now + timedelta(hours=1))
print(now - timedelta(minutes=10))

#
print(datetime.tzinfo)
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。


from collections import namedtuple, deque, defaultdict, OrderedDict, Counter
# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)

# deque 实现插入和删除操作的双向列表，适合用于队列和栈
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
q.popleft()
print(q)

# defaultdict key不存在时，返回一个默认值，就可以用defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])


# OrderedDict Key会按照插入的顺序

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)


# class LastUpdatedOrderedDict(OrderedDict):
#
#     def __init__(self, capacity):
#         super(LastUpdatedOrderedDict, self).__init__()
#         self._capacity = capacity
#
#     def __setitem__(self, key, value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False)
#             print('remove:', last)
#         if containsKey:
#             del self[key]
#             print('set:', (key, value))
#         else:
#             print('add', (key, value))
#         OrderedDict.__setitem__(self, key, value)


# counter 统计字符出现的个数

c = Counter()
for ch in 'programming':
    c[ch] += 1

print(c)


# import  base64
# # base64
#
# print(base64.b64encode(b'\x00'))
import struct
print(struct.pack('>I', 10240099))


import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

import  itertools
# 迭代
natuals = itertools.count(1)
# natuals = itertools.cycle('ABC')
# natuals = itertools.repeat('a', 3)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

for c in itertools.chain('abc', 'XYZ'):
    print(c)

for key, group in itertools.groupby('AAABBBBCCAAA'):
    print(key, list(group))
print('----------------------')
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))


# contextlib
# xml

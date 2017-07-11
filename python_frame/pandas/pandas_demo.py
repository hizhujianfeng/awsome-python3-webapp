# -*- coding:utf-8 -*-
"""
pandas series DataFrame

"""
import pandas as pd
import numpy as np

# n = pd.Series(np.arange(10))
# print(n)

b = pd.Series([9, 8, 7, 6], ['a', 'b', 'c', 'd'])
a = pd.Series([1, 2, 3], ['c', 'd', 'e'])
# print(b.index)
# print(b['a'])
# print(b[0])
# print(b[:3])
# print(b[b > b.median()])
# print(np.exp(b))
# print(0 in b)
# print(b.get('d', 100))
# 自动对齐不同索引
# print(a + b)
# b.name = 'Series 对象'
# b.index.name = '索引列'
# print(b.name)
# print(b.index.name)
# print(b)
# b['b', 'c'] = 20
# print(b)

# 二维 ndarray ,一维ndarray和Series, 列表类型，


# d = pd.DataFrame(np.arange(10).reshape(2, 5))
# print(d)

# dt = {
#     'one': pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd']),
#     'two': pd.Series([1, 2, 3], ['c', 'd', 'e'])
# }
#
# d = pd.DataFrame(dt)
# print(d)

# dl = {
#     'one': [9, 8, 7, 6],
#     'two': [1, 2, 3, 4]
# }
# d = pd.DataFrame(dl, index=['a', 'b', 'c', 'd'])
#
# print(d)

# print(d.ix['c'])
# d = d.reindex(index=['d', 'c', 'b', 'a'])
# print(d)
#
# d = d.reindex(columns=['two', 'one'])
# print(d)

# nc = d.columns.delete(1)
# ni = d.index.insert(2, 'x')
# nd = d.reindex(index=ni, columns=nc, method='ffill')
# print(nd)

# print(d.drop(['a', 'b']))

# a = pd.DataFrame(np.arange(12).reshape(3, 4))
# b = pd.DataFrame(np.arange(20).reshape(4, 5))
#
# print(b.add(a, fill_value=100000))

b = pd.DataFrame(np.arange(20).reshape(4, 5), index=['c', 'a', 'd', 'b'])
c = b.sort_values('d', axis=1, ascending=False)
print(b)
# print(c)

print(b.sum())
# print(b.describe().ix['max'])
print(b.cumsum())
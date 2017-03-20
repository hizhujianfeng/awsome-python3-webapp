#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 调试
print()
assert 断言
logging  VIP
pdb
IDE debug模式

"""
import logging
logging.basicConfig(level=logging.INFO)


# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
#
#
# def main():
#     foo('10')
#
#
# main()


s = '1'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

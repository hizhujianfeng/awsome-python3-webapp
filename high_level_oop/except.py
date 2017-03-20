#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 错误处理
try ... except ... finally ...

"""
import logging


try:
    print('try...')
    r = 10 / int('10')
    print('result is ', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    logging.exception(e)
    # print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('Finally...')
print('END')


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value:%s' %s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError:', e)
        raise

bar()
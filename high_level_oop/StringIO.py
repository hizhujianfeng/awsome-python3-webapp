#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import StringIO
from io import BytesIO
import os
print(os.name)
print(os.environ)
print(os.path.abspath('/'))


# os.makedirs('E://test')
# os.rmdir('E://test')
# os.remove('E://test.txt')
# print(os.path.splitext('E://test.txt'))
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

# print(f.getvalue())

y = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

print(y)

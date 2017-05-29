#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

socket 客户端
"""
import socket

# SOCK_STREAM 表示简历的是TCP连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()

# buffer = []
# while True:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
#
# data = b''.join(buffer)
#
# s.close()
#
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# with open('sina.html', 'wb') as f:
#     f.write(html)



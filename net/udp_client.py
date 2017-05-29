#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
udp 客户端
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'1', b'2', b'3']:
    s.sendto(data, ('127.0.0.1', 9999))
    print(s.recv(1024).decode('utf-8'))

s.close()

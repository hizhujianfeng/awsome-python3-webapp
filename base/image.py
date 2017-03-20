#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image


im = Image.open('Img791369_f.jpg')

print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('test.jpg', 'JPEG')
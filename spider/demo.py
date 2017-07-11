#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


url = "http://www.baidu.com"
r = requests.get(url)
r.encoding = r.apparent_encoding

soaup = BeautifulSoup(r.text,  'html.parser')
html = soaup.find('form')


# print(soaup.prettify())
for x in html.contents:
    print(x)


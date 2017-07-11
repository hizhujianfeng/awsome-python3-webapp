#!/usr/bin/env python
# -*- coding: utf-8 -*-\
"""
最好大学排名
"""

import requests
from bs4 import BeautifulSoup
import bs4


def getHtmlText(url):
    try:
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        html = r.text
    except requests.HTTPError:
        return ''
    return html


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])


def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    tt = "{0:^10}\t{1:^10}\t{2:^10}"
    print(tt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))
    print("Suc " + str(num))


def main():
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = getHtmlText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)


main()




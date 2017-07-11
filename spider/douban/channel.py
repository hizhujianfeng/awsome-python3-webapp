# -*- coding:utf-8 -*-
"""
豆瓣图书爬虫
"""

import requests
from bs4 import BeautifulSoup       #导入库

channel = ''
url = "https://book.douban.com/tag/?icn=index-nav"
wb_data = requests.get(url)                #请求网址
soup = BeautifulSoup(wb_data.text, "lxml")  #解析网页信息
tags = soup.select("#content > div > div.article > div > div > table > tbody > tr > td > a")
     # 根据CSS路径查找标签信息，CSS路径获取方法，右键-检查-copy selector，tags返回的是一个列表
for tag in tags:
       tag=tag.get_text()    #将列表中的每一个标签信息提取出来
       helf="https://book.douban.com/tag/"
          #观察一下豆瓣的网址，基本都是这部分加上标签信息，所以我们要组装网址，用于爬取标签详情页
       url=helf+str(tag)
       channel += url+"\r\n"

print(channel)    #网址组装完毕，输出

#!/usr/bin/env python
# -*- coding:utf-8 -*-
from lxml import etree


parser = etree.HTMLParser(encoding='utf-8')
htmlElement = etree.parse("选电影.html", parser=parser)
# print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))

# 1.获取所有div标签
# xpath返回列表
# trs = htmlElement.xpath("//div")
# for tr in trs:
#  print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))

# 2.获取第2个div标签
# tr = htmlElement.xpath("//div[2]")[0]
# print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))

# 3.获取所有class等于item的a标签
# trs = htmlElement.xpath("//a[@class='item']")
# for tr in trs:
#  print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))

# 4.获取所有a标签的href属性
# aList = htmlElement.xpath("//a/@href")
# for a in aList:
#     print(a)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
from lxml import etree
from bs4 import BeautifulSoup

parser = etree.HTMLParser(encoding='utf-8')
htmlElement = etree.parse("选电影.html", parser=parser)
# print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))

# ==========================  lxml =============================================
# 1.获取所有div标签
# xpath返回列表
# divs = htmlElement.xpath("//div")
# for div in divs:
#  print(etree.tostring(div, encoding='utf-8').decode('utf-8'))

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

# 5.获取title标签的纯文本信息
# titleList = htmlElement.xpath("//title//text()")[0]
# print(titleList)

# ==========================  BeautifulStoneSoup =============================================
html = open('选电影.html')
soup = BeautifulSoup(html, "lxml")

# 1.获取所有meta标签
# metas = soup.find_all('meta')
# for meta in metas:
#     print(meta)

# 2.获取第2个div标签
# div = soup.find_all('meta', limit=2)[1]
# print(div)

# 3.获取所有class等于item的a标签
# aList = soup.find_all('a', class_='item')
#  或者
# aList = soup.find_all('a', attrs={'class': "item"})
# for a in aList:
#     print(a)

# 4.获取所有id等于top-nav-appintro class等于more-items的div标签
# divs = soup.find_all('div', id='top-nav-appintro', class_='more-items')
#  或者
# divs = soup.find_all('div',attrs={'id': 'top-nav-appintro', 'class': 'more-items'})
# for div in divs:
#     print(div)

# 5.获取所有a标签下的href属性
# aList = soup.find_all('a')
# for a in aList:
#     href = a.attrs['href']
#     print(href)

# 6. 获取所有class等于item的a标签中的文字
# aList = soup.find_all('a', class_='item')
# for a in aList:
#     infos = list(a.stripped_strings)
#     print(infos)

# 1.获取所有meta标签
# metas = soup.select('meta')
# for meta in metas:
#     print(meta)

# 2.获取第2个meta标签
# meta = soup.select('meta')[1]
# print(meta)

# 3.获取所有class等于item的a标签
# aList = soup.select('a.item')
# for a in aList:
#     print(a)

# 4.获取所有id等于top-nav-appintro class等于more-items的div标签
# 在css选择器中无法实现

# 5.获取所有a标签下的href属性
# aList = soup.select('a')
# for a in aList:
#     href = a.attrs['href']
#     print(href)


# 6. 获取所有title中的文字
titleList = soup.select('title', class_='item')
for title in titleList:
    infos = list(title.stripped_strings)
    print(infos)


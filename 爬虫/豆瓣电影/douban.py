#!/usr/bin/env python
# -*- coding:utf-8 -*-
from lxml import etree


parser = etree.HTMLParser(encoding='utf-8')
htmlElement = etree.parse("选电影.html", parser=parser)
# print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))


divElement = htmlElement.xpath("//div[@class='list']")[0]   # 所有电影节点数组
aElement = divElement.xpath("./a")
movies = []
for a in aElement:
    # print(etree.tostring(a, encoding='utf-8').decode('utf-8'))
    # 链接
    url = a.xpath('@href')[0]
    # print(url)
    # 片名
    name = a.xpath('.//img/@alt')[0]
    # 评价分数
    pElement = a.xpath('./p')[0]
    score = pElement.xpath('./strong//text()')[0]
    # print(score)
    movie = {
        'name': name,
        'url': url,
        'score': score
    }
    movies.append(movie)

print('爬取结果是：')
print(movies)

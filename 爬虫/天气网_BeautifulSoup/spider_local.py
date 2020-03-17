#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from pyecharts.charts import Bar
ALL_DATA = []


def parse_page(url):
    html = open(url)
    soup = BeautifulSoup(html, "html5lib")
    conMidtab = soup.find('div', class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({"city": city, "min_temp": int(min_temp)})
            # print({"city": city, "min_temp": min_temp})


def main():
    urls = [
        '华北地区天气预报.html',
        '东北地区天气预报.html',
        '华东地区天气预报.html',
        '华中地区天气预报.html',
        '华南地区天气预报.html',
        '西北地区天气预报.html',
        '西南地区天气预报.html',
        '港澳台地区天气预报.html',
    ]
    for url in urls:
        parse_page(url)
    # 分析数据
    # 根据最低气温进行排序
    ALL_DATA.sort(key=lambda data: data['min_temp'])
    # print(ALL_DATA)
    data = ALL_DATA[0:10]

    cities = map(lambda x: x['city'], data)
    min_temp = map(lambda x: x['min_temp'], data)

    bar = Bar()
    bar.add_xaxis(list(cities))
    bar.add_yaxis("今日中国最低温度", list(min_temp))
    bar.render("mycharts_local.html")


if __name__ == '__main__':
   main()

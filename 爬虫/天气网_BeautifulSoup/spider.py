#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Bar
from lxml import etree
ALL_DATA = []

def parse_page(url):
    headers = {
       'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text, 'html5lib')  # 港澳台数据缺少结束标签，使用html5lib解析器解析，容错性比lxml强
    conMidtab = soup.find('div', class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        # print(trs)
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            # print(tds)
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
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
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
    bar.render("mycharts.html")


if __name__ == '__main__':
   main()


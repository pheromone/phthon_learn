#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re


def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    response = requests.get(url, headers)
    text = response.text
    # print(text)
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    contents_tags = re.findall(r'<div class="contson" .*?>(.*?)</div>', text, re.DOTALL)
    contents = []
    for content in contents_tags:
        x = re.sub(r'<.*?>', "", content)
        contents.append(x.strip())

    poems = []
    for value in zip(titles, dynasties, authors, contents):
        title, dynasty, author, content = value
        poem = {
            'title': title,
            'dynasty': dynasty,
            'author': author,
            'content': content,
        }
        poems.append(poem)

    for poem in poems:
        print(poem)
        print('='*50)


def main():
    for x in range(1, 5):
        url = 'https://www.gushiwen.org/default.aspx?page=%s' % x
        parse_page(url)


if __name__ == '__main__':
    main()

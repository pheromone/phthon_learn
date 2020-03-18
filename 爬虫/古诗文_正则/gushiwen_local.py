#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup


def parse_page(url):
    html = open(url)
    text = html.read()
    titles = re.findall(r'<div class="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
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
        print('=' * 50)


def main():
    urls = [
        '古诗文网-古诗文经典传承1.html',
        '古诗文网-古诗文经典传承2.html',
        '古诗文网-古诗文经典传承3.html',
        '古诗文网-古诗文经典传承4.html',
        '古诗文网-古诗文经典传承5.html',
    ]
    for url in urls:
        parse_page(url)


if __name__ == '__main__':
    main()

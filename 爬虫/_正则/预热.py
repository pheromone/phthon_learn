#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

# 1. 匹配某个字符串
# text = 'hello'
# ret = re.match('he', text)  # he 匹配到 el 无法匹配到
# rett = re.search('el', text) # el 可以匹配到
# print(ret.group())

# 2. .(点) 匹配任意字符(不能匹配 \n等)
# text = '+hello'
# ret = re.match('.', text)
# print(ret.group())

# 3. \d 匹配任意的数字
# text = '520'
# ret = re.match('\d', text)
# print(ret.group())

# 4. \D 匹配任意的非数字
# text = '++'
# ret = re.match('\D', text)
# print(ret.group())

# 5. \s 匹配空白字符（\n \t \r 空格）
# text = ' '
# ret = re.match('\s', text)
# print(ret.group())

# 6. \w 匹配a~z A~Z 数字 下划线
# text = 'asd_1'
# ret = re.match('\w', text)
# print(ret.group())

# 6. \W 匹配与 \w相反
# text = '<+'
# ret = re.match('\W', text)
# print(ret.group())

# 7. []  组合
# text = 'a'
# ret = re.match('[a1]', text)
# print(text)

# +匹配多个字符 （1个或者多个）
# text = '0874-5621391'
# ret = re.match('[\d\-]+', text)
# print(ret.group())

# text = '5621391'
# ret = re.match('[0-9]+', text)
# print(ret.group())

# ^ 在[]中代表 非（取反）
# text = 'ABC'
# ret = re.match('[^0-9]+', text)
# print(ret.group())

# ^m 没在[]中代表 以m开始
# text = 'abc'
# ret = re.match('^ab', text)
# print(ret.group())

# text = 'ABC_123'
# ret = re.match('[a-zA-Z0-9_]+', text)
# print(ret.group())

# 8 \s 匹配空格
# text = ' '
# ret = re.match('\s', text)
# print(ret.group())

# 9 * 匹配多个字符（0个或者多个）
# text = '2345f'
# ret = re.match('\d*',text)
# print(ret.group())

# 10. ？ 匹配一个或者0个
# text = '12sd'
# ret = re.match('\w?',text)
# print(ret.group())

# 11. {m} 匹配m个字符
# text = 'abcdertyui'
# ret = re.match('\w{3}', text)
# print(ret.group())

# 12. {m,n} 匹配m到n个字符(取最大区间)
# text = 'qwerty'
# ret = re.match('\w{0,4}', text)
# print(ret.group())

# 13. $m 以m结尾
# text = 'xxx@163.com'
# ret = re.match('\w+@163.com$', text)
# print(ret.group())


# 13. | 或
# text = 'https'
# ret = re.match('ftp|http|https', text)
# print(ret.group())

# 14. 贪婪模式 非贪婪模式
# text = "<h1>标题<h1>"
# ret = re.match('<.+>', text)
# ret = re.match('<.+?>', text)
# print(ret.group())

# 15. 转义 \ 或者 r
# text ='\r'
# text = r'\r'
# print(text)

# find_all
# text = 'fuck you 3000 又 300'
# ret = re.findall('\d+', text)
# print(ret)

# sub
# text = 'fuck you 3000'
# ret = re.sub('\d', '9', text)
# print(ret)

# split
# text = 'hello00world'
# ret = re.split('\d+', text)
# print(ret)

# compile 提前编译
#
# text = 'the number is 20.89'
# r = re.compile('\d+\.?\d*')
# r = re.compile(r"""
#   \d+  # 小数点前面的数字
#   \.?   # 小数点本身
#   \d*  # 小数点后面的数字
# """, re.VERBOSE)
# ret = re.search(r, text)
# print(ret.group())






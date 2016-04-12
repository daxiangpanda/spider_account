#!/usr/bin/env python
# encoding: utf-8

# import urlfunc
import urllib
from bs4 import BeautifulSoup
zhilian_url = r'http://m.zhaopin.com/chengdu-801/?keyword=%E4%BC%9A%E8%AE%A1'

def find_last(url):
    html = urllib.urlopen(zhilian_url).read()
    soup = BeautifulSoup(html)
    print soup
    print soup.find_all('a',rel = 'nofollow')

find_last(zhilian_url)

# print urllib.urlopen(zhilian_url).read()
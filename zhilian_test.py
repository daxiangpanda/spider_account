#!/usr/bin/env python
# encoding: utf-8
# import urllib2
import urlfunc
import time
import random
base_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%88%90%E9%83%BD&kw=%E4%BC%9A%E8%AE%A1&sm=0&isfilter=0&fl=801&isadv=0&sg=e1b9f5c9a6c54d9f8fab2a38dece44aa&p='
start_page = 0
result = []

def process(soup):
    for i in soup.findall('table',cellpadding='0'):
        tag_info = i.find('tbody')


while True:
    print '正在爬取第{0}页'.format(start_page)
    soup = urlfunc.url_open(base_url+str(start_page))
    result.append(process(soup))
    start_page+=1
    time_sleep = random.random()*5
    print '爬的好累，我休息{0}秒'.format(time_sleep)
    time.sleep(time_sleep)

# def get_page_html(page): #读取指定某页源代码
#     html_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%AE%97%E6%B3%95%E5%B7%A5%E7%A8%8B%E5%B8%88&sm=0&p='+str(page)
#     html=urllib2.urlopen(html_url).read()
#     return html
# print get_page_html(1)
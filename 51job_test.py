#!/usr/bin/env python
# encoding: utf-8
import requests
import process_51job
# import re
# import json
from bs4 import BeautifulSoup
joblist_url = "http://search.51job.com/list/190200%252C00,000000,0000,00,9,99,%2B,0,{0}.html?"\
     "lang=c&stype=2&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&"\
     "lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&confirmdate=9&fromType=1&dibiaoid=0"



start_url = joblist_url.format(1)
print joblist_url
print start_url

cookies = dict(guide='1')
r = requests.get(start_url,cookies=cookies,)
r.encoding = 'gb2312'

soup = BeautifulSoup(r.text,"html.parser")
tag_pagenum = soup.find_all('span',class_ = 'td')[0].string
a = tag_pagenum.find(u'共')
b = tag_pagenum.find(u'页')
pagenum = tag_pagenum[a+1:b]


for i in range(1,int(pagenum)+1):
     r = requests.get(joblist_url.format(i),cookies=cookies,)
     r.encoding = 'gb2312'
     soup = BeautifulSoup(r.text)
     with open('51job_html\\'+str(i)+'.html','w') as f:
          f.write(str(soup))
     # print soup
     print process_51job.process(soup)
     with open('51job_pick\\'+str(i)+'.pick','w') as f:
          f.write(str(process_51job.process(soup)))
     print u'已爬取'+str(i)+u'个网页'
# print pagenum
# print soup.find_all('span',class_ = 'td')[0].string.find(u'共')
# print soup.find_all('span',class_ = 'td')[0].string.find(u'页')
# print (soup.find_all('span',class_ = 'td')[0].string)[1:5]
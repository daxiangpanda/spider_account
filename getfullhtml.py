#!/usr/bin/env python
# encoding: utf-8
import urlfunc
# baseurl = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%88%90%E9%83%BD&kw=%E4%BC%9A%E8%AE%A1&p='+page+'&isadv=0'
part1 = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%88%90%E9%83%BD&kw=%E4%BC%9A%E8%AE%A1&p='
part2 = '&isadv=0'

for i in range(1,55):
    html = urlfunc.url_open(part1+str(i)+part2)
    print len(str(html))
    with open(r'E:\\python\\scrapy\\ttmeiju_all\\spider_account\\fullhtml\\'+str(i)+'.html','w') as f:
        f.write(str(html))
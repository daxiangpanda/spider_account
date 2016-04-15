#!/usr/bin/env python
# encoding: utf-8
# import urllib2
import urlfunc
import time
import random
import urllib2
import cPickle as pickle
import socket
socket.setdefaulttimeout(10)


def process(soup):
    result = []
    num = 0
    # print soup.find_all('table',cellpadding='0')
    for i in soup.find_all('table',cellpadding='0'):
        if num==0:
            num+=1
            continue
        # print i
        # try:
        position = i.find('a',style = "font-weight: bold").get_text()


        position_link = i.find('a',style = 'font-weight: bold')['href']
        company = i.find('td',class_='gsmc').find('a').string
        company_link = i.find('td',class_='gsmc').find('a')['href']
        wage = i.find('td',class_='zwyx').string
        location = i.find('td',class_='gzdd').string
        result.append([position,position_link,company,company_link,wage,location])
    return result


def crawler(start_page):
    result = []
    while True:
        print '正在爬取第{0}页'.format(start_page)
        resoup = 0
        soup = urlfunc.url_open(base_url+str(start_page))
        if 'strong' in str(soup):
            print u'爬取完毕。'
            return result
        print len(str(soup))
        while True:
            if len(str(soup))<2000:
                resoup+=1
                soup = urlfunc.url_open(base_url+str(start_page))
                print u'长度不对啊，真是的'
                print str(resoup)
                            # print soup
                time.sleep(random.random())
            else:
                resoup=0
                break
                    # print soup
        with open('html\\'+str(start_page)+'.html','w') as f:
            f.write(str(soup))
        subres = process(soup)
        with open('pick\\'+str(start_page)+'.pick','w') as f:
            f.write(pickle.dumps(process(soup)))
        print subres
        result.append(subres)
        start_page+=1
        time_sleep = random.random()*1
        print '爬的好累，我休息{0}秒'.format(time_sleep)
        time.sleep(time_sleep)


if __name__ == '__main__':
    base_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%' \
               'E6%88%90%E9%83%BD&kw=%E4%BC%9A%E8%AE%A1&sm=0&isfilter' \
               '=0&fl=801&isadv=0&sg=e1b9f5c9a6c54d9f8fab2a38dece44aa&p='
    start_page = 1
    crawler(start_page)


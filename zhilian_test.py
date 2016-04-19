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
    for i in soup.find_all('table',cellpadding='0'):
        if num==0:
            num+=1
            continue
        sub_res = {}
        sub_res['position'] = i.find('a',style = "font-weight: bold").get_text()
        sub_res['position_link'] = i.find('a',style = 'font-weight: bold')['href']
        sub_res['company'] = i.find('td',class_='gsmc').find('a').string
        sub_res['company_link'] = i.find('td',class_='gsmc').find('a')['href']
        sub_res['wage'] = i.find('td',class_='zwyx').string
        sub_res['location'] = i.find('td',class_='gzdd').string
        result.append(sub_res)
    return result


def crawler(keyword,start_page):
    base_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%88%90%E9%83%BD&sm=0'

    result = []
    while True:
        print '正在爬取{0}行业的第{1}页'.format(keyword,start_page)
        resoup = 0
        url = base_url+'&kw='+urllib2.quote(keyword)+'&p='+str(start_page)
        soup = urlfunc.url_open(url)
        print url
        if '对不起，暂时无符合您条件的职位' in str(soup):
            print u'爬取完毕。'
            return result
        print len(str(soup))
        while True:
            if len(str(soup))<2000:
                resoup+=1
                soup = urlfunc.url_open(base_url+str(start_page))
                print u'长度不对啊，真是的'
                print str(resoup)
                time.sleep(random.random())
            else:
                resoup=0
                break
        with open('html/'+keyword.decode('utf-8')+str(start_page)+'.html','w') as f:
            f.write(str(soup))
        subres = process(soup)
        with open('pick/'+keyword.decode('utf-8')+str(start_page)+'.pick','w') as f:
            f.write(pickle.dumps(process(soup)))
        print subres
        result.append(subres)
        start_page+=1
        time_sleep = random.random()*1
        print '爬的好累，我休息{0}秒'.format(time_sleep)
        time.sleep(time_sleep)


if __name__ == '__main__':
    keyword = ['算法工程师','会计']
    start_page = [1]*len(keyword)
    map(crawler,keyword,start_page)

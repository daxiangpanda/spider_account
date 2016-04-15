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


def crawler(keyword,start_page):
    base_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%88%90%E9%83%BD&sm=0'

    result = []
    while True:
        print '正在爬取第{0}页'.format(start_page)
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
                            # print soup
                time.sleep(random.random())
            else:
                resoup=0
                break
                    # print soup
        with open('html\\'+keyword.decode('utf-8')+str(start_page)+'.html','w') as f:
            f.write(str(soup))
        subres = process(soup)
        with open('pick\\'+keyword.decode('utf-8')+str(start_page)+'.pick','w') as f:
            f.write(pickle.dumps(process(soup)))
        print subres
        result.append(subres)
        start_page+=1
        time_sleep = random.random()*1
        print '爬的好累，我休息{0}秒'.format(time_sleep)
        time.sleep(time_sleep)


if __name__ == '__main__':
    keyword = '算法工程师'
    start_page = 1
    crawler(keyword,start_page)


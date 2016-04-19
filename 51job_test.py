#!/usr/bin/env python
# encoding: utf-8
import requests
import process_51job
import urllib
from bs4 import BeautifulSoup
import cPickle as pickle
def crawler(keyword,start_page):
    joblist_url = "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=090200%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99" \
                  "&keyword={0}&keywordtype=0" \
                  "&curr_page={1}&lang=c&stype=2&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9"


    start_url = joblist_url.format(urllib.quote(keyword),1)
    cookies = dict(guide='1')
    r = requests.get(start_url,cookies=cookies,)
    r.encoding = 'gb2312'
    soup = BeautifulSoup(r.text,"html.parser")
    tag_pagenum = soup.find_all('span',class_ = 'td')[0].string
    a = tag_pagenum.find(u'共')
    b = tag_pagenum.find(u'页')
    pagenum = tag_pagenum[a+1:b]
    print pagenum

    for i in range(1,int(pagenum)+1):
        r = requests.get(joblist_url.format(urllib.quote(keyword),i),cookies=cookies,)
        r.encoding = 'gb2312'
        soup = BeautifulSoup(r.text,'html.parser')
        with open('51job_html\\'+str(i)+'.html','w') as f:
            f.write(str(soup))
        print process_51job.process(soup)
        with open('51job_pick\\'+str(i)+'.pick','w') as f:
            f.write(pickle.dumps(process_51job.process(soup)))
        print u'已爬取'+str(i)+u'个网页'
    print '爬取完毕，请签收'


if __name__ == '__main__':
    keyword = '大数据'
    start_page = 1
    crawler(keyword,start_page)

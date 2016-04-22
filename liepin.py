# encoding: utf-8
import urllib2
import random
import urlfunc
from bs4 import BeautifulSoup
baseurl=r'https://www.liepin.com/zhaopin/?pubTime=&salary=&searchType=1&clean_condition=&jobKind=&isAnalysis=&init=-1&sortFlag=15&searchField=1&key=%E4%BC%9A%E8%AE%A1&industries=&jobTitles=&dqs=280&compscale=&compkind=&ckid=a92d6f07f665295d&curPage={0}'
# https://www.liepin.com/zhaopin/?pubTime=&salary=&searchType=1&amp;clean_condition=&jobKind=&isAnalysis=&amp;init=-1&amp;sortFlag=15&searchField=1&amp;key=%E4%BC%9A%E8%AE%A1&industries=&jobTitles=&dqs=280020&amp;compscale=&compkind=&ckid=837c183a94754c9b&curPage=1
# https://www.liepin.com/zhaopin/?pubTime=&salary=&searchType=1&amp;clean_condition=&jobKind=&isAnalysis=&amp;init=1&amp;sortFlag=15&searchField=1&;key=%E4%BC%9A%E8%AE%A1&amp;industries=&jobTitles=&dqs=280&compscale=&amp;compkind=


def process(soup):
    result = []
    for i in soup.find_all('div',class_='sojob-item-main clearfix'):
        per_result = {}
        per_result['job_title'] = i.find('h3')['title'].lstrip().rstrip()
        per_result['job_link'] = i.find_all('a',target = '_blank')[0]['href'].lstrip().rstrip()
        per_result['job_name'] = i.find_all('a',target = '_blank')[0].string.lstrip().rstrip()
        per_result['job_condition'] = i.find('p',class_='condition clearfix')['title'].lstrip().rstrip()
        try:
            per_result['job_companylink'] = i.find_all('a',target = '_blank')[1]['href'].lstrip().rstrip()
            per_result['job_companyname'] = i.find_all('a',target = '_blank')[1].string.lstrip().rstrip()
        except KeyError:
            per_result['job_companylink'] = ''
            per_result['job_companyname'] = ''
        per_result['job_companyfield'] = i.find('p',class_='field-financing').find('span').string
        per_result['job_goods'] = ''
        goods = i.find('p',class_='temptation clearfix').find_all('span')
        for ii in goods:
            per_result['job_goods']+=ii.string.lstrip().rstrip()
            per_result['job_goods']+=' '
        result.append(per_result)
    return result
num = 0
job_num = 0
result = []
while True:
    f=open('liepin_account.txt','wa')
    url = baseurl.format(str(num))
    soup = urlfunc.url_open(url)
    if len(soup.find_all('div',class_='alert alert-info sojob-no-result-alert')):
        print 'crawl complete'
        for i in result:
            f.write(i.encode('utf-8'))
            f.write('\n')
        f.close()
        break
    else:
        # print process(soup)
        for i in process(soup):
            job_num+=1
            print job_num
            for ii in i:
                if i[ii]:
                    print ii+':'+(len('job_companyfield')-len(ii))*' '+i[ii]
                    result.append(ii+':'+(len('job_companyfield')-len(ii))*' '+i[ii])
                else:
                    print ii+':'+'none'
                    result.append(ii+':'+'none')
    num+=1

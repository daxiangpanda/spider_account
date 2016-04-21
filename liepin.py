# encoding: utf-8
import urllib2
import random
from bs4 import BeautifulSoup
baseurl = r'https://www.liepin.com/zhaopin/?pubTime=&salary=&searchType=1&amp;clean_condition=&jobKind=&isAnalysis=&amp;init=-1&amp;sortFlag=15&searchField=1&amp;key=%E4%BC%9A%E8%AE%A1&industries=&jobTitles=&dqs=280020&amp;compscale=&compkind=&ckid=837c183a94754c9b&curPage='
# https://www.liepin.com/zhaopin/?pubTime=&salary=&searchType=1&amp;clean_condition=&jobKind=&isAnalysis=&amp;init=-1&amp;sortFlag=15&searchField=1&amp;key=%E4%BC%9A%E8%AE%A1&industries=&jobTitles=&dqs=280020&amp;compscale=&compkind=&ckid=837c183a94754c9b&curPage=1
# https://www.liepin.com/zhaopin/?pubTime=&salary=&searchType=1&amp;clean_condition=&jobKind=&isAnalysis=&amp;init=1&amp;sortFlag=15&searchField=1&;key=%E4%BC%9A%E8%AE%A1&amp;industries=&jobTitles=&dqs=280&compscale=&amp;compkind=
def url_open(url):
    req = urllib2.Request(url)
    header1 = 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5'
    header2 = 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5'
    header3 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X; en-us) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53'
    header4 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4'
    header5 = 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+'
    header6 = 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+'
    header7 = 'Mozilla/5.0 (Linux; Android 4.4.4; en-us; Nexus 5 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2307.2 Mobile Safari/537.36'
    header8 = 'Mozilla/5.0 (Linux; Android 4.3; Nexus 10 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2307.2 Safari/537.36'
    header9 = 'Mozilla/5.0 (Linux; Android 4.3; Nexus 7 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2307.2 Safari/537.36'
    header10 = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)'
    header11 = 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13'
    header12 = 'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    header = [header1,header2,header3,header4,header5,header6,header7,header8,header9,header10,header11,header12]
    req.add_header('User-Agent',random.choice(header))
    # proxies = ['120.195.198.69:80','120.195.195.249:80','112.64.28.11:8090']
    # proxy = random.choice(proxies)
    #
    # proxy_support = urllib2.ProxyHandler({'http':proxy})
    # opener = urllib2.build_opener(proxy_support)
    # urllib2.install_opener(opener)
    response = urllib2.urlopen(req)
    html = response.read()
    #print html
    return html

def process(soup):
    result = []
    for i in soup.find_all('div',class_='sojob-item-main clearfix'):
        # print i
        per_result = {}
        per_result['job_title'] = i.find('h3')['title']
        # print per_result['job_title']
        per_result['job_link'] = i.find_all('a',target = '_blank')[0]['href']
        per_result['job_name'] = i.find_all('a',target = '_blank')[0].string
        per_result['job_condition'] = i.find('p',class_='condition clearfix')['title']
        try:
            per_result['job_companylink'] = i.find_all('a',target = '_blank')[1]['href']
            per_result['job_companyname'] = i.find_all('a',target = '_blank')[1].string
        except KeyError:
            per_result['job_companylink'] = ''
            per_result['job_companyname'] = ''
        per_result['job_companyfield'] = i.find('p',class_='field-financing').find('span').string
        per_result['job_goods'] = ''

        goods = i.find('p',class_='temptation clearfix').find_all('span')
        for ii in goods:
            per_result['job_goods']+=ii.string
            per_result['job_goods']+=' '
        result.append(per_result)
    return result
num = 0
result = []
while True:
    url = baseurl+str(num)
    html = url_open(url)
    soup = BeautifulSoup(html)
    # print html
    if len(soup.find_all('div',class_='alert alert-info sojob-no-result-alert')):
        print 'crawl complete'
        break
    else:
        print process(soup)
	
    num+=1


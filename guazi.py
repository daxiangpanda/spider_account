# encoding=utf-8
# 瓜子二手车居然也要cookies
# 我试试？
import urlfunc
import urllib
import requests
from bs4 import BeautifulSoup

def crawler(start_page):
    joblist_url = 'http://www.guazi.com/cd/buy/o{0}/'


    start_url = joblist_url.format(start_page)
    print start_url
    cookies = dict(lg='1')
    r = requests.get(start_url,cookies=cookies,)
    r.encoding = 'utf-8'
    return r.text
    # with open('guazi{0}.html'.format(start_page),'w') as f:
    #     f.write(r.text.encode('utf-8'))
    # print r.text
    # print type(r.text.encode('utf-8'))


def process(html):
    soup = BeautifulSoup(html)
    result = []
    baseurl = 'www.guazi.com/'
    for i in soup.find_all('div',class_='list')[0].find_all('li'):
        sub_res = {}
        sub_res['car_link'] = baseurl+i.find_all('a')[1]['href']
        print 'car_link'
        sub_res['car_name'] = i.find_all('a')[1]['title']
        print 'car_name'
        car_state = i.find_all('p')[1].text
        sub_res['car_starttime'] = car_state.split('|')[0]
        print 'car_starttime'
        sub_res['car_length'] = car_state.split('|')[1].lstrip()
        print 'car_length'
        try:
            sub_res['car_price'] = i.find_all('i')[0].string.lstrip().rstrip()
            print 'car_price'
        except AttributeError:
            sub_res['car_price'] = 'none'
            print 'no car_price'
        try:
            sub_res['car_originalprice'] = i.find('s').string
            print 'car_originalprice'
        except AttributeError:
            sub_res['car_originalprice'] = 'none'
            print 'no car_originalprice'
        sub_res['car_image_link'] = i.find('img')['src']
        print 'car_image_link'
        result.append(sub_res)
    return result


if __name__ == '__main__':
    for i in range(1,10):
        result = process(crawler(i))
        for i in result:
            for ii in i:
                print ii,':',i[ii]

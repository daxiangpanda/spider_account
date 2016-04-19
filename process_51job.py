from bs4 import BeautifulSoup
import sys
sys.setrecursionlimit(1000000)
def process(soup):
    result = []
    for i in soup.find_all('div', class_='el'):
        test = i.find_all('p',class_='t1')
        # print test
        # print len(test)
        sub_result = {}
        if len(test)<1:
            continue
        sub_result['position'] = i.find('p', class_='t1').find('a')['title']
        sub_result['position_link'] = i.find('p', class_='t1').find('a')['href']
        sub_result['company'] = i.find('span', class_='t2').find('a')['title']
        sub_result['company_name'] = i.find('span', class_='t2').find('a')['href']
        sub_result['location'] = i.find('span', class_='t3').string
        sub_result['wage'] = i.find('span', class_='t4').string
        sub_result['date'] = i.find('span', class_='t5').string
        result.append(sub_result)
    return result

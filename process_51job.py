from bs4 import BeautifulSoup
def process(soup):
    result = []
    for i in soup.find_all('div', class_='el'):
        test = i.find_all('p',class_='t1')
        # print test
        # print len(test)
        if len(test)<1:
            continue
        position = i.find('p', class_='t1').find('a')['title']
        position_link = i.find('p', class_='t1').find('a')['href']
        company = i.find('span', class_='t2').find('a')['title']
        company_name = i.find('span', class_='t2').find('a')['href']
        location = i.find('span', class_='t3').string
        wage = i.find('span', class_='t4').string
        data = i.find('span', class_='t5').string
        result.append([position, position_link, company, company_name, location, wage, data])
    return result

with open('51job_html\\1.html','r') as f:
    soup = BeautifulSoup(f.read(),"html.parser")
print process(soup)
# for i in soup.find_all('div',class_='el'):
#     print i.find_all('p',class_='t1')
#     print

for i in process(soup):
    for ii in i:
        print ii
    print
    print
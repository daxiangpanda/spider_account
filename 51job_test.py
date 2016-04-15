import urllib
from bs4 import BeautifulSoup
base_url = 'http://search.51job.com/list/090200%252C00,%2B,%2B,%2B,%2B,%2B,%25B3%25F6%25C4%25C9,0,%2B.html?lang=c&stype=1&image_x=50&image_y=20&specialarea=00'
html = urllib.urlopen(base_url).read()
soup = BeautifulSoup(html,"html.parser")
# html = urllib.urlopen(base_url).read()
real_link = soup.find('a',id='dw_close')['href']
real_html = urllib.urlopen(real_link).read()
# print html
with open('51job_real.html','w') as f:
    f.write(real_html)
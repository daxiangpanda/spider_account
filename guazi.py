import urlfunc

soup = urlfunc.url_open('http://www.guazi.com/cd/buy/o7/')

print soup.find_all('a',class_="info-title")
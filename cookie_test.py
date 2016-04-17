import urllib2
import cookielib

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

response = opener.open('http://search.51job.com/list/%2B,%2B,%2B,%2B,%2B,%2B,%25BB%25E1%25BC%25C6,0,%2B.html?lang=c&stype=1&image_x=0&image_y=0')

for item in cookie:
    print item.name
    print item.value

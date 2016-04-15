base_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%88%90%E9%83%BD&kw=%E4%BC%9A%E8%AE%A1&sm=0&isfilter=0&fl=801&isadv=0&sg=e1b9f5c9a6c54d9f8fab2a38dece44aa&p='
start_page = 0
from lxml import etree
import urllib

html = urllib.urlopen(base_url+str(start_page)).read()
# print html
tree = etree.HTML(html)
print tree
for i in tree.xpath('//table[@cellpadding=0]'):
    if len(i.xpath('.//td[@class="gsmc"]/a/text()')):
        print i.xpath('.//td[@class="gsmc"]/a/text()')[0]
def extract(file, decoding, xpath):
    html = readFile(file, decoding)
    tree = etree.HTML(html)
    return tree.xpath(xpath)
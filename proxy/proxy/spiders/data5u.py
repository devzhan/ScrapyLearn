# -*- coding: utf-8 -*-
# __author__: owen_zhan

import scrapy
from bs4 import BeautifulSoup

from proxy.items import ProxyPoolItem


class Data5uSpider(scrapy.Spider):
    name = "data5u"
    allowed_domains = ["data5u.com"]
    # start_urls = [
    #     'http://www.data5u.com/free/gngn/index.shtml',
    # ]

    headers = {
        'User-Agent':' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',

    }

    def start_requests(self):
        yield scrapy.Request("http://www.data5u.com/free/gngn/index.shtml",headers=self.headers)
        yield scrapy.Request("http://www.data5u.com/free/gnpt/index.shtml",headers=self.headers)
        yield scrapy.Request("http://www.data5u.com/free/gwgn/index.shtml",headers=self.headers)
        yield scrapy.Request("http://www.data5u.com/free/gwpt/index.shtml",headers=self.headers)

    def parse(self, response):
        soup=BeautifulSoup(response.text,"html.parser")
        l2s=soup.find_all('ul',class_='l2')
        for l2 in l2s:
            ipconfig=l2.find_all('li')
            ip=ipconfig[0].text
            ports=ipconfig[1].text
            types = ipconfig[6].text
            protocols=ipconfig[3].text
            address=ipconfig[5].text
            time=ipconfig[8].text
            yield ProxyPoolItem({
                'ip': ip,
                'protocol': protocols,
                'port': ports,
                'types': types,
                'address': address,
                'website': 'http://www.data5u.com/',
                'time': time
            })




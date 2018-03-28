# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from proxy.items import ProxyPoolItem
from bs4 import BeautifulSoup

class Ip3366Spider(scrapy.Spider):
    name = 'ip3366'
    allowed_domains = ['ip3366.net']
    start_urls = ['http://www.ip3366.net/free/?stype=1']
    def parse(self, response):

        soup = BeautifulSoup(response.text,'html.parser')
        trs=soup.find_all('tbody')[0].find_all('tr')
        print(trs)
        for tr in trs:
            ips=tr.find_all('td')
            ip = ips[0].text
            protocols = "HTTP"
            ports = ips[1].text
            address = ips[4].text
            time = ips[6].text
            types = ips[2].text
            yield ProxyPoolItem({
                'ip': ip,
                'protocol': protocols,
                'port': ports,
                'types': types,
                'address': address,
                'website': 'www.httpsdaili.com/',
                'time': time
            })

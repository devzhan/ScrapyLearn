# -*- coding: utf-8 -*-
# __author__: owen_zhan

import scrapy
from proxy.items import ProxyPoolItem
from bs4 import BeautifulSoup


class HttpsDaiLiSpider(scrapy.Spider):
    name = 'httpsdaili'
    allowed_domains = ['httpsdaili.com']
    start_urls = ['http://www.httpsdaili.com/?stype=1',
                  'http://www.httpsdaili.com/?stype=2',
                  'http://www.httpsdaili.com/?stype=3',]

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        trs = soup.find_all('tr', class_='odd')
        for tr in trs:
            ips=tr.find_all('td')
            ip=ips[0].text
            protocols = "HTTP"
            ports = ips[1].text
            address = ips[4].text
            time = ips[6].text
            types=ips[2].text
            yield ProxyPoolItem({
                'ip': ip,
                'protocol': protocols,
                'port': ports,
                'types': types,
                'address': address,
                'website': 'www.httpsdaili.com/',
                'time': time
            })

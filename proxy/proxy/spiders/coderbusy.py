# -*- coding: utf-8 -*-
# __author__: owen_zhan

import scrapy
from proxy.items import ProxyPoolItem
from bs4 import BeautifulSoup


class CoderBusySpider(scrapy.Spider):
    name = 'coderbusy'
    allowed_domains = ['coderbusy.com']

    start_urls = [
        'https://proxy.coderbusy.com/',
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        itmes = soup.find_all("tbody")
        trs = itmes[0].find_all('tr')
        for tr in trs:
            ips = tr.find_all('td')
            ip = ips[0].text.strip()
            protocols = "HTTP"
            ports = ips[1].text
            address = ips[2].text
            types = ips[3].text
            time = ips[5].find("span").get('title')
            yield ProxyPoolItem({
                'ip': ip,
                'protocol': protocols,
                'port': ports,
                'types': types,
                'address': address,
                'website': 'www.proxy.coderbusy.com/',
                'time': time
            })

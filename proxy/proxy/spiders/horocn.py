# -*- coding: utf-8 -*-
# __author__: owen_zhan

import scrapy
from proxy.items import ProxyPoolItem
from bs4 import BeautifulSoup


class HorocnSpider(scrapy.Spider):
    name = 'horocn'
    allowed_domains = ['horocn.com']

    start_urls = [
        'https://proxy.horocn.com/free-proxy.html',
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        itmes = soup.find_all("tbody")
        trs = itmes[0].find_all('tr')
        print(trs)
        for tr in trs:
            ips = tr.find_all('th')
            ip = ips[0].text.strip()
            protocols = "HTTP"
            ports = ips[1].text
            address = ips[2].text
            time = ips[3].text
            yield ProxyPoolItem({
                'ip': ip,
                'protocol': protocols,
                'port': ports,
                'types': '',
                'address': address,
                'website': 'www.proxy.horocn.com/',
                'time': time
            })

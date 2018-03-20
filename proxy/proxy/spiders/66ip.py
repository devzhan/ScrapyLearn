# -*- coding: utf-8 -*-
# __author__: vincentlc

import scrapy
from proxy.items import ProxyPoolItem
from bs4 import BeautifulSoup


class SixSixIpSpider(scrapy.Spider):
    name = '66ip'
    allowed_domains = ['66ip.cn']

    # start_urls = [
    #     "http://www.66ip.cn/1.html",
    # ]
    name = '66ip'
    allowed_domains = ['66ip.cn']

    def start_requests(self):
        for i in range(1, 20):
                yield scrapy.Request("http://www.66ip.cn/{0}.html".format(i),
                                     callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        # print(soup)
        trs = soup.find_all("table", border="2px")[0].find_all("tr")
        trs.pop(0)
        for tr in trs:
            ips = tr.find_all('td')
            ip = ips[0].text
            protocols = "HTTP"
            ports = ips[1].text
            address = ips[2].text
            types = ips[3].text
            time = ips[4].text
            yield ProxyPoolItem({
                'ip': ip,
                'protocol': protocols,
                'port': ports,
                'types': types,
                'address': address,
                'website': 'www.66ip.cn',
                'time': time
            })

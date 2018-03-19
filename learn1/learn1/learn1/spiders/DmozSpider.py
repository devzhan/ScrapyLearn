import scrapy
from bs4 import BeautifulSoup as BS
class DmozSpider(scrapy.Spider):
    # 必须定义
    name = "dmoz"
    # 初始urls
    start_urls = [
        "http://www.mzitu.com/",
    ]
 
    # 默认response处理函数
    def parse(self, response):
        # 把结果写到文件中
        # print(response.text)
        pageSoup=BS(response.text,"html.parser")
        items=pageSoup.find_all('a',target="_blank")

        for item in items:
            if item.has_attr('href'):
                print(item.get('href'))
                print(item.text)
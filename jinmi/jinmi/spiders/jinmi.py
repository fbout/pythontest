import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
#from jinmi.items import JinmiItems

class Myspider(scrapy.Spider):
    name = "jinmi"
    #allowed_domains = ["http://www.geekonomics10000.com/"]
    #start_urls = ["http://www.geekonomics10000.com/"]
    #start_urls = 'http://www.baidu.com/'
    bashurl='http://www.geekonomics10000.com/page/'
    #页面提取数
    max=2

    #页面地址
    def start_requests(self):
        for i in range(1,self.max+1):
            mianurl=self.bashurl+str(i)
            yield Request(mianurl,self.parse)

    #分页地址
    def parse(self, response):
        #print(response.body)
        urls=response.xpath('//*[@id="main-content"]/div/div/h3/a/@href').extract()
        for url in urls:
            url=url
            print(url)
            yield Request(url,callback=self.get_title)

    #内容提取
    def get_title(self,response):
       title=response.xpath('//*[@id="main-content"]/div[2]/h2').extract()
       print(title)








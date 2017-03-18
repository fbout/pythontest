import scrapy
from scrapy.http import request

class Myspider(scrapy.Spider):

    name = "douban"
    allowed_domains=['dounan.com']
    bashurl='https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start='
    #bashurl='https://www.baidu.com/s?ie=UTF-8&wd='
    pages=2

    def start_requests(self):
        for i in range(1,self.pages):
            url=self.bashurl+str(i*20)
            yield scrapy.Request(url,self.parse)
    #return[scrapy.FormRequest("http://cuiqingcai.com/3472.html")]
    #start_urls=['http://cuiqingcai.com/3472.html']

    def parse(self, response):
        print(response.body)
        #print(response.xpath('/html/body/div[3]/div[1]/div/div[1]/div/div[4]/div/a[1]/p'))
        #response.xpath('//ul/li/text()').extract()
import scrapy
from scrapy.http import request

class Myspider(scrapy.Spider):

    name = "douban"
    allowed_domains=['dounan.com']

    def start_requests(self):
        return[scrapy.FormRequest("http://cuiqingcai.com/3472.html")]

    def parse(self, response):
        print(response.txt)

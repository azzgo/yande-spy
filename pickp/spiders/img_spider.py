# coding: utf-8
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from pickp.items import PickImg
from scrapy.exceptions import  CloseSpider
# from scrapy.shell import inspect_response

class Yande(Spider):
    name = 'yand'
    allowed_domains = ['yande.re']

    def start_requests(self):
        # 指定第一次请求
        return [Request('https://yande.re/post',
                        headers={
                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, lik\
                            e Gecko) Chrome/34.0.1847.116 Safari/537.36"
                        },
                        callback=self.parse_img)]

    def parse_img(self, response):
        sel = Selector(response)
        img_item = PickImg()
        for item in sel.css("#post-list-posts>li"):
            img_item['img'] = item.xpath('.//img/@title').extract()[0].split(':')[-2]
            img_item['img_url'] = item.xpath(".//a[@class='directlink largeimg' or @class='directlink\
             smallimg']/@href").extract()
            yield img_item

        next_page = sel.xpath("//a[@class='next_page']/@href").extract()
        yield Request('https://yande.re' + next_page[0],
                      headers={
                          "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, lik\
                            e Gecko) Chrome/34.0.1847.116 Safari/537.36",
                          "Refer": "yande.re"
                      },
                      callback=self.parse_img,
                      )

        if next_page[0].find("page=10") is not -1:
            # 在第10页时引发关闭异常,让爬虫不会无限运行
            raise CloseSpider(u'正常退出')
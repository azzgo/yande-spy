# coding: utf-8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.http import Request
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem


class ImageHander(ImagesPipeline):
    def get_media_requests(self, item, info):
        #获取采集到到图片url并发起请求
        if len(item['img_url']) is not 0:
            return Request(item['img_url'][0],
                      headers={
                          "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, lik\
                            e Gecko) Chrome/34.0.1847.116 Safari/537.36",
                          "Refer": "yande.re"
                      })
        else:
            return None

    def item_completed(self, results, item, info):
        #同官方文档,未修改
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
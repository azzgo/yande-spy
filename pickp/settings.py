# coding: utf-8

BOT_NAME = 'pickp'

SPIDER_MODULES = ['pickp.spiders']
NEWSPIDER_MODULE = 'pickp.spiders'

# 用来声明下载管道
ITEM_PIPELINES = {
    'pickp.pipelines.ImageHander': 2}
IMAGES_STORE = './download'

# 下载器的延迟时间
DOWNLOAD_DELAY = 2

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pickp (+http://www.yourdomain.com)'

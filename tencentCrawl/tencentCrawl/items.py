# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    positionTitle = scrapy.Field()
    #职位类别
    positionType = scrapy.Field()
    #职位人数
    positionNum = scrapy.Field()
    #职位地点
    positionAddr = scrapy.Field()
    #职位时间
    positionTime = scrapy.Field()

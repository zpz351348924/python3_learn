# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YingjieshengspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobTitle = scrapy.Field()
    jobTime = scrapy.Field()
    jobSource = scrapy.Field()
    jobLink = scrapy.Field()

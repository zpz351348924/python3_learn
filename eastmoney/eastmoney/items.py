# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EastmoneyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    eastUrl = scrapy.Field()
    eastName = scrapy.Field()
    eastOne = scrapy.Field()
    eastThree = scrapy.Field()
    eastSix = scrapy.Field()
    eastOneyear = scrapy.Field()
    eastThreeyear = scrapy.Field()
    eastAll = scrapy.Field()
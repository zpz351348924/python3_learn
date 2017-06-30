# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencentCrawl.items import TencentcrawlItem

class Tencent2Spider(CrawlSpider):
    name = 'tencent2'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=10#a']

    rules = (
        Rule(LinkExtractor(allow=('start=\d+')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #爬取页面的处理
        dataList = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        for each in dataList:
            item = TencentcrawlItem()
            item['positionTitle'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['positionNum'] = each.xpath('./td[3]/text()').extract()[0]
            item['positionAddr'] = each.xpath('./td[4]/text()').extract()[0]
            item['positionTime'] = each.xpath('./td[5]/text()').extract()[0]
            if len(each.xpath('./td[2]/text()').extract())>0:
                item['positionType'] = each.xpath('./td[2]/text()').extract()[0]
            else:
                item['positionType'] = 'Nothing'

            yield item

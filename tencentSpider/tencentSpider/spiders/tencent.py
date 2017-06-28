# -*- coding: utf-8 -*-
import scrapy
from tencentSpider.items import TencentspiderItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    url = 'http://hr.tencent.com/position.php?lid=&tid=&start='
    offset = 70
    start_urls = [url + str(offset)]

    def parse(self, response):

            #爬取页面的处理
        dataList = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        for each in dataList:
            item = TencentspiderItem()
            item['positionTitle'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['positionNum'] = each.xpath('./td[3]/text()').extract()[0]
            item['positionAddr'] = each.xpath('./td[4]/text()').extract()[0]
            item['positionTime'] = each.xpath('./td[5]/text()').extract()[0]
            if len(each.xpath('./td[2]/text()').extract())>0:
                item['positionType'] = each.xpath('./td[2]/text()').extract()[0]
            else:
                item['positionType'] = 'Nothing'

            yield item
        #用回调函数进行多url的处理
        if self.offset < 2170:
            self.offset += 10
        #回调函数
            yield scrapy.Request(self.url + str(self.offset), callback = self.parse)



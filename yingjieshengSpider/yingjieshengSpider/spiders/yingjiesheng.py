# -*- coding: utf-8 -*-
import scrapy
from yingjieshengSpider.items import YingjieshengspiderItem


class YingjieshengSpider(scrapy.Spider):
    name = 'yingjiesheng'
    allowed_domains = ['yingjiesheng.com']
    offset = 1
    url1 = 'http://www.yingjiesheng.com/jiangsujob/list_'
    url2 = '.html'

    start_urls = ['http://www.yingjiesheng.com/jiangsujob/list_1.html']

    def parse(self, response):
        dataList = response.xpath('//tr[@class="bg_0"] | //tr[@class="bg_1"]')
        for each in dataList:
            item = YingjieshengspiderItem()
            item['jobTitle'] = each.xpath('./td[@class="item1"]/a/text()').extract()[0]
            item['jobTime'] = each.xpath('./td[@class="date cen"]/text()').extract()[0]
            item['jobLink'] = each.xpath('./td[@class="item1"]/a/@href').extract()[0]
            if len(each.xpath('./td[@class="cen"]/text()').extract()) > 0:
                item['jobSource'] = each.xpath('./td[@class="cen"]/text()').extract()[0]
            else:
                item['jobSource'] = 'Nothing'

            yield item

        if self.offset < 200:  #注意使用self.offset和self.url1

            self.offset += 1

        yield scrapy.Request(self.url1+str(self.offset)+self.url2, callback = self.parse)
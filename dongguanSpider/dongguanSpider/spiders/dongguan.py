# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguanSpider.items import DongguanspiderItem

class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=0']

    rules = (
        Rule(LinkExtractor(allow=r'page=\d+'), follow = True), #没有callback默认follow为true
        Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'), follow= False, callback='parse_item'),
    )

    #该网站有反扒机制，返回了错误的url，需要用到process_links处理


    def parse_item(self, response):
        item = DongguanspiderItem()

        title=response.xpath('/html/body/div[6]/div/div[1]/div[1]/strong/text()').extract()[0]
        item['title']= title

        item['num'] = title.split(':')[-1]

        if len(response.xpath('/html/body/div[6]/div/div[2]/div[1]/div[2]/text()').extract()) >0:
            item['content'] = response.xpath('/html/body/div[6]/div/div[2]/div[1]/div[2]/text()').extract()[0]
        else:
            item['content'] = response.xpath('/html/body/div[6]/div/div[2]/div[1]/text()').extract()[0]

        item['url'] = response.url

        yield item

#/html/body/div[6]/div/div[2]/div[1]/div[2]
#/html/body/div[6]/div/div[2]/div[1]/text()
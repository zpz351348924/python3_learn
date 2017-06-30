# -*- coding: utf-8 -*-
import scrapy
from eastmoney.items import EastmoneyItem

class EastmoneyspiderSpider(scrapy.Spider):
    name = 'eastmoneySpider'
    allowed_domains = ['eastmoney.com']
    url = 'http://fund.eastmoney.com/allfund.html'

    def start_requests(self):
        yield scrapy.Request(self.url, callback = self.parse_info)

    #提取主页面所有基金url，每个url进行回调
    def parse_info(self, response):
        dataList = response.xpath('//ul[@class="num_right"]/li[@class="b"]/div | //ul[@class="num_right"]/li/div ')

        for each in dataList:
            link = each.xpath('./a[1]/@href').extract()[0]
            yield scrapy.Request(link, callback = self.parse)

    #判断函数
    def panduaninfo(self, infolist):
        if len(infolist) > 0 :
            return infolist[0]
        else:
            return '0%'

    #处理详情页数据放入item
    def parse(self, response):
        item = EastmoneyItem()
        try:
            #基金名字
            item['eastName'] = self.panduaninfo(response.xpath('//div[@class="fundDetail-tit"]/div/text()').extract())
            #基金链接
            item['eastUrl'] = self.panduaninfo(response.xpath('//h1[@class="fl"]/a/@href').extract())
            #近一个月到成立以来的收益率
            item['eastOne'] = self.panduaninfo(response.xpath('//*[@id="body"]/div[12]/div/div/div[2]/div[1]/div[1]/dl[1]/dd[2]/span[2]/text()').extract())
            item['eastThree'] = self.panduaninfo(response.xpath('//*[@id="body"]/div[12]/div/div/div[2]/div[1]/div[1]/dl[2]/dd[2]/span[2]/text()').extract())
            item['eastSix'] = self.panduaninfo(response.xpath('//*[@id="body"]/div[12]/div/div/div[2]/div[1]/div[1]/dl[3]/dd[2]/span[2]/text()').extract())
            item['eastOneyear'] = self.panduaninfo(response.xpath('//*[@id="body"]/div[12]/div/div/div[2]/div[1]/div[1]/dl[1]/dd[3]/span[2]/text()').extract())
            item['eastThreeyear'] = self.panduaninfo(response.xpath('//*[@id="body"]/div[12]/div/div/div[2]/div[1]/div[1]/dl[2]/dd[3]/span[2]/text()').extract())
            item['eastAll'] = self.panduaninfo(response.xpath('//*[@id="body"]/div[12]/div/div/div[2]/div[1]/div[1]/dl[3]/dd[3]/span[2]/text()').extract())

            yield item

        except:
            pass


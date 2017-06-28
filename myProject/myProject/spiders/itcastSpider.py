# -*- coding: utf-8 -*-
import scrapy
from myProject.items import ItcastItem


class ItcastspiderSpider(scrapy.Spider):
    name = 'itcastSpider'
    allowed_domains = ['http://www.itcast.cn/']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#']

    def parse(self, response):
        
        teacher_list = response.xpath('//div[@class="li_txt"]')

        for each in teacher_list:
        	#give a class 
        	item = ItcastItem()

        	#extract()的作用是将匹配出来的结果转换为unicode字符串
	        name = each.xpath('./h3/text()').extract()
	        title = each.xpath('./h4/text()').extract()
	        info = each.xpath('./p/text()').extract()
	        
	        item['name'] = name[0]
	        item['title'] = title[0]
	        item['info'] = info[0]

	        yield item
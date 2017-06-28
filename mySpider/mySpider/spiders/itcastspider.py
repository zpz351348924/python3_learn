# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcastItem


#创建一个爬虫类
class ItcastSpider(scrapy.Spider):
    #爬虫名
    name = 'itcast'

    #允许爬虫作用的域
    allowd_domains = ['http://www.itcast.cn/']

    #爬虫真实的URL
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#']

    #实例化一个对象


    def parse(self, response):
        print('=======================================')
        print(type(response))
        # item = ItcastItem()
        teacher_list = response.xpath('//div[@class="li_txt"]')
        # names = response.xpath('//div/h3/text()')
        # titles = response.xpath('//div/h4/text()')
        # infos = response.xpath('//div/p/text()')
        teacherItem = []

        for each in teacher_list:
            #extract()的作用是将匹配出来的结果转换为unicode字符串
            name = each.xpath('./h3/text()').extract()
            title = each.xpath('./h4/text()').extract()
            info = each.xpath('./p/text()').extract()


            print(name)

            # data= {
            #     '姓名':name.extract(),
            #     '职别':title.extract(),
            #     '介绍':info.extract(),
            # }

        #     item['name']= name.extract()
        #     item['title'] = title.extract()
        #     #item['info'] = info.extract()
        #
        #     teacherItem.append(item)
        #
        # return teacherItem
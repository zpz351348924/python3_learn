# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentspiderPipeline(object):
    #初始化一个功能，新建文件
    def __init__(self):
        self.file = open('tencentInfo.json','wb')


    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii = False) +'\n'
        self.file.write(text.encode('utf-8'))
        return item

    #关闭文件
    def closefile(self, spider):
        self.file.close()
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class YingjieshengspiderPipeline(object):

    def __init__(self):
        self.file = open('yingjiesheng.json','wb')

    def process_item(self, item, spider):
        jobtext = json.dumps(dict(item), ensure_ascii = False) +'\n'
        self.file.write(jobtext.encode('utf-8'))
        return item

    def closefile(self, spider):
        self.file.close()

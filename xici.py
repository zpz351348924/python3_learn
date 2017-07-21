#-*-encoding=utf-8-*-

import requests
from lxml import etree
import time
import pymongo
from multiprocessing import Pool


class Getproxy(object):
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        self.url = 'http://www.xicidaili.com/wt/'
        self.client = pymongo.MongoClient('localhost',27017)
        self.xici = self.client['xici']
        self.xiciipinfo =self.xici['xiciipinfo']
        #self.removeip = '127.0.0.1' #第一次运行会检测该变量，因为下面只有检测失败了才会赋值

    def getip(self,num):
        #爬西祠所有代理，更新放入数据库
        url = self.url + str(num)
        wb_data = requests.get(url, headers= self.headers)
        html = etree.HTML(wb_data.text)
        # htmls = etree.tostring(html)
        ips = html.xpath('//tr[@class="odd"]/td[2]/text()')
        ports = html.xpath('//tr[@class="odd"]/td[3]/text()')
        protocols = html.xpath('//tr[@class="odd"]/td[6]/text()')
        areas = html.xpath('//tr[@class="odd"]/td[4]/a/text()')
        for ip, port, protocol, area in zip(ips, ports, protocols, areas):
            data = {
                'ip': ip,
                'port': port,
                'protocol': protocol,
                'area': area,
            }
            print data
            #self.xiciipinfo.insert_one(data)
            #if self.removeip != ip: #此处加一个判断，如果是下面检测过的不可用的ip，就不更新进入数据库，可以节省下面的检测时间
            self.xiciipinfo.update({'ip':ip}, {'$set':data}, True)


    def count(self,num):
        for i in range(1,num):
            self.getip(i)
            time.sleep(2)


    def dbclose(self):
        self.client.close()


    def getiplist(self):
        # 将数据库内数据整理放入列表
        ips = self.xiciipinfo.find()
        proxylist = []
        for i in ips:
            # print i['ip'], i['port']
            a = i['protocol']
            b = "http" + "://" + i['ip'] + ":" + i['port']
            proxies = {"http": b}
            # print proxies
            proxylist.append(proxies)
        # print proxylist
        return proxylist

    def iptest(self, proxy):
        # 检测ip，并更新进入数据库，删掉不可用的ip
        ip = proxy['http'][7:].split(':')[0]
        try:
            requests.get('http://wenshu.court.gov.cn/', proxies=proxy, timeout = 6)
        except:
            print 'field...............>>>>>>>>>>>>>>>>>>>>>>>>'
            #self.removeip = ip #赋值给类属性
            self.xiciipinfo.remove({'ip': ip})  # 用remove方法，将符合条件的删掉
            print 'remove it now.....{}'.format(ip)
        else:
            print '<<<<<<<<<<<<<<<<<.............success'
            print proxy


if __name__ == '__main__':
    pool = Pool()
    proxy = Getproxy()
    proxy.count(2)
    iplist = proxy.getiplist()
    map(proxy.iptest, iplist)
    proxy.dbclose()

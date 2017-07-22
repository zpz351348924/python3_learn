#-*-encoding=utf-8-*-
import requests
import pymongo
import random


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

class Test_proxy(object):
    def __init__(self):
        #初始化数据库
        self.client= pymongo.MongoClient('localhost', 27017)
        self.xici = self.client['xici']
        self.xiciipinfo =self.xici['xiciipinfo']


    def get_proxies(self):
        #拿到格式化后的代理，放入列表
        proxies = []
        info = self.xiciipinfo.find()
        for each in info:
            proxy = 'http://'+each['ip']+':'+each['port']
            proxies.append(proxy)
        return proxies


    def judge_ip(self, proxies):
        proxy = random.choice(proxies)
        print proxy[7:].split(':')[0]
        try:
            requests.get('https://www.baidu.com/', proxies ={'http':proxy}, timeout = 5)
        except:
            self.xiciipinfo.remove({'ip':proxy[7:].split(':')[0]})
            print 'get ip again...>>>>>>>>>>>'
            a= self.get_proxies()
            if len(a) > 0:  #数据库中代理被删除完后会出现异常，此处判断一下
                self.judge_ip(a)
            else:
                print '<<<<<<<have no ip>>>>>>>.........'
        else:
            self.get_work(proxy)

    def get_work(self,proxy): #用代理来工作
        wb_data = requests.get('https://www.baidu.com/', proxies = {'http':proxy})
        print wb_data.text



#执行函数
def main():
    xiaotest = Test_proxy()
    proxies_list= xiaotest.get_proxies()
    if len(proxies_list) > 0:
        xiaotest.judge_ip(proxies_list)
    else:
        print ',,,,,,,,,,<<<<<<<have no ip>>>>>>>.........'

main()
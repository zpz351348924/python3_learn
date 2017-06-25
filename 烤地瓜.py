# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2017-06-21 17:28:39
# @Last Modified by:   Marte
# @Last Modified time: 2017-06-22 11:48:27

class SweetPotato(object):
    """docstring for SweetPotato"""
    def __init__(self):
        self.cookLevel = 0
        self.cookString = '生的'
        self.condiments = []
    def __str__(self):
        msg = '状态是：'+self.cookString
        if len(self.condiments)>0:
            for item in self.condiments:
                msg = msg +str(item)
        return msg

    def cook(self,usetime):
        self.cookLevel+= usetime
        if self.cookLevel >8:
            self.cookString = '烤糊了。。。'
        elif 5<self.cookLevel<=8:
            self.cookString= '熟了'
        elif 3<self.cookLevel<=5:
            self.cookString = '半生不熟的'
        else:
            self.cookString = '生的'
    def burden(self,*something):
        self.condiments.append(something)




digua = SweetPotato()
print(digua)
digua.cook(1)
digua.cook(3)
print(digua)
print('=====加辅料=====')
digua.burden('番茄酱','辣酱')
print(digua)
print('继续烤')
digua.cook(5)
print(digua)
digua.burden('芥末')
print(digua)
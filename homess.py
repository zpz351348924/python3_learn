# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2017-06-22 12:05:44
# @Last Modified by:   Marte
# @Last Modified time: 2017-06-24 14:11:50

#定义一个家类
class Home(object):
    def __init__(self,  area=200):
        self.area = area
        self.rongnaList = []


    def __str__(self):
        msg = '这个房子是：'+str(self.area)+'平米'
        if len(self.rongnaList)>0:
            msg += '；现在包含：'
            for item in self.rongnaList:
                msg += item.getBedname()+', '
            msg = msg.strip(', ')
        return msg

    def containItem(self,item):
        bedarea = item.getBedArea()
        if self.area >bedarea:
            self.rongnaList.append(item)
            self.area -=bedarea
            print('成功添加物品：%s'%item.getBedname())
        else:
            print('错误,添加的物品面积过大')

    def __test(self):  #私有方法和私有属性一样，只能在父类里面调用。
        print('---------')

    def test1(self):
        print('-----Home-----类')
        print('home')

#定义一个床的类
class Bed(object):
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        msg = '床的名字是：'+self.name +',大小是：'+str(self.area)
        return msg

    def getBedArea(self):
        return self.area

    def getBedname(self):
        return self.name



class Table(Home):
    def test2(self):
        Home.test1(self)
        print('-----use super-----')
        super().test1()
        print('----Table-----类')
        print('table')

home = Home(180)

bed = Bed('席梦思床',4)
print(bed)

home.containItem(bed)
print(home)

bed2 = Bed('木板床',30)

home.containItem(bed2)
print(home)

table=Table()
table.test2()



#多继承,广度遍历
class Base(object):
    def test(self):

        print('------base-----')

class A(Base):
    def test1(self):
        print('----A----')

class B(Base):
    def test1(self):
        print('----B----')

class C(A, B):
    pass

c= C()
c.test()


#类方法和类属性，实例属性和方法
class Horse(object):
    """docstring for Horse"""

    #类属性
    horseNum = 0

    #实例属性
    def __init__(self, name='白龙马', color='白色'):

        self.name = name
        self.color = color
        self.setHorseNum()

    def __str__(self):
        return self.name + self.color

    @classmethod
    def setHorseNum(self):
        self.horseNum+=1


bailongma = Horse()
print(bailongma)
print(Horse.horseNum) #直接打印类属性

Horse.horseNum = 1 #直接修改类属性
print(Horse.horseNum)

bailongma.horseNum = 2 #此代码是创建一个一样名字的实例属性，并未改变类属性
print(Horse.horseNum)
print(bailongma.horseNum)

print('----------')
#将类属性保护起来，在__init__里面调用，创建一个Horse对象，就默认调用一次
print(Horse.horseNum)
cetuma = Horse()
print(Horse.horseNum)



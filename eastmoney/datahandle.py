# -*- coding: utf-8 -*-

import pymongo
import pandas as pd

#设置链接信息
client = pymongo.MongoClient('localhost', 27017)
eastmoneyinfo = client['eastmoneyinfo']
eastinfo = eastmoneyinfo['eastinfo']

#加载数据到pandas中
data= pd.DataFrame(list(eastinfo.find()))

#删除_id字段
del data['_id']

#选择需要显示的字段
#data = data[['eastAll']]

#print data.head()

df = data
#观察数据
print df.index
print df.columns

#去掉数据中名字和地址，方便以后排序
df_no_name = df.drop(['eastName','eastUrl'], axis = 1)

#替换所有的%和--
def clean_num_in_column(column):
    return column.apply(drop_percent_sign)

def drop_percent_sign(state):
    if column.endswith('-'):
        return float(column.replace('-','0'))
    elif column.endswith('%'):
        return float(column.replace('%',''))


df_drop_percent = df_no_name.apply(clean_num_in_column)



#去掉空字符
df = df_drop_percent.dropna()

#查询出每一列的最大值基金，排序
def get_large_in_column(column):
    return column.sort_values(ascending=False).iloc[0]
df.apply(get_large_in_column)

#基于eastAll排序，取出前100个
range=100
df.sort_values(by=['eastAll'],ascending=False).head(range)
#这100个的index值
df.sort_values(by=['eastAll'], ascending=False).head(range).index

#可以把所有的排序完，放入set集合，这样可以去重,综合选取最优基金
fs_index=df.sort_values(by=['eastAll'], ascending=False).head(range).index
y3_index=df.sort_values(by=['eastThreeyear'], ascending=False).head(range).index
y1_index=df.sort_values(by=['eastOneyear'], ascending=False).head(range).index
m6_index=df.sort_values(by=['eastSix'], ascending=False).head(range).index
m3_index=df.sort_values(by=['eastThree'], ascending=False).head(range).index
m1_index=df.sort_values(by=['eastOne'], ascending=False).head(range).index

#全部集合化
fs_index_set=set(fs_index)
y3_index_set=set(y3_index)
y1_index_set=set(y1_index)
m6_index_set=set(m6_index)
m3_index_set=set(m3_index)
m1_index_set=set(m1_index)

#取3年，1年，6,3,1个月都在涨的基金
mix_5c = y3_index_set&y1_index_set&m6_index_set&m3_index_set&m1_index_set
#集合打印出来看看
print mix_5c

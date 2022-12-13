# -*- coding: utf-8 -*-
import pandas as pd
import string
import datetime
df = pd.read_csv("C:\\Users\\shi'shuai'shuai'a\\Desktop\\可视化大作业\\平安银行的分公司.csv",sep=',', encoding='utf-8')
dic={}
for i in df["地区"]:
    if i[0:2] not in dic.keys():
        dic[i[0:2]]=1
    else:
        dic[i[0:2]]+=1
print(dic)
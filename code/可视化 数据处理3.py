# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv("C:\\Users\\shi'shuai'shuai'a\\Desktop\\可视化大作业\\平安银行投资分布表.csv",sep=',', encoding='utf-8')
dic={}
for i in range(0,21):
    if df.loc[i][1] not in dic.keys():
        dic[df.loc[i][1]]=1
    else:
        dic[df.loc[i][1]]+=1
print(dic.values())
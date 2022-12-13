# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv("C:\\Users\\shi'shuai'shuai'a\\Desktop\\可视化大作业\\平安银行7年收支表.csv",sep=',', encoding='utf-8')
df1 = pd.DataFrame(columns=(['2016年','2017年','2018年','2019年','2020年','2021年','2022年']))
df1.loc["营业收入"]=""
df1.loc["营业支出"]=""
for i in range(1,8):
    df1.iloc[0][i-1]=df.loc[0][i]
    df1.iloc[1][i-1]=float(df.loc[0][i])-float(df.loc[1][i])
print(df1)

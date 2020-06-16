# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:19:01 2020

@author: buyewen
"""

'''
Action1：求2+4+6+8+...+100的求和，用Python该如何写
'''
print("----------Action1----------")
import numpy as np

data = np.arange(2, 101, 2)
print(data.sum())

'''
Action2: 统计全班的成绩
班里有5名同学，现在需要你用Python来统计下
这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
然后把这些人的总成绩排序，得出名次进行成绩输出（可以用numpy或pandas）
姓名  语文  数学  英语
张飞  68    65    30
关羽  95    76    98
刘备  98    86    88
典韦  90    88    77
许禇  80    90    90
'''
print("----------Action2----------")
import pandas as pd
from pandas import DataFrame

data = DataFrame({"姓名": ["张飞", "关羽", "刘备", "典韦", "许禇"],
                  "语文": [68, 95, 98, 90, 80],
                  "数学": [65, 76, 86, 88, 90],
                  "英语": [30, 98, 88, 77, 90]})
#print(data)
print(data.describe())
varC = data["语文"].var()
varM = data["数学"].var()
varE = data["英语"].var()
print("var   %f %f %f" %(varC, varM, varE))

def sumOfScore(d):
    d["总成绩"] = d["语文"] + d["数学"] + d["英语"]
    return d
data = sumOfScore(data).sort_values(by="总成绩", ascending=False).reset_index(drop=True)
print(data)

'''
Action3: 对汽车质量数据进行统计
数据集：car_complain.csv
600条汽车质量投诉
Step1，数据加载
Step2，数据预处理
拆分problem类型 => 多个字段
Step3，数据统计
对数据进行探索：品牌投诉总数，车型投诉总数
哪个品牌的平均车型投诉最多
'''
print("----------Action3----------")
print("STEP1:")
car_comp_data = DataFrame(pd.read_csv("car_complain.csv"))
car_comp_data["brand"].replace("一汽-大众", "一汽大众", inplace=True)
print(car_comp_data)
car_comp_data.to_excel("car_complain.xlsx")

print("STEP2:")
problem_data = car_comp_data.problem.str.get_dummies(",")
#print(problem_data)
car_comp_data = car_comp_data.drop(columns = ["desc", "problem", "datetime", "status"]).join(problem_data)
print(car_comp_data)

print("STEP3:")
'''
for name, group in car_comp_data.groupby(["brand", "car_model"]):
    print(name)
    print(group)
car_comp_data.groupby(["brand", "car_model"]).size().to_excel("count.xlsx")
'''

brand_count = car_comp_data["id"].groupby(car_comp_data["brand"]).agg(["count"])\
    .sort_values(by="count", ascending=False)
''' 
#for problem summary merge
tags = car_comp_data.columns[4:]
problem_sum = car_comp_data[tags].groupby(car_comp_data["brand"]).agg(["sum"])
brand_count = pd.merge(brand_count, problem_sum, on="brand")
'''
print(brand_count)

model_count = car_comp_data["id"].groupby(car_comp_data["car_model"]).agg(["count"])\
    .sort_values(by="count", ascending=False)
'''
#for problem summary merge
problem_sum = car_comp_data[tags].groupby(car_comp_data["car_model"]).agg(["sum"])
model_count = pd.merge(model_count, problem_sum, on="car_model")
'''
print(model_count)

ave_model_count = car_comp_data.groupby(["brand", "car_model"])["id"].agg(["count"])\
    .groupby("brand").mean().sort_values(by="count", ascending=False)
print(ave_model_count)

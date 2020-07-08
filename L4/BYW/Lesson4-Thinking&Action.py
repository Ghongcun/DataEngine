# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:02:15 2020

@author: buyewen
"""


import pandas as pd

data = pd.read_csv("BreadBasket_DMS.csv")
#print(data)
data['Item'] = data['Item'].str.lower()
#print(data)

data = data.drop(data[data.Item == "none"].index)
#print(data)

orders_series = data.set_index("Transaction")["Item"]
#print(orders_series)

transactions = []
temp_index = 0
'''
for i, v in orders_series.items():
    if i != temp_index:
        temp_set = set()
        temp_index = i
        temp_set.add(v)
        transactions.append(temp_set)
    else:
        temp_set.add(v)
'''
temp_set = set()
for i, v in orders_series.items():
    if i != temp_index:
        if len(temp_set) != 0:
            transactions.append(temp_set)
        temp_set = set()
        temp_index = i
        temp_set.add(v)
    else:
        temp_set.add(v)


#Action
import time
from efficient_apriori import apriori

dataset = pd.read_csv("Market_Basket_Optimisation.csv", header = None)
#print(dataset.shape)
#dataset.to_csv("collect.csv")

transactions = []
for i in range(0, dataset.shape[0]):
    temp = []
    for j in range(0, dataset.shape[1]):
        if str(dataset.values[i, j]) != "nan":
            temp.append(str(dataset.values[i, j]))
    transactions.append(temp)
#print(transactions)

start = time.time()
itemsets, rules = apriori(transactions, min_support = 0.05, min_confidence = 0.2)
end = time.time()
print("频繁项集：", itemsets)
print("关联规则：", rules)
print("efficient_apriori用时：", end - start)

print("*" * 100)

from mlxtend.frequent_patterns import apriori as mlapriori
from mlxtend.frequent_patterns import association_rules

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
    
tp = []
tq = []
x = 0
for list in transactions:
    for y in list:
        tp.append(x)
        tq.append(y)
    x = x + 1
data = zip(tp, tq)
df = pd.DataFrame(data, columns=["Transaction", "Items"])
#df.to_csv('temp1.csv')

hot_encoded_df = df.groupby(["Transaction", "Items"])["Items"].count().unstack().reset_index().fillna(0).set_index("Transaction")
hot_encoded_df = hot_encoded_df.applymap(encode_units)
start = time.time()
frequent_itemsets = mlapriori(hot_encoded_df, min_support = 0.05, use_colnames = True)
rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 0.5)
end = time.time()
print("频繁项集：", frequent_itemsets.sort_values(by = "support", ascending = False))
print("关联规则：", rules[(rules["lift"] >= 1) & (rules["confidence"] >= 0.2)].sort_values(by = "lift", ascending = False))
print("mlxtend_apriori用时：", end - start)

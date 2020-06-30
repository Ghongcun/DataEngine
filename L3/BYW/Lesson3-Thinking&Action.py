# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:38:57 2020

@author: buyewen
"""

from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

data = pd.read_csv("car_data.csv", encoding = "gbk")
#print(data)
train_x = data[["人均GDP", "城镇人口比重", "交通工具消费价格指数", "百户拥有汽车量"]]

min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
#print(train_x)

sse = []
for k in range(1, 15):
    kmeans = KMeans(n_clusters = k)
    kmeans.fit(train_x)
    sse.append(kmeans.inertia_)

import matplotlib.pyplot as plt
x = range(1, 15)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()

kmeans = KMeans(n_clusters = 4)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
#print(predict_y)

#train_x = pd.concat((data, pd.DataFrame(predict_y)), axis = 1)
result = pd.DataFrame(data).join(pd.DataFrame(predict_y))
#print(result)
result.rename({0:u"KMean聚类结果"}, axis = 1, inplace = True)
print(result)

from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

model = AgglomerativeClustering(linkage = "ward", n_clusters = 4)
predict_y = model.fit_predict(train_x)
#print(predict_y)

result = pd.DataFrame(data).join(pd.DataFrame(predict_y))
#print(result)
result.rename({0:u"层级聚类结果"}, axis = 1, inplace = True)
print(result)

linkage_matrix = ward(train_x)
dendrogram(linkage_matrix)
plt.show()
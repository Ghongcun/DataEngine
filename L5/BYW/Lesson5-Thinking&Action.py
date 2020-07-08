# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 13:18:51 2020

@author: buyewen
"""

from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
import pandas as pd
import matplotlib.pyplot as plt

def create_word_cloud(f):
    #f = remove_stop_workds(f)
    cut_text = word_tokenize(f)
    print(cut_text)
    cut_text = " ".join(cut_text)
    wc = WordCloud(max_words = 100, width = 2000, height = 1200)
    wordcloud = wc.generate(cut_text)
    wordcloud.to_file("wordcloud.jpg")
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

dataset = pd.read_csv("Market_Basket_Optimisation.csv", header = None)
#print(dataset)
dataset.to_csv("collect.csv")


data = ""
for i in range(0, dataset.shape[0]):
    for j in range(0, dataset.shape[1]):
        if str(dataset.values[i, j]) != "nan":
            data += str(dataset.values[i, j])
            data += " "

#print(data)

create_word_cloud(data)
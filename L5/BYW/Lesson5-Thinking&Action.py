# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 13:18:51 2020

@author: buyewen
"""

from wordcloud import WordCloud, ImageColorGenerator
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from collections import Counter
import seaborn as sns

def create_visual_show(f):
    count = Counter(f)
    #print(count)
    dictionary = dict(count)
    #print(dictionary)
    
    '''
    labels = list(list_show.keys())
    num = list(list_show.values())
    '''
    
    k = 30
    list_show = count.most_common(k)
    #print(list_show)
    
    labels = [i[0] for i in list_show]
    num = [i[1] for i in list_show]
    
    print(labels)
    print(num)
    
    sns.barplot(labels, num)
    plt.xticks(rotation = 90)
    plt.show()
    
    plt.figure(figsize = (18, 10))
    plt.pie(x = num, labels = labels)
    plt.legend(labels)
    plt.legend(loc = "center right")
    plt.axis('equal')
    plt.show()
    

def create_word_cloud(f):
    #f = remove_stop_workds(f)
    #print(type(f))
    
    '''
    #if f is not a standard string like "aaa bbb ccc ddd"
    cut_text = word_tokenize(f)
    print(cut_text)
    cut_text = " ".join(cut_text)
    print(cut_text)
    '''
    
    #Condition1 : if cut_text is a string and already seprated clearly
    cut_text = f
    #Condition2 : if cut_text is a list
    #cut_text = " ".join(cut_text)
    
    mask = np.array(Image.open("mask.png"))
    wc = WordCloud(mask = mask, max_words = 100, width = 2000, height = 2000, background_color = "Black")
    wordcloud = wc.generate(cut_text)

    image_color = ImageColorGenerator(mask)
    wc.recolor(color_func = image_color)
    
    wordcloud.to_file("wordcloud.jpg")
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


def main():
    dataset = pd.read_csv("Market_Basket_Optimisation.csv", header = None)
    #print(dataset)
    #dataset.to_csv("collect.csv")
    
    
    # Condition1
    data = ""
    datalist = []
    for i in range(0, dataset.shape[0]):
        for j in range(0, dataset.shape[1]):
            if str(dataset.values[i, j]) != "nan":
                data += str(dataset.values[i, j])
                data += " "
                datalist.append(str(dataset.values[i, j]))
    
    create_visual_show(datalist)
    
    '''
    # Condition2
    data = []
    for i in range(0, dataset.shape[0]):
        for j in range(0, dataset.shape[1]):
            if str(dataset.values[i, j]) != "nan":
                data.append(str(dataset.values[i, j]))
                
    '''
    #print(data)
    
    create_word_cloud(data)
    
if __name__ == '__main__':
    main()

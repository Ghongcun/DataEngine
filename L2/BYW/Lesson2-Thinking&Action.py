# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:38:40 2020

@author: buyewen
"""


import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
page_num = 10

# 请求URL
def getURLContent(url):
    # 得到页面的内容
    html = requests.get(url, headers = headers, timeout = 10)
    content = html.text
    
    # 通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding = 'utf-8')
    return soup

def analyzeContent(df, soup):
    temp = soup.find("div", class_="tslb_b")
    #print(temp)
    
    tr_list = temp.find_all("tr")
    #print(tr_list)
    
    for tr in tr_list:
        td_list = tr.find_all("td")
        #print(td_list)
        temp = {}
        if len(td_list) > 0:
            temp["投诉编号id"], temp["投诉品牌brand"], temp["投诉车系car_model"], temp["投诉车型type"],\
                temp["问题简述desc"], temp["典型问题problem"], temp["投诉时间datetime"], temp["投诉状态status"] =\
                    td_list[0].text, td_list[1].text, td_list[2].text, td_list[3].text,\
                        td_list[4].text, td_list[5].text, td_list[6].text, td_list[7].text
            df = df.append(temp, ignore_index = True)
    
    #print(df)
    return df


df = pd.DataFrame(columns = ["投诉编号id", "投诉品牌brand", "投诉车系car_model", "投诉车型type",\
                                 "问题简述desc", "典型问题problem", "投诉时间datetime", "投诉状态status"])
for i in range(page_num):
    request_url = base_url + str(i + 1) + ".shtml"
    soup = getURLContent(request_url)
    df = analyzeContent(df, soup)

#print(df)
df.to_excel("12365auto.xlsx", index = False)

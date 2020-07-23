# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 17:52:38 2020

@author: buyewen
"""

import pandas as pd

train = pd.read_csv("train.csv")
#print(train)

train["Datetime"] = pd.to_datetime(train.Datetime, format = "%d-%m-%Y %H:%M")
train.index = train.Datetime
#print(train)

train.drop(["ID", "Datetime"], axis = 1, inplace = True)
#print(train)

daily_train = train.resample("D").sum()
#print(daily_train)

daily_train["ds"] = daily_train.index
daily_train["y"] = daily_train.Count
#print(daily_train)

daily_train.drop(["Count"], axis = 1, inplace = True)
#print(daily_train)

from fbprophet import Prophet

m = Prophet(yearly_seasonality = True, seasonality_prior_scale = 0.1)
m.fit(daily_train)
future = m.make_future_dataframe(periods = 213)

forecast = m.predict(future)
print(forecast)

m.plot(forecast)
m.plot_components(forecast)
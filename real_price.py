#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np
import tushare as ts
#import talib
import matplotlib.pyplot as plt
from pylab import mpl



def Convert(df):
    #x = df.index
    y = df.price.values
    #x = [p.encode('unicode-escape').decode('string_escape') for p in x]
    #y = [p.encode('unicode-escape').decode('string_escape') for p in y]#转换成str
    y = [float(p) for p in y]#转化成float
    #df.index = x
    df['price'] = y
    return df


plt.ion()
#plt.figure(1)
fig,ax = plt.subplots()
real = pd.DataFrame()
length_time = 200
stock_code = '600519'

stock = ts.get_hist_data(stock_code)
close = stock['close'].values[0]

plt.hlines(close,0,length_time)
mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']

#color = 'blue'

for i in range(length_time):
    df = ts.get_realtime_quotes(stock_code)
    df = df[['code','name','time','price']]
    name = df['name'].values[0]
    #df = df.set_index('time')
    df_co = Convert(df)
    real = real.append(df_co)
    price = real['price'].values
    
    dy = 1.2*max(abs(p-close) for p in price)
    y_low = close-dy
    y_uper = close+dy
    #设置标题颜色，大于昨日收盘价就红色
    if price[-1]>close:
    	color = 'red'
    else:
    	color = 'green'

    ax.lines = []
    ax.plot(price,'b')
    #ax.hline(close)
    ax.set_xlim(0,length_time)
    ax.set_ylim(y_low,y_uper)
    ax.set_title('%s %.2f' %(name,round(price[-1],2)),color=color)
    plt.draw()
    plt.pause(5)


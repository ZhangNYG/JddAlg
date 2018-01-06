#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

salesSum = pd.read_csv(r'../DATA/Droped_t_sales_sum.csv', low_memory=False)
salesSum = salesSum[salesSum.sale_amt_3m >= 0]
print(salesSum.head(10))

tOrder = pd.read_csv(r'../DATA/t_order.csv',low_memory=False)
tOrder = tOrder[tOrder.sale_amt >= 0]
print(tOrder.head(10))

tOrder['datetime'] = pd.to_datetime(tOrder['ord_dt'])
saleWeekOrder = tOrder.groupby('shop_id').resample('1W',on='datetime').sum()
del saleWeekOrder['shop_id']
print(saleWeekOrder.head(10))
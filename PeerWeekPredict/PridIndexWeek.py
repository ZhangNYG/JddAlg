
# coding: utf-8

# In[1]:


#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

tOrder = pd.read_csv(r'../DATA/t_order.csv',low_memory=False)
tOrder = tOrder[tOrder.sale_amt >= 0]
#print(tOrder.head(10))
tOrder['datetime'] = pd.to_datetime(tOrder['ord_dt'])
saleSumOnlyDateAndAmt = tOrder[['shop_id','datetime','sale_amt']]
print(saleSumOnlyDateAndAmt.head(10))


# In[2]:


groupSaleByShop = saleSumOnlyDateAndAmt.groupby('shop_id').resample('1W',on='datetime',label='left').sum()

del groupSaleByShop['shop_id']

groupSaleByShop = groupSaleByShop.reset_index()
print(groupSaleByShop.head(30))


# In[3]:


baiduIndex = pd.read_csv(r'../DATA/BaiDuIn.csv', low_memory=False)
baiduIndex['datetime'] = pd.to_datetime(baiduIndex['datetime'])
print(baiduIndex.head(10))


# In[4]:


baiduIndex = baiduIndex[(baiduIndex['datetime']>='2016-08-07')&(baiduIndex['datetime']<='2017-04-16')]
print(baiduIndex)


# In[5]:




# In[6]:


baiduIndex = baiduIndex.drop(['alldev'], axis=1)
baiduIndex =baiduIndex.reset_index()
print(baiduIndex)


# In[7]:


groupSaleByShop = groupSaleByShop[(groupSaleByShop['datetime']>='2016-08-07')&(groupSaleByShop['datetime'] <= '2017-04-16')]
print(groupSaleByShop.head(50))


# In[8]:


baiduIndex = baiduIndex.drop(['index'], axis=1)
print(baiduIndex)
#     datetime  iphone  computer
#0  2016-08-07  140994    236530
#1  2016-08-14  139847    237085
#2  2016-08-21  137562    232730
#3  2016-08-28  136249    237919

# In[9]:


groupSaleByShop=groupSaleByShop.reset_index()
#    index  shop_id   datetime  sale_amt
#0            1        1 2016-08-07   4462.63
#1            2        1 2016-08-14   3525.99
#2            3        1 2016-08-21   2398.56

# In[10]:


print(groupSaleByShop)


# In[11]:


groupSaleByShop = groupSaleByShop.drop(['index'], axis=1)
print(groupSaleByShop)

label_data = groupSaleByShop[groupSaleByShop['shop_id'] == 1]['sale_amt']
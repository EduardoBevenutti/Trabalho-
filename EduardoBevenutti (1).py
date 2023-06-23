#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
dados = pd.read_csv('spotify_weather_data.csv')
dados


# In[16]:


dados.Weather.unique()


# In[19]:


import matplotlib.pyplot as plt

test = dados.groupby('Weather')['Popularity'].mean()
test.plot(kind='bar')
# dados.plot(x='Weather', y='Popularity', kind='bar')


# In[ ]:





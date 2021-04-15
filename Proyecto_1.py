#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px 

data = pd.read_csv("https://egauge50670.egaug.es/5D1CF/cgi-bin/egauge-show?c")
#data = pd.read_csv("https://egauge50670.egaug.es/5D1CF/cgi-bin/egauge?inst&tot")

data = data.rename(columns = {'Date & Time':'Fecha y Hora','Usage [kWh]':'Uso [kWh]'})

print(data.head())
#print(data)


# In[2]:


fig = px.scatter(data.head(10), x = 'Fecha y Hora', y =  'Uso [kWh]',
                 size= 'Uso [kWh]', color = 'Fecha y Hora' ,size_max = 60)

print(fig.update_layout())


# In[ ]:





# In[ ]:





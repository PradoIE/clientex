# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 23:26:59 2021

@author: alonso
"""

import pandas as pd
import numpy as np
import plotly.express as px 

data = pd.read_csv("https://egauge50670.egaug.es/5D1CF/cgi-bin/egauge-show?c")

data = data.rename(columns = {'Date & Time':'Fecha y Hora','Usage [kWh]':'Uso [kWh]'})

#print(data.head())

fig = px.scatter(data.head(10), x = 'Fecha y Hora', y =  'Uso [kWh]',
                 size= 'Uso [kWh]', color = 'Fecha y Hora' ,size_max = 60)

fig.update_layout()

#print(fig)
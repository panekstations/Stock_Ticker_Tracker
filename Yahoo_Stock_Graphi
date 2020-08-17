import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

#style.use('bmh')

#start = dt.datetime(2020,1,15)
#end = dt.datetime(2020,1,22)
source = 'yahoo'

thing = ['DIS','JPM','BLK','JHG','MS','MSFT']

df = web.DataReader(thing,source,start,end)
df.Close.plot(figsize=(16, 8),label=thing, legend=True)
plt.show()

'''

you should write a Python script that reads and analyses the ice cream data file (Weekly_Sales.csv) and merge it with the store details file (StoreDetails.csv) and region file (Region.csv) to produce at least FOUR useful graphs that
give insight into the ice cream sales trends. For example, here are some suggestions:

• show the change in ice cream sales over the period 2010 to 2012
• compare the trends of all stores in a given year.
• compare sales against the different store details (i.e. temperature and unemployment) to see what the relationship between them is (data from StoreDetails.csv).
• compare sales in the five different regions (using the data from the Region.csv to group the stores)



'''

import pandas as pd
weeklysales=pd.read_csv("f:/Agilisium_python-master/Weekly_Sales.csv")
storedetails=pd.read_csv("f:/Agilisium_python-master/StoreDetails.csv")
region=pd.read_csv("f:/Agilisium_python-master/Region.csv")

'''
compare sales in the five different regions (using the data from the Region.csv to group the stores)


'''

merge=pd.merge(storedetails,region)
region=pd.merge(merge,weeklysales)
df_region = region[["Region", "Store"]]
df_region.groupby("Region").sum().plot(kind="bar")


'''
compare sales against the different store details (i.e. temperature and unemployment) to see what the relationship between them is (data from StoreDetails.csv).
'''

x=pd.merge(weeklysales,storedetails)
sales=pd.merge(x,region)
sales.head()
df_sales = sales[["Temperature","Unemployment", "Store"]]
df_sales.groupby("Store").sum().plot(kind="bar")


'''
how the change in ice cream sales over the period 2010 to 2012
• compare the trends of all stores in a given year.

'''

sales['DateinYear'] = pd.DatetimeIndex(sales['Date']).year
df_change = sales[["Weekly_Sales",'DateinYear']]
df_change.groupby("DateinYear").sum().plot(kind="bar")

import numpy as np
import pandas as pd



data = pd.read_csv(r"C:\Users\Suleman Farooqi\Downloads\Adops & Data Scientist Sample Data - Q1 Analytics.csv")




# question 1
data_1 = data[data['country_id']=='BDV']
data_1 = data_1.groupby('site_id')['user_id'].nunique()
#from inspection - it seems that there are 13 users who were visited more than one site

# question 2
data_2 = data.copy()
data_2['ts'] = pd.to_datetime(data_2['ts'], format='%Y-%m-%d')
data_2 = data_2[(data_2['ts'] > '2019-02-03') & (data_2['ts'] < '2019-02-05')]
data_2 = data_2.groupby(['site_id','user_id']).size().reset_index()

# question 3
data_3 = data.copy()
data_3.sort_values('ts', inplace=True)
data_3 = data_3.groupby('user_id').tail(1)
data_3= data_3.groupby('site_id')['user_id'].nunique().reset_index()

# question 4
data_4 = data.copy()
data_4.sort_values('ts', inplace=True)
last_visit = data_4.groupby('user_id').tail(1)[['user_id', 'site_id']]
first_visit = data_4.groupby('user_id').head(1)[['user_id', 'site_id']]
data_4 = pd.merge(last_visit, first_visit, how = 'left', left_on = 'user_id', right_on='user_id' )
data_4 = data_4[data_4['site_id_x'] == data_4['site_id_y']]

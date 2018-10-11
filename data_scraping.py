# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 13:17:51 2018

@author: Yunsun2
"""

#(1) 
import requests, zipfile, io
zip_file_url="http://api.worldbank.org/v2/en/indicator/SH.STA.ACSN?downloadformat=csv&source=2"
r = requests.get(zip_file_url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

#(2) 
import pandas as pd
df=pd.read_csv('API_SH.STA.ACSN_DS57_en_csv_v2_9953350.csv', skiprows=4)
df=df[df['Country Code'].apply(lambda x: x in ['HIC', 'MIC', 'LIC', 'WLD'])]
df.drop(['Indicator Name',	'Indicator Code', 'Country Code'], axis=1, inplace=True)    
df=df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1)
df=df.set_index('Country Name').transpose()
df['Year'] = df.index

#(3) 
import matplotlib.pyplot as plt
#%matplotlib inline
plt.show()
df.plot(figsize=(7, 5), title='Access to Sanitation Facilities Over Time (1959-2017)', 
        grid=2, fontsize=10, sort_columns=True, mark_right=True)


print("*** Conclusions")
print("* Data is not available until around 1990;"+'\n'+ "* World wide (red line), the access to sanitation facilities maintain a slight uptrend from around 1990-2010;"
     + '\n' + "* From around 2010 onwards, there's a sharp descrease on the access to sanitation facilities;" +'\n'+ 
      "* This trend applies to all income groups;" + '\n' + "* However, the access gap between high income group and middle income is much larter than that of middle and low." + '\n')

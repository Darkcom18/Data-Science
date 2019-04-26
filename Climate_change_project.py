# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26:43:16 2019

@author: PHAM Quoc Trng
"""
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import t
import matplotlib.pyplot as plt
#Read the file
inFile = "climate.xlsx"
df = pd.read_excel(inFile,na_values='-')
#Data analyze
#Store some value used
Year = df['Year'].values
AveTemp = df['T'].values
MaxTemp = df['TM'].values
MinTemp = df['Tm'].values
AmountRnS = df['PP'].values
Rainday = df['RA'].values
#Plot to see how average temperature changed through years
x = range(len(Year))
plt.plot(x,AveTemp)
plt.xticks(x,Year,rotation = 45)
plt.show()
#Plot to see the distribution temperature
plt.hist(AveTemp)
plt.show()
#Describe to see the difference between Max temperature and Min temperature
print(df[['TM','Tm']].describe())
df[['TM','Tm']].boxplot()
plt.show()
#Plot the map to see the relationship between Max temperature and the amountof rain and snow
fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('Max Temperature', color=color)
ax1.plot(Year, MaxTemp, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx() 
color = 'tab:blue'
ax2.set_ylabel('Amount of Rain or snow', color=color)
ax2.plot(Year, AmountRnS, color=color)  
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()  
plt.show()
#Hypotest
normality_avetemp= stats.normaltest(AveTemp,nan_policy='omit')
print('The normality of average temperature data s:\nt-value = {:4.3f} \np-value = {:4.3f}'.format(normality_avetemp[0],normality_avetemp[1]))
confidence = 0.95
n = len(AveTemp)
m = np.nanmean(AveTemp)
std_err = np.nanstd(AveTemp)
h = std_err * t.ppf((1 + confidence) / 2, n - 1)
print('The value of confidence interval is {:4.3f}: ',h)
#Bonus check the relavance of 2 data group
RelTest = stats.ttest_rel(MaxTemp,AmountRnS,nan_policy='omit')
print('The normality of average temperature data s:\nt-value = {:4.3f} \np-value = {:4.35f}'.format(RelTest[0],RelTest[1]))

 


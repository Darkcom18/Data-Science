# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 07:52:27 2019

Issue: Nowadays, the accidents increase. It caused worse consequencies to all drivers and families
The accidents happend by some reasons.

The data below is collect form github https://github.com/fivethirtyeight/data/tree/master/bad-drivers
with resource of data.
In the data, we can see there are  2 main reasons: by speeding and by alcohol.
The data also shows the experience of the driver in the fatal accidents that whether they are distracted or involved in any previous accidents
We also can see how the insurance involved in those accidents

@author: DarkCoM
"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt
from scipy.stats import t

inFile = "bad-driver.xlsx"
df = pd.read_excel(inFile)
df1 = df.rename(index=str, columns={"Number of drivers involved in fatal collisions per billion miles":"Death per bil miles","Percentage Of Drivers Involved In Fatal Collisions Who Were Speeding": "Speeding", "Percentage Of Drivers Involved In Fatal Collisions Who Were Alcohol-Impaired": "Alcohol","Percentage Of Drivers Involved In Fatal Collisions Who Were Not Distracted":"Not distracted","Percentage Of Drivers Involved In Fatal Collisions Who Had Not Been Involved In Any Previous Accidents":"Not involved","Car Insurance Premiums ($)":"Insurance","Losses incurred by insurance companies for collisions per insured driver ($)":"Losses incurred"})
#Here I changed the names of column since it s too long to recopy again

states = df['State'].values
percent_death = df1['Death per bil miles'].values
percent_speeding = df1['Speeding'].values
percent_alcohol =  df1['Alcohol'].values
percent_notdistracted = df1['Not distracted'].values
percent_noaccidentbefore = df1['Not involved'].values
percent_insurance = df1['Insurance'].values
percent_lossincurred = df1['Losses incurred'].values
#store value in the array numpy

x = range(len(states))
plt.plot(x,percent_death)
plt.xticks(x,states,rotation = 90)
plt.savefig('states by death.png')
plt.show()
'''re I plot a image show the states and their death respectly.
 Some states with very low  death are District of Columbia, Massachusetts, Minnesota
 Some states with very high  death are South Carolina, North Dakota, West Virginia
'''

plt.hist(percent_death)
plt.show()

print(df1[['Speeding','Alcohol']].describe())
print(df1[['Not distracted','Not involved']].describe())
print(df1[['Insurance','Losses incurred']].describe())

df1[['Speeding','Alcohol']].boxplot()
plt.show()
'''
Here you will see the graph that the mean value between them are very mall, just 1 case
But the Max of death cause by speeding is higher than alcohol
'''
df1[['Not distracted','Not involved']].boxplot()
plt.show()
'''
Mean value not so different, but the std is very high difference
'''
df1[['Insurance','Losses incurred']].boxplot()
plt.show()
'''
For this one, I dont really know how to say.
'''

'''
Here is part 3
For the test, we just need to make one hypothesis test, So I choose death by speeding and alcohole
They are independent group. So I do a independent t test
'''
# Test the Normality
normality_speed = stats.normaltest(percent_speeding)
normality_alcohol = stats.normaltest(percent_alcohol)
print('The results of the Normality of speeding data are: \n\tt-value = {:4.3f}\n\tp-value = {:4.3f}'.format(normality_speed[0],normality_speed[1]))
print('The results of the Normality of alcohol data are: \n\tt-value = {:4.3f}\n\tp-value = {:4.3f}'.format(normality_alcohol[0],normality_alcohol[1]))

#Conduct t-test between 2 independent groups. Here I chose the reason, if u want to test more, just retype the name
ind_t_test = stats.ttest_ind(percent_speeding, percent_alcohol) 

std_speeding = percent_speeding.std()
std_alcohol = percent_alcohol.std()
mean_speeding = percent_speeding.mean() 
mean_alcohol = percent_alcohol.mean()
N1 = 51
N2 = 51
df = (N1 + N2 - 2)
std_N1N2 = sqrt( ((N1 - 1)*(std_speeding)**2 + (N2 - 1)*(std_alcohol)**2) / df) 
diff_mean = mean_speeding  - mean_alcohol
MoE = t.ppf(0.975, df) * std_N1N2 * sqrt(1/N1 + 1/N2)

print('The results of the independent t-test are: \n\tt-value = {:4.3f}\n\tp-value = {:4.3f}'.format(ind_t_test[0],ind_t_test[1]))
print ('\nThe difference between groups is {:3.1f} [{:3.1f} to {:3.1f}] (mean [95% CI])'.format(diff_mean, diff_mean - MoE, diff_mean + MoE))

'''Bonus compare 2 groups with respect to each other; I chose insurance and losses incurred insurance 
Since we suppose that the higher insurance pay, the higher loss for the insurrance company
'''
res_t_test = stats.ttest_rel(percent_insurance,percent_lossincurred)
print('The results of the dependent t-test are: \n\tt-value = {:4.3f}\n\tp-value = {:4.3f}'.format(res_t_test[0],res_t_test[1]))
'''
But the result show that p = 0, I think there is no relationship; but we can say our suppose is wrong :D
'''


# the histogram of the data




# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:40:29 2019

@author: DELL
"""
#importing libraries


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reading dataset using pandas
df = pd.read_csv('C:\\Users\\DELL\\Desktop\\dataset\\train.csv')

#printing first 5 values of the dataset
df.head(10)

##summary of the dataset
df.describe()

#information of dataset
df.info()

#plotting the applicantincom using histogram
df['ApplicantIncome'].hist(bins=50)

df.boxplot(column='ApplicantIncome', by = 'Education')

df['LoanAmount'].hist(bins=50)

#Categorical variable analysis
temp1 = df['Credit_History'].value_counts(ascending=True)
temp2 = df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x: x.map({'Y':1,'N':0}).mean())
print ('Frequency Table for Credit History:') 
print (temp1)

print ('\nProbility of getting loan for each Credit History class:')
print (temp2)

#probability of getting loan on credit history
H = df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x: x.map({'Y':1,'N':0}).mean())
H

fig = plt.figure(figsize=(8,4))
x1 = fig.add_subplot(121)
x1.set_xlabel('Credit_History')
x1.set_ylabel('Count of Applicants')
x1.set_title("Applicants by Credit_History")
temp1.plot(kind='bar')

x2 = fig.add_subplot(122)
temp2.plot(kind = 'bar')
x2.set_xlabel('Credit_History')
x2.set_ylabel('Probability of getting loan')
x2.set_title("Probability of getting loan by credit history")

#probability of getting loan having valid credit history
temp3 = pd.crosstab(df['Credit_History'], df['Loan_Status'])
temp3.plot(kind='bar', stacked=True, color=['red','blue'], grid=False)

#probability of getting loan for male and female
pv = df.pivot_table(values='Gender',index=['Credit_History'],aggfunc=lambda x: x.map({'Female':1,'Male':0}).mean())
pv
chart = pd.crosstab(df['Credit_History'], df['Loan_Status'])
chart.plot(kind='bar', stacked=True, color=['red','yellow'], grid=False)
chart = pd.crosstab(df['Gender'], df['Loan_Status'])
chart.plot(kind='bar', stacked=True, color=['red','yellow'], grid=False)








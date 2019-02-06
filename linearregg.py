# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 22:29:22 2019

@author: DELL
"""
#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the dataset
df = pd.read_csv('Salary_Data.csv')
x = df.iloc[:,:-1].values
y = df.iloc[:,:1].values

#spliting the dataset into training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)

#fitting simple lenear reggresion to train set
from sklearn.linear_model import LinearRegression
regg = LinearRegression()
regg.fit(X_train, y_train)

#predicting the test result
y_predict = regg.predict(X_test) 

#visualizing the training set
plt.scatter(X_train, y_train, color= 'red')
plt.plot(X_train, regg.predict(X_train), color= 'blue')
plt.title('salary vs experience(training set)')
plt.xlabel('years of experience')
plt.ylabel('salary')
plt.show()

#visualizing the test set
plt.scatter(X_test, y_test, color= 'red')
plt.plot(X_test, regg.predict(X_train), color= 'blue')
plt.title('salary vs experience(test set)')
plt.xlabel('years of experience')
plt.ylabel('salary')
plt.show()






# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np #Numerical Computing
import pandas as pd #Data processing
import matplotlib.pyplot as plt #Visualization
import seaborn as sns #Modern Visualization

#theme set for seaborn(sns) plots
sns.set_style("darkgrid")

#define the size for plot figures
plt.rcParams['figure.figsize'] = (14,8)

#file_path ='C:\\Users\\sudhi\\Desktop'
matches=pd.read_csv('matches.csv')
print(matches)

#information bout datatype
matches.info()

#describe the table
z=matches.describe()

#couple of actual rows of input dataset
r=matches.head(2)

#maximum number of matches
print(matches['id'].max())

# unique set of match year
u=matches['season'].unique()

#List of years
print(len(matches['season'].unique()))

#Team won by maximum runs
#Here idxmax return the id of the maximumth value which is fed in the iloc.
maxruns = matches.iloc[matches['win_by_runs'].idxmax()]

#Wining team in dataset by maximum runs
print(matches.iloc[matches['win_by_runs'].idxmax()]['winner'])

#Team won by Maximum Wickets
print(matches.iloc[matches['win_by_wickets'].idxmax()]['winner'])

#Team which won by (Closest margin) or minimun runs
print(matches.iloc[matches[matches['win_by_runs'].ge(1)].win_by_runs.idxmin()]['winner'])

#Team which had won by minimum wickets
print(matches.iloc[matches[matches['win_by_wickets'].ge(1)].win_by_wickets.idxmin()])

#DATA VISUALIZATION SECTION BEGINS

#Which season had most number of matches.
sns.countplot(x = 'season',data = matches)
plt.show()

#Most successful IPL Team
data = matches.winner.value_counts()
sns.barplot(y = data.index, x = data, orient='h');

#Top player of the match Winners
top_players = matches.player_of_match.value_counts()[:10]

fig, ax = plt.subplots()
ax.set_ylim([0,20])
ax.set_ylabel("Count")
ax.set_title("Top player of the match Winners")

sns.barplot(x = top_players.index, y = top_players, orient = 'v');
plt.show()

#Toss winning helped in Match-Winning
ss = matches['toss_winner'] == matches['winner']
print(ss.groupby(ss).size())

#Visualizing the result of toss wining and match winning
sns.countplot(matches['toss_winner'] == matches['winner'])
print(sns.countplot(ss))
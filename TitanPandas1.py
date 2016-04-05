# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 20:38:47 2016

@author: Katsenis Konstantinos

This script uses Pandas
"""

"""The gendermodel program converted to pandas"""

import pandas as pd
import numpy as np
import seaborn 
import matplotlib.pyplot  as plt

df=pd.read_csv("train.csv", header=0)
print
print "Number of people of the sample: ",len(df)
print "Number of variables: ",len(df.columns)
print
print "Our sample consists of:"
print df["Sex"].value_counts(sort=False)
print
print type(df["Sex"])
print
df["Sex"]=df["Sex"].astype("category")

print

df['Survived'] = pd.to_numeric(df['Survived'], errors='coerce')

seaborn.factorplot(x="Sex",y="Survived", data=df, kind="bar",ci=None)
plt.xlabel("Sex")
plt.ylabel("Proportion of survivors")
plt.title("Graph of Sex and Survived variables")
plt.show()

print "We can see that females have better chances of survival than males."
print "Let's calculate precisely these proportions."

females=df[ df["Sex"]=="female"]
males=df[ df["Sex"]=="male"]
femalessurvived=females[females["Survived"]==1]
malessurvived=males[males["Survived"]==1]
prop_females_survived=len(femalessurvived)/(len(females)*0.01)
prop_males_survived=len(malessurvived)/(len(males)*0.01)
print
print "The "+str(prop_females_survived)+" % of females and the "\
 +str(prop_males_survived)+" % of males survived."
 
print
print "So, our strategy is to consider that all females survived and all males died."
print
test = pd.read_csv('test.csv',index_col=[0])
test["Gender"]=test["Sex"].map({"female":1, "male":0}).astype(int)
test["Survived"]=test["Gender"]

test[['Survived']].to_csv('gendermodel-pandas.csv')
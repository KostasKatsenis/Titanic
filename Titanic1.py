# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 17:04:26 2016

@author: Katsenis Konstantinos
"""
#This script is about the genderbased model
import csv as csv
import numpy as np
train_file=open('train.csv','rb')
csv_file_object=csv.reader(train_file)

header = csv_file_object.next()
data=[]

for row in csv_file_object:    
    data.append(row)            
data = np.array(data)

number_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
proportion_survivors = number_survived / number_passengers
print
print "Titanic had a total of "+str(number_passengers)+ " passengers."\
 "Only "+str(number_survived)+" of them survived."\
 "That means that only the "+str(proportion_survivors*100)\
 +" % of the passengers survived."
print
women_only_stats = data[0::,4] == "female"
men_only_stats = data[0::,4] != "female"
# or men_only_stats_alternative = data[0::,4] == "male"

women_onboard = data[women_only_stats,1].astype(np.float)
men_onboard = data[men_only_stats,1].astype(np.float)

proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)

print 'Proportion of women who survived is '+str(proportion_women_survived*100)+' %.'
print 'Proportion of men who survived is '+str(proportion_men_survived*100)+' %.'
train_file.close()
print
print "My strategy is to consider that every woman survived and every man died."
test_file = open('test.csv', 'rb')
test_file_object = csv.reader(test_file)
header1 = test_file_object.next()

prediction_file = open("genderbasedmodel.csv", "wb")
prediction_file_object = csv.writer(prediction_file)

prediction_file_object.writerow(["PassengerId", "Survived"])
for row in test_file_object:
    if row[3] == 'female':
        prediction_file_object.writerow([row[0],'1'])
    else:
        prediction_file_object.writerow([row[0],'0'])
test_file.close()
prediction_file.close()


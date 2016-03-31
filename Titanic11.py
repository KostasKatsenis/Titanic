# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 02:14:47 2016

@author: Katsenis Konstantinos
"""
import csv as csv
import numpy as np
train_file=open('train.csv','rb')
csv_file_object=csv.reader(train_file)

header = csv_file_object.next()
data=[]

for row in csv_file_object:    
    data.append(row)            
data = np.array(data)
print
print header
print
males=data[0::,4]=="male"
data=data[males]
print np.size(data[0::,1])
print
print "----------------Embarked factor-----------------------------------"
print
Cherbourg=data[0::,11]=="C"
Queenstown=data[0::,11]=="Q"
Southampton=data[0::,11]=="S"
Cherbourgonboard=data[Cherbourg,1].astype(np.float)
Queenstownonboard=data[Queenstown,1].astype(np.float)
Southamptononboard=data[Southampton,1].astype(np.float)
proportion_Cherbourg=np.sum(Cherbourgonboard)/np.size(Cherbourgonboard)
proportion_Queenstown=np.sum(Queenstownonboard)/np.size(Queenstownonboard)
proportion_Southampton=np.sum(Southamptononboard)/np.size(Southamptononboard)
print
print "Proportion of passengers from Cherbourg is "+str(proportion_Cherbourg*100)+" %."
print np.size(Cherbourgonboard)
print "Proportion of passengers from Queenstown is "+str(proportion_Queenstown*100)+" %."
print np.size(Queenstownonboard)
print "Proportion of passengers from Southampton is "+str(proportion_Southampton*100)+" %."
print np.size(Southamptononboard)
print
print "Only 7.3% of men embarked from Queenstown survived. So, our first rule is that\
 all men from there died."
data=data[ data[0::,11]!="Q"]
print np.size(data[0::,1])
print
print "------------------Family factor-------------------------"
print
Family0=data[0::,6].astype(np.float)+data[0::,7].astype(np.float)==0
Family1=data[0::,6].astype(np.float)+data[0::,7].astype(np.float)==1
Family2=data[0::,6].astype(np.float)+data[0::,7].astype(np.float)==2
Family3=data[0::,6].astype(np.float)+data[0::,7].astype(np.float)==3
Family4=data[0::,6].astype(np.float)+data[0::,7].astype(np.float)==4
Family5=data[0::,6].astype(np.float)+data[0::,7].astype(np.float)==5
Family6=data[0::,6].astype(np.float)+data[0::,7].astype(np.float)==6
Family7=data[0::,6].astype(np.float)+data[0::,7].astype(np.float)==7
Family8=data[0::,6].astype(np.float)+data[0::,7].astype(np.float)==8
Family9=data[0::,6].astype(np.float)+data[0::,7].astype(np.float)==9
Family10=data[0::,6].astype(np.float)+data[0::,7].astype(np.float)==10
F0onboard=data[Family0,1].astype(np.float)
F1onboard=data[Family1,1].astype(np.float)
F2onboard=data[Family2,1].astype(np.float)
F3onboard=data[Family3,1].astype(np.float)
F4onboard=data[Family4,1].astype(np.float)
F5onboard=data[Family5,1].astype(np.float)
F6onboard=data[Family6,1].astype(np.float)
F7onboard=data[Family7,1].astype(np.float)
F8onboard=data[Family8,1].astype(np.float)
F9onboard=data[Family9,1].astype(np.float)
F10onboard=data[Family10,1].astype(np.float)
proportion_F0=np.sum(F0onboard)/np.size(F0onboard)
proportion_F1=np.sum(F1onboard)/np.size(F1onboard)
proportion_F2=np.sum(F2onboard)/np.size(F2onboard)
proportion_F3=np.sum(F3onboard)/np.size(F3onboard)
proportion_F4=np.sum(F4onboard)/np.size(F4onboard)
proportion_F5=np.sum(F5onboard)/np.size(F5onboard)
proportion_F6=np.sum(F6onboard)/np.size(F6onboard)
proportion_F7=np.sum(F7onboard)/np.size(F7onboard)
proportion_F8=np.sum(F8onboard)/np.size(F8onboard)
proportion_F9=np.sum(F9onboard)/np.size(F9onboard)
proportion_F10=np.sum(F10onboard)/np.size(F10onboard)
print proportion_F0,np.size(F0onboard)
print proportion_F1,np.size(F1onboard)
print proportion_F2,np.size(F2onboard)
print proportion_F3,np.size(F3onboard)
print proportion_F4,np.size(F4onboard)
print proportion_F5,np.size(F5onboard)
print proportion_F6,np.size(F6onboard)
print proportion_F7,np.size(F7onboard)
print proportion_F8,np.size(F8onboard)
print proportion_F9,np.size(F9onboard)
print proportion_F10 ,np.size(F10onboard)
print
print "Second rule is that all men with 4 or more family members died."
print
data=data[ data[0::,6].astype(np.float)+data[0::,7].astype(np.float)<4 ]
print np.size(data[0::,1])
print
print "----------------Age factor--------------------------"
print
data[ data[0::,5]=="",5] = "1000"
agebin0 = data[data[0::,5]=="1000",1].astype(np.float)
agebin1= data[data[0::,5].astype(np.float)<=15,1].astype(np.float)
agebin2= data[(data[0::,5].astype(np.float)>15)&(data[0::,5].astype(np.float)<=40),1].astype(np.float)
agebin3= data[(data[0::,5].astype(np.float)>40)&(data[0::,5].astype(np.float)<=60),1].astype(np.float)
agebin4= data[(data[0::,5].astype(np.float)>60)&(data[0::,5].astype(np.float)<=80),1].astype(np.float)
proportion_agebin0 = np.sum(agebin0) / np.size(agebin0)
proportion_agebin1 = np.sum(agebin1) / np.size(agebin1)
proportion_agebin2 = np.sum(agebin2) / np.size(agebin2)
proportion_agebin3 = np.sum(agebin3) / np.size(agebin3)
proportion_agebin4 = np.sum(agebin4) / np.size(agebin4)
print
print "Proportion of age nan is "+str(proportion_agebin0*100)+" %."
print np.size(agebin0)
print "Proportion of age 0-20 is "+str(proportion_agebin1*100)+" %."
print np.size(agebin1)
print "Proportion of age 20-40 is "+str(proportion_agebin2*100)+" %."
print np.size(agebin2)
print "Proportion of age 40-60 is "+str(proportion_agebin3*100)+" %."
print np.size(agebin3)
print "Proportion of age 60-80 is "+str(proportion_agebin4*100)+" %."
print np.size(agebin4)
print "Third rule is that men below 15 years old survived."

train_file.close()
print
print "My strategy is to consider that every woman survived and every man died."
test_file = open('test.csv', 'rb')
test_file_object = csv.reader(test_file)
header1 = test_file_object.next()

prediction_file = open("myninthmodel.csv", "wb")
prediction_file_object = csv.writer(prediction_file)

prediction_file_object.writerow(["PassengerId", "Survived"])
for row in test_file_object:
    if row[4]=="":
        row[4]="1000"
    if row[3] == 'female':
        prediction_file_object.writerow([row[0],'1'])
    elif row[3] == "male" and float(row[4])<=15 and row[10]!="Q" and float(row[5])+float(row[6])<4:
        prediction_file_object.writerow([row[0],'1'])
    else:
        prediction_file_object.writerow([row[0],'0'])
test_file.close()
prediction_file.close()
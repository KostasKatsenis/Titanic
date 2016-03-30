# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 13:52:24 2016

@author: Katsenis Konstantinos
"""
#Trying to improve my childish linear model
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
print "---------------Sex factor---------------------------"
print
females=data[0::,4]=="female"
males=data[0::,4]=="male"

femalesonboard=data[females,1].astype(np.float)
malesonboard=data[males,1].astype(np.float)

proportion_females=np.sum(femalesonboard)/np.size(femalesonboard)
proportion_males=np.sum(malesonboard)/np.size(malesonboard)
print
print "Proportion of females is "+str(proportion_females*100)+" %."
print "Proportion of males is "+str(proportion_males*100)+" %."
print np.size(femalesonboard),np.size(malesonboard)
data=data[females]
print
print "---------------Pclass factor---------------------"
pclass1=data[0::,2]=="1"
pclass2=data[0::,2]=="2"
pclass3=data[0::,2]=="3"

pclass1onboard=data[pclass1,1].astype(np.float)
pclass2onboard=data[pclass2,1].astype(np.float)
pclass3onboard=data[pclass3,1].astype(np.float)

proportion_pclass1=np.sum(pclass1onboard)/np.size(pclass1onboard)
proportion_pclass2=np.sum(pclass2onboard)/np.size(pclass2onboard)
proportion_pclass3=np.sum(pclass3onboard)/np.size(pclass3onboard)
print "Proportion of pclass1 is "+str(proportion_pclass1*100)+" %."
print "Proportion of pclass2 is "+str(proportion_pclass2*100)+" %."
print "Proportion of pclass3 is "+str(proportion_pclass3*100)+" %."
print
print "----------------Age factor--------------------------"
print
print "Now, let's examine what happens with the Age factor."
print
print "Our biggest concern is how we will bin up our data."
print
data[ data[0::,5]=="",5] = "1000"
agebin1= data[data[0::,5].astype(np.float)<=20,1].astype(np.float)
agebin2= data[(data[0::,5].astype(np.float)>20)&(data[0::,5].astype(np.float)<=60),1].astype(np.float)
agebin3= data[data[0::,5].astype(np.float)>60,1].astype(np.float)
proportion_agebin1 = np.sum(agebin1) / np.size(agebin1)
proportion_agebin2 = np.sum(agebin2) / np.size(agebin2)
proportion_agebin3 = np.sum(agebin3) / np.size(agebin3)
print
print "Proportion of age 0-20 is "+str(proportion_agebin1*100)+" %."
print
print "Proportion of age 20-60 is "+str(proportion_agebin2*100)+" %."
print
print "Proportion of age 60+ and nan is "+str(proportion_agebin3*100)+" %."
print
print "--------------------SibSp factor----------------------"
print
print np.unique(data[0::,6])
sib0=data[0::,6]=="0"
sib1=data[0::,6]=="1"
sib2=data[0::,6]=="2"
sib3=data[0::,6].astype(np.float)>=3
sib0onboard=data[sib0,1].astype(np.float)
sib1onboard=data[sib1,1].astype(np.float)
sib2onboard=data[sib2,1].astype(np.float)
sib3onboard=data[sib3,1].astype(np.float)
proportion_sib0=np.sum(sib0onboard)/np.size(sib0onboard)
proportion_sib1=np.sum(sib1onboard)/np.size(sib1onboard)
proportion_sib2=np.sum(sib2onboard)/np.size(sib2onboard)
proportion_sib3=np.sum(sib3onboard)/np.size(sib3onboard)
print
print "Proportion of sib=0 is "+str(proportion_sib0*100)+" %."
print
print "Proportion of sib=1 is "+str(proportion_sib1*100)+" %."
print
print "Proportion of sib=2 is "+str(proportion_sib2*100)+" %."
print
print "Proportion of sib=3 is "+str(proportion_sib3*100)+" %."
print 
print "-------------------Parch-----------------------"
print 
parch0=data[0::,7]=="0"
parch1=data[0::,7]=="1"
parch2=data[0::,7]=="2"
parch3=data[0::,7]=="3"
parch4=data[0::,7].astype(np.float)>=4
parch0onboard=data[parch0,1].astype(np.float)
parch1onboard=data[parch1,1].astype(np.float)
parch2onboard=data[parch2,1].astype(np.float)
parch3onboard=data[parch3,1].astype(np.float)
parch4onboard=data[parch4,1].astype(np.float)
proportion_parch0=np.sum(parch0onboard)/np.size(parch0onboard)
proportion_parch1=np.sum(parch1onboard)/np.size(parch1onboard)
proportion_parch2=np.sum(parch2onboard)/np.size(parch2onboard)
proportion_parch3=np.sum(parch3onboard)/np.size(parch3onboard)
proportion_parch4=np.sum(parch4onboard)/np.size(parch4onboard)
print
print "Proportion of parch=0 is "+str(proportion_parch0*100)+" %."
print
print "Proportion of parch=1 is "+str(proportion_parch1*100)+" %."
print
print "Proportion of parch=2 is "+str(proportion_parch2*100)+" %."
print
print "Proportion of parch=3 is "+str(proportion_parch3*100)+" %."
print
print "Proportion of parch>=4 is "+str(proportion_parch4*100)+" %."
print
print "-----------------Fare factor--------------------"
print
ticketbin1= data[data[0::,9].astype(np.float)<=10,1].astype(np.float)
ticketbin2= data[(data[0::,9].astype(np.float)>10)&(data[0::,9].astype(np.float)<=20),1].astype(np.float)
ticketbin3= data[(data[0::,9].astype(np.float)>20)&(data[0::,9].astype(np.float)<=30),1].astype(np.float)
ticketbin4= data[data[0::,9].astype(np.float)>30,1].astype(np.float)
proportion_ticketbin1 = np.sum(ticketbin1) / np.size(ticketbin1)
proportion_ticketbin2 = np.sum(ticketbin2) / np.size(ticketbin2)
proportion_ticketbin3 = np.sum(ticketbin3) / np.size(ticketbin3)
proportion_ticketbin4 = np.sum(ticketbin4) / np.size(ticketbin4)
print
print "Proportion of ticket 0-10 is "+str(proportion_ticketbin1*100)+" %."
print
print "Proportion of ticket 10-20 is "+str(proportion_ticketbin2*100)+" %."
print
print "Proportion of ticket 20-30 is "+str(proportion_ticketbin3*100)+" %."
print
print "Proportion of ticket 30-max is "+str(proportion_ticketbin4*100)+" %."
print
print "------------------Cabin factor---------------------------------"
print
print "The only way I can manage the cabin factor for the moment, is to see if \
 the passengers have a cabin or not"
print
nocabin=data[0::,10]==""
cabin=data[0::,10]!=""
nocabinonboard=data[nocabin,1].astype(np.float)
cabinonboard=data[cabin,1].astype(np.float)
proportion_nocabin=np.sum(nocabinonboard)/np.size(nocabinonboard)
proportion_cabin=np.sum(cabinonboard)/np.size(cabinonboard)
print
print "Proportion of nocabin passengers is "+str(proportion_nocabin*100)+" %."
print "Proportion of cabin passengers is "+str(proportion_cabin*100)+" %."
print
print "----------------Embarked factor-----------------------------------"
print
print "The last factor to examine is Embarked."
print
Cherbourg=data[0::,11]=="C"
Queenstown=data[0::,11]=="Q"
Southampton=data[0::,11]=="S"
Unknown=data[0::,11]==""
Cherbourgonboard=data[Cherbourg,1].astype(np.float)
Queenstownonboard=data[Queenstown,1].astype(np.float)
Southamptononboard=data[Southampton,1].astype(np.float)
Unknownonboard=data[Unknown,1].astype(np.float)
proportion_Cherbourg=np.sum(Cherbourgonboard)/np.size(Cherbourgonboard)
proportion_Queenstown=np.sum(Queenstownonboard)/np.size(Queenstownonboard)
proportion_Southampton=np.sum(Southamptononboard)/np.size(Southamptononboard)
proportion_Unknown=np.sum(Unknownonboard)/np.size(Unknownonboard)
print
print "Proportion of passengers from Cherbourg is "+str(proportion_Cherbourg*100)+" %."
print "Proportion of passengers from Queenstown is "+str(proportion_Queenstown*100)+" %."
print "Proportion of passengers from Southampton is "+str(proportion_Southampton*100)+" %."
print "Proportion of passengers from unknown is "+str(proportion_Unknown*100)+" %."
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
print proportion_F0
print proportion_F1
print proportion_F2
print proportion_F3
print proportion_F4
print proportion_F5
print proportion_F6
print proportion_F7
print proportion_F8
print proportion_F9
print proportion_F10 
print "Now we will construct our model for prediction."

def pclass(row):
    a=0
    if float(row[2])<=2:
        a=100
    elif float(row[2])==3:
        a=50
    return a


def family(row):
    a=0
    if float(row[6])+float(row[7])<4:
        a=80
    else:
        a=0
    return a

def cabin(row):
    a=0
    if row[10]=="":
        a=65
    else:
        a=100
    return a


for row in data:
     row[3]=pclass(row)+family(row)+cabin(row)
     print row[1],row[3],pclass(row),family(row),cabin(row)


print "Now I will examine the scores."
bin1= data[data[0::,3].astype(np.float)<=190,1].astype(np.float)
bin2= data[data[0::,3].astype(np.float)>190,1].astype(np.float)
proportion_bin1 = np.sum(bin1) / np.size(bin1)
proportion_bin2 = np.sum(bin2) / np.size(bin2)
print
print "Proportion of score 0-350 is "+str(proportion_bin1*100)+" %."
print np.size(bin1)
print "Proportion of score 350+ is "+str(proportion_bin2*100)+" %."
print np.size(bin2)

print np.sum(data[0::,1].astype(np.float)),np.size(data[0::,1])


train_file.close()
print

test_file = open('test.csv', 'rb')
test_file_object = csv.reader(test_file)
header1 = test_file_object.next()

prediction_file = open("myeigthmodel.csv", "wb")
prediction_file_object = csv.writer(prediction_file)
#FUNCTIONS
def pclass1(row):
    a=0
    if float(row[1])<=2:
        a=100
    elif float(row[1])==3:
        a=50
    return a


def family1(row):
    a=0
    if float(row[5])+float(row[6])<4:
        a=80
    else:
        a=0
    return a

def cabin1(row):
    a=0
    if row[9]=="":
        a=65
    else:
        a=100
    return a

prediction_file_object.writerow(["PassengerId", "Survived"])
for row in test_file_object:
    if row[3] == 'female'and pclass1(row)+family1(row)+cabin1(row)>190:
        prediction_file_object.writerow([row[0],'1'])
    else:
        prediction_file_object.writerow([row[0],'0'])
test_file.close()
prediction_file.close()
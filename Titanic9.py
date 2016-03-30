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

print "Now we will construct our model for prediction."

def pclass(row):
    a=0
    if float(row[2])==1:
        a=100
    elif float(row[2])==2:
        a=100
    elif float(row[2])==3:
        a=0
    return a

def sex(row):
    a=0
    if row[4]=="female":
        a=74
    else:
        a=0
    return a

def age(row):
    a=0
    if float(row[5])<=20:
        a=69
    elif float(row[5])>20 and float(row[5])<=60:
        a=79
    else:
        a=70
    return a

def sibsp(row):
    a=0
    if float(row[6])<=2:
        a=75
    else:
        a=0
    return a

def parch(row):
    a=0
    if float(row[7])<=3:
        a=70
    else:
        a=0
    return a

def fare(row):
    a=0
    if float(row[9])<=10:
        a=60
    elif float(row[9])>10 and float(row[9])<=20:
        a=73
    elif float(row[9])>20 and float(row[9])<=30:
        a=69
    else:
        a=86
    return a

def cabin(row):
    a=0
    if row[10]=="":
        a=65
    else:
        a=100
    return a

def embarked(row):
    a=0
    if row[11]=="C":
        a=100
    elif row[11]=="Q":
        a=75
    else:
        a=70
    return a

for row in data:
     row[3]=pclass(row)+sibsp(row)+parch(row)
     print row[1],row[3],pclass(row),sibsp(row),parch(row)

 
print "Now I will examine the scores."
bin1= data[data[0::,3].astype(np.float)<=140,1].astype(np.float)
bin2= data[data[0::,3].astype(np.float)>140,1].astype(np.float)
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

prediction_file = open("myseventhmodel.csv", "wb")
prediction_file_object = csv.writer(prediction_file)
#FUNCTIONS
def pclass1(row):
    a=0
    if float(row[1])==1:
        a=100
    elif float(row[1])==2:
        a=100
    elif float(row[1])==3:
        a=0
    return a
    
def sex1(row):
    a=0
    if row[2]=="female":
        a=74
    else:
        a=19
    return a

def age1(row):
    a=0
    if row[4]=="":
        row[4]="1000"
    if float(row[4])<=20:
        a=46
    elif float(row[4])>20 and float(row[4])<=60:
        a=40
    else:
        a=29
    return a

def sibsp1(row):
    a=0
    if float(row[5])<=2:
        a=75
    else:
        a=0
    return a

def parch1(row):
    a=0
    if float(row[6])<=3:
        a=70
    else:
        a=0
    return a


def fare1(row):
    a=0
    if row[8]=="":
        row[8]="1000"
    if float(row[8])<=10:
        a=20
    elif float(row[8])>10 and float(row[8])<=20:
        a=42
    elif float(row[8])>20 and float(row[8])<=30:
        a=44
    else:
        a=58
    return a

def cabin1(row):
    a=0
    if row[9]=="":
        a=30
    else:
        a=67
    return a

def embarked1(row):
    a=0
    if row[10]=="C":
        a=55
    elif row[10]=="Q":
        a=39
    else:
        a=37
    return a

prediction_file_object.writerow(["PassengerId", "Survived"])
for row in test_file_object:
    if row[3] == 'female'and pclass1(row)+sibsp1(row)+parch1(row)>145:
        prediction_file_object.writerow([row[0],'1'])
    else:
        prediction_file_object.writerow([row[0],'0'])
test_file.close()
prediction_file.close()
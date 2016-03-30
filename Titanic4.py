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
print "Our variables are:"
print header
print
pclass1=data[0::,2]=="1"
pclass2=data[0::,2]=="2"
pclass3=data[0::,2]=="3"

pclass1onboard=data[pclass1,1].astype(np.float)
pclass2onboard=data[pclass2,1].astype(np.float)
pclass3onboard=data[pclass3,1].astype(np.float)

proportion_pclass1=np.sum(pclass1onboard)/np.size(pclass1onboard)
proportion_pclass2=np.sum(pclass2onboard)/np.size(pclass2onboard)
proportion_pclass3=np.sum(pclass3onboard)/np.size(pclass3onboard)
print "---------------Pclass factor---------------------"
print "Proportion of pclass1 is "+str(proportion_pclass1*100)+" %."
print "Proportion of pclass2 is "+str(proportion_pclass2*100)+" %."
print "Proportion of pclass3 is "+str(proportion_pclass3*100)+" %."
print
print "So, we can see that pclass affects the probability to survive."
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
print
print "And the sex affects the probability of survive."
print
print "----------------Age factor--------------------------"
print
print "Now, let's examine what happens with the Age factor."
print
print "Our biggest concern is how we will bin up our data."
print
data[ data[0::,5]=="",5] = "1000"
agebin0 = data[data[0::,5]=="1000",1].astype(np.float)
agebin1= data[data[0::,5].astype(np.float)<=20,1].astype(np.float)
agebin2= data[(data[0::,5].astype(np.float)>20)&(data[0::,5].astype(np.float)<=40),1].astype(np.float)
agebin3= data[(data[0::,5].astype(np.float)>40)&(data[0::,5].astype(np.float)<=60),1].astype(np.float)
agebin4= data[(data[0::,5].astype(np.float)>60)&(data[0::,5].astype(np.float)<=80),1].astype(np.float)

proportion_agebin0 = np.sum(agebin0) / np.size(agebin0)
proportion_agebin1 = np.sum(agebin1) / np.size(agebin1)
proportion_agebin2 = np.sum(agebin2) / np.size(agebin2)
proportion_agebin3 = np.sum(agebin3) / np.size(agebin3)
proportion_agebin4 = np.sum(agebin4) / np.size(agebin4)
print
print "Proportion of age nan is "+str(proportion_agebin0*100)+" %."
print
print "Proportion of age 0-20 is "+str(proportion_agebin1*100)+" %."
print
print "Proportion of age 20-40 is "+str(proportion_agebin2*100)+" %."
print
print "Proportion of age 40-60 is "+str(proportion_agebin3*100)+" %."
print
print "Proportion of age 60-80 is "+str(proportion_agebin4*100)+" %."
print
print "Age factor needs further investigation. I believe that kids had better chances to survive."
print "We will examine this factor deeper later."
print
print "--------------------SibSp factor----------------------"
print
print np.unique(data[0::,6])
sib0=data[0::,6]=="0"
sib1=data[0::,6]=="1"
sib2=data[0::,6]=="2"
sib3=data[0::,6]=="3"
sib4=data[0::,6]=="4"
sib5=data[0::,6]=="5"
sib8=data[0::,6]=="8"
sib0onboard=data[sib0,1].astype(np.float)
sib1onboard=data[sib1,1].astype(np.float)
sib2onboard=data[sib2,1].astype(np.float)
sib3onboard=data[sib3,1].astype(np.float)
sib4onboard=data[sib4,1].astype(np.float)
sib5onboard=data[sib5,1].astype(np.float)
sib8onboard=data[sib8,1].astype(np.float)
proportion_sib0=np.sum(sib0onboard)/np.size(sib0onboard)
proportion_sib1=np.sum(sib1onboard)/np.size(sib1onboard)
proportion_sib2=np.sum(sib2onboard)/np.size(sib2onboard)
proportion_sib3=np.sum(sib3onboard)/np.size(sib3onboard)
proportion_sib4=np.sum(sib4onboard)/np.size(sib4onboard)
proportion_sib5=np.sum(sib5onboard)/np.size(sib5onboard)
proportion_sib8=np.sum(sib8onboard)/np.size(sib8onboard)
print
print "Proportion of sib=0 is "+str(proportion_sib0*100)+" %."
print
print "Proportion of sib=1 is "+str(proportion_sib1*100)+" %."
print
print "Proportion of sib=2 is "+str(proportion_sib2*100)+" %."
print
print "Proportion of sib=3 is "+str(proportion_sib3*100)+" %."
print
print "Proportion of sib=4 is "+str(proportion_sib4*100)+" %."
print
print "Proportion of sib=5 is "+str(proportion_sib5*100)+" %."
print
print "Proportion of sib=8 is "+str(proportion_sib8*100)+" %."
print
print "The SibSp factor has very interesting results."
print 
print "-------------------Parch-----------------------"
print 
print np.unique(data[0::,6])
parch0=data[0::,7]=="0"
parch1=data[0::,7]=="1"
parch2=data[0::,7]=="2"
parch3=data[0::,7]=="3"
parch4=data[0::,7]=="4"
parch5=data[0::,7]=="5"
parch6=data[0::,7]=="6"
parch0onboard=data[parch0,1].astype(np.float)
parch1onboard=data[parch1,1].astype(np.float)
parch2onboard=data[parch2,1].astype(np.float)
parch3onboard=data[parch3,1].astype(np.float)
parch4onboard=data[parch4,1].astype(np.float)
parch5onboard=data[parch5,1].astype(np.float)
parch6onboard=data[parch6,1].astype(np.float)
proportion_parch0=np.sum(parch0onboard)/np.size(parch0onboard)
proportion_parch1=np.sum(parch1onboard)/np.size(parch1onboard)
proportion_parch2=np.sum(parch2onboard)/np.size(parch2onboard)
proportion_parch3=np.sum(parch3onboard)/np.size(parch3onboard)
proportion_parch4=np.sum(parch4onboard)/np.size(parch4onboard)
proportion_parch5=np.sum(parch5onboard)/np.size(parch5onboard)
proportion_parch6=np.sum(parch6onboard)/np.size(parch6onboard)
print
print "Proportion of parch=0 is "+str(proportion_parch0*100)+" %."
print
print "Proportion of parch=1 is "+str(proportion_parch1*100)+" %."
print
print "Proportion of parch=2 is "+str(proportion_parch2*100)+" %."
print
print "Proportion of parch=3 is "+str(proportion_parch3*100)+" %."
print
print "Proportion of parch=4 is "+str(proportion_parch4*100)+" %."
print
print "Proportion of parch=5 is "+str(proportion_parch5*100)+" %."
print
print "Proportion of parch=6 is "+str(proportion_parch6*100)+" %."
print
print "So, we see that when parch>=4, the probability of someone to survive is low."
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
print "The bigger the value of the ticket, the mpre probabilities to survive."
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
print "So, we see that passengers with cabin were more likely to survive."
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
print "We see that passengers who use Cherbourg as their port of embarkation have better chances to survive."
print 
print "Now, I will see the results and I  will choose the factors that I believe\
 will help me predict with accuracy who survived or not."
print
print "I have two major goals:"
print "The first one is to create a simple model."
print "The second one is to achieve a better score in the leaderboard than that\
 of the gender model."
print
print "My main purpose is to keep the same model for the women and try to\
 predict that some men will survive. Also, the majority of our sample is men."
print "So, I will concetrate my research on men."
print
men=data[males]
print "---------------Pclass factor---------------------"
class1=men[0::,2]=="1"
class2=men[0::,2]=="2"
class3=men[0::,2]=="3"

class1onboard=men[class1,1].astype(np.float)
class2onboard=men[class2,1].astype(np.float)
class3onboard=men[class3,1].astype(np.float)

proportion_class1=np.sum(class1onboard)/np.size(class1onboard)
proportion_class2=np.sum(class2onboard)/np.size(class2onboard)
proportion_class3=np.sum(class3onboard)/np.size(class3onboard)

print "Proportion of class1 is "+str(proportion_class1*100)+" %."
print "Proportion of class2 is "+str(proportion_class2*100)+" %."
print "Proportion of class3 is "+str(proportion_class3*100)+" %."
print "Nothing interesting about class factor."
print
print "----------------Embarked factor-----------------------------------"
mCherbourg=men[0::,11]=="C"
mQueenstown=men[0::,11]=="Q"
mSouthampton=men[0::,11]=="S"
mCherbourgonboard=men[mCherbourg,1].astype(np.float)
mQueenstownonboard=men[mQueenstown,1].astype(np.float)
mSouthamptononboard=men[mSouthampton,1].astype(np.float)
mproportion_Cherbourg=np.sum(mCherbourgonboard)/np.size(mCherbourgonboard)
mproportion_Queenstown=np.sum(mQueenstownonboard)/np.size(mQueenstownonboard)
mproportion_Southampton=np.sum(mSouthamptononboard)/np.size(mSouthamptononboard)
print
print "Proportion of men from Cherbourg is "+str(mproportion_Cherbourg*100)+" %."
print "Proportion of men from Queenstown is "+str(mproportion_Queenstown*100)+" %."
print "Proportion of men from Southampton is "+str(mproportion_Southampton*100)+" %."
print "Nothing interesting again."
print
print "------------------Cabin factor---------------------------------"
mennocabin=men[0::,10]==""
mencabin=men[0::,10]!=""
mennocabinonboard=men[mennocabin,1].astype(np.float)
mencabinonboard=men[mencabin,1].astype(np.float)
proportion_mennocabin=np.sum(mennocabinonboard)/np.size(mennocabinonboard)
proportion_mencabin=np.sum(mencabinonboard)/np.size(mencabinonboard)
print
print "Proportion of nocabin men is "+str(proportion_mennocabin*100)+" %."
print "Proportion of cabin men is "+str(proportion_mencabin*100)+" %."
print "That is a little better. 42% of men with cabin survived."
print 
print "-----------------Fare factor--------------------"
print
mt1= men[men[0::,9].astype(np.float)<=10,1].astype(np.float)
mt2= men[(men[0::,9].astype(np.float)>10)&(men[0::,9].astype(np.float)<=20),1].astype(np.float)
mt3= men[(men[0::,9].astype(np.float)>20)&(men[0::,9].astype(np.float)<=30),1].astype(np.float)
mt4= men[men[0::,9].astype(np.float)>30,1].astype(np.float)
proportion_mt1 = np.sum(mt1) / np.size(mt1)
proportion_mt2 = np.sum(mt2) / np.size(mt2)
proportion_mt3 = np.sum(mt3) / np.size(mt3)
proportion_mt4 = np.sum(mt4) / np.size(mt4)
print
print "Proportion of ticket 0-10 is "+str(proportion_mt1*100)+" %."
print
print "Proportion of ticket 10-20 is "+str(proportion_mt2*100)+" %."
print
print "Proportion of ticket 20-30 is "+str(proportion_mt3*100)+" %."
print
print "Proportion of ticket 30-max is "+str(proportion_mt4*100)+" %."
print "Nothing interesting in this factor."
print
print "-------------------Parch-----------------------"
print 
print np.unique(men[0::,7])
par0=men[0::,7]=="0"
par1=men[0::,7]=="1"
par2=men[0::,7]=="2"
par3=men[0::,7]=="3"
par4=men[0::,7]=="4"
par5=men[0::,7]=="5"
par0onboard=men[par0,1].astype(np.float)
par1onboard=men[par1,1].astype(np.float)
par2onboard=men[par2,1].astype(np.float)
par3onboard=men[par3,1].astype(np.float)
par4onboard=men[par4,1].astype(np.float)
par5onboard=men[par5,1].astype(np.float)
proportion_par0=np.sum(par0onboard)/np.size(par0onboard)
proportion_par1=np.sum(par1onboard)/np.size(par1onboard)
proportion_par2=np.sum(par2onboard)/np.size(par2onboard)
proportion_par3=np.sum(par3onboard)/np.size(par3onboard)
proportion_par4=np.sum(par4onboard)/np.size(par4onboard)
proportion_par5=np.sum(par5onboard)/np.size(par5onboard)
print
print "Proportion of parch=0 is "+str(proportion_par0*100)+" %."
print
print "Proportion of parch=1 is "+str(proportion_par1*100)+" %."
print
print "Proportion of parch=2 is "+str(proportion_par2*100)+" %."
print
print "Proportion of parch=3 is "+str(proportion_par3*100)+" %."
print
print "Proportion of parch=4 is "+str(proportion_par4*100)+" %."
print
print "Proportion of parch=5 is "+str(proportion_par5*100)+" %."
print
print "This is again something interesting because we can focus on\
 men with parch<=2"
print
print "--------------------SibSp factor----------------------"
print
print np.unique(men[0::,6])
sb0=men[0::,6]=="0"
sb1=men[0::,6]=="1"
sb2=men[0::,6]=="2"
sb3=men[0::,6]=="3"
sb4=men[0::,6]=="4"
sb5=men[0::,6]=="5"
sb8=men[0::,6]=="8"
sb0onboard=men[sb0,1].astype(np.float)
sb1onboard=men[sb1,1].astype(np.float)
sb2onboard=men[sb2,1].astype(np.float)
sb3onboard=men[sb3,1].astype(np.float)
sb4onboard=men[sb4,1].astype(np.float)
sb5onboard=men[sb5,1].astype(np.float)
sb8onboard=men[sb8,1].astype(np.float)
proportion_sb0=np.sum(sb0onboard)/np.size(sb0onboard)
proportion_sb1=np.sum(sb1onboard)/np.size(sb1onboard)
proportion_sb2=np.sum(sb2onboard)/np.size(sb2onboard)
proportion_sb3=np.sum(sb3onboard)/np.size(sb3onboard)
proportion_sb4=np.sum(sb4onboard)/np.size(sb4onboard)
proportion_sb5=np.sum(sb5onboard)/np.size(sb5onboard)
proportion_sb8=np.sum(sb8onboard)/np.size(sb8onboard)
print
print "Proportion of sib=0 is "+str(proportion_sb0*100)+" %."
print
print "Proportion of sib=1 is "+str(proportion_sb1*100)+" %."
print
print "Proportion of sib=2 is "+str(proportion_sb2*100)+" %."
print
print "Proportion of sib=3 is "+str(proportion_sb3*100)+" %."
print
print "Proportion of sib=4 is "+str(proportion_sb4*100)+" %."
print
print "Proportion of sib=5 is "+str(proportion_sb5*100)+" %."
print
print "Proportion of sib=8 is "+str(proportion_sb8*100)+" %."
print
print "Again, we have an interesting result, as we can concetrate only on the men\
 with less than two siblings/spouse."
print
print "----------------Age factor--------------------------"
print
men[ men[0::,5]=="",5] = "1000"
age0 = men[men[0::,5]=="1000",1].astype(np.float)
age1= men[men[0::,5].astype(np.float)<=20,1].astype(np.float)
age2= men[(men[0::,5].astype(np.float)>20)&(men[0::,5].astype(np.float)<=40),1].astype(np.float)
age3= men[(men[0::,5].astype(np.float)>40)&(men[0::,5].astype(np.float)<=60),1].astype(np.float)
age4= men[(men[0::,5].astype(np.float)>60)&(men[0::,5].astype(np.float)<=80),1].astype(np.float)

proportion_age0 = np.sum(age0) / np.size(age0)
proportion_age1 = np.sum(age1) / np.size(age1)
proportion_age2 = np.sum(age2) / np.size(age2)
proportion_age3 = np.sum(age3) / np.size(age3)
proportion_age4 = np.sum(age4) / np.size(age4)
print
print "Proportion of age nan is "+str(proportion_age0*100)+" %."
print
print "Proportion of age 0-20 is "+str(proportion_age1*100)+" %."
print
print "Proportion of age 20-40 is "+str(proportion_age2*100)+" %."
print
print "Proportion of age 40-60 is "+str(proportion_age3*100)+" %."
print
print "Proportion of age 60-80 is "+str(proportion_age4*100)+" %."
print
print "Nothing interesting."
print
print "O.K. My most valuable factors are: SibSp, Parch and Cabin."
print
print "I will subset my data again and I will concetrate on men with cabin"
mwc=men[mencabin]
print
print "--------------------SibSp factor----------------------"
print
scb0=mwc[0::,6]=="0"
scb1=mwc[0::,6]=="1"
scb2=mwc[0::,6]=="2"
scb0onboard=mwc[scb0,1].astype(np.float)
scb1onboard=mwc[scb1,1].astype(np.float)
scb2onboard=mwc[scb2,1].astype(np.float)
proportion_scb0=np.sum(scb0onboard)/np.size(scb0onboard)
proportion_scb1=np.sum(scb1onboard)/np.size(scb1onboard)
proportion_scb2=np.sum(scb2onboard)/np.size(scb2onboard)
print
print "Proportion of sib=0 is "+str(proportion_scb0*100)+" %."
print
print "Proportion of sib=1 is "+str(proportion_scb1*100)+" %."
print
print "Proportion of sib=2 is "+str(proportion_scb2*100)+" %."
print
print "-------------------Parch-----------------------"
print 
pr0=mwc[0::,7]=="0"
pr1=mwc[0::,7]=="1"
pr2=mwc[0::,7]=="2"
pr0onboard=mwc[pr0,1].astype(np.float)
pr1onboard=mwc[pr1,1].astype(np.float)
pr2onboard=mwc[pr2,1].astype(np.float)
proportion_pr0=np.sum(pr0onboard)/np.size(pr0onboard)
proportion_pr1=np.sum(pr1onboard)/np.size(pr1onboard)
proportion_pr2=np.sum(pr2onboard)/np.size(pr2onboard)
print
print "Proportion of parch=0 is "+str(proportion_pr0*100)+" %."
print
print "Proportion of parch=1 is "+str(proportion_pr1*100)+" %."
print
print "Proportion of parch=2 is "+str(proportion_pr2*100)+" %."
print
survival_table = np.zeros([3,3],float)
for i in xrange(3):
    for j in xrange(3):
        men_only_stats=data[ (data[0::,4] == "male") \
                                 & (data[0::,10]!= "") \
                                 & (data[0:,6].astype(np.float)== i ) \
                                 & (data[0:,7].astype(np.float)== j ), 1]                      
        survival_table[i,j] = np.mean(men_only_stats.astype(np.float))
survival_table[ survival_table != survival_table ] = 0
print survival_table        
train_file.close()

test_file = open('test.csv', 'rb')
test_file_object = csv.reader(test_file)
header1 = test_file_object.next()
predictions_file = open("mysecondmodel.csv", "wb")
post = csv.writer(predictions_file)

post.writerow(["PassengerId", "Survived"])
for row in test_file_object:
    if row[3] == 'female':
        post.writerow([row[0],'1'])
    else:
        if row[9]=="":
            post.writerow([row[0],'0'])
        else:
            if float(row[5]) == 1 and float(row[6])<=2 and float(row[6])>=1:
                post.writerow([row[0],'1'])
            else:
                if float(row[5]) == 2 and float(row[6])==1:
                    post.writerow([row[0],'1'])
                else:
                    post.writerow([row[0],'0'])

test_file.close()
predictions_file.close()



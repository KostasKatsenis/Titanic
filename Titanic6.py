# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 18:43:17 2016

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
print "For the time, my goal is to find a simple model which will achieve a\
 better score than the genderbased model. The majority of my sample is men, so\
 I  want to make a good prediction about them. The proportion of men that died was\
 bigger than that of women, so I suppose that this will help me to find the factors\
 that contribute to survive. In this script I will try to go backwards and see\
 if I can find common characteristics to the men who survived."

females=data[0::,4]=="female"
males=data[0::,4]=="male"

femalesonboard=data[females,1].astype(np.float)
malesonboard=data[males,1].astype(np.float)

proportion_females=np.sum(femalesonboard)/np.size(femalesonboard)
proportion_males=np.sum(malesonboard)/np.size(malesonboard)
print
print "Proportion of females survived is "+str(proportion_females*100)+" %."
print "Proportion of males survived is "+str(proportion_males*100)+" %."
print 
print "Total women on board: "+str(np.size(femalesonboard))
print "Total men on board: "+str(np.size(malesonboard))
print
print "As you can see there are 577 men out of 891 people of sample. About 81% of them died so\
 imagine that if we had only men on board, we could predict the outcome with\
 more accuracy. In fact it is the women that drop our accuracy around 77%. So,\
 my approach is wrong. I should concetrate on women."
print

women=data[females]

print "------------------Cabin factor---------------------------------"
print
nocabin=women[0::,10]==""
cabin=women[0::,10]!=""
nocabinonboard=women[nocabin,1].astype(np.float)
cabinonboard=women[cabin,1].astype(np.float)
proportion_nocabin=np.sum(nocabinonboard)/np.size(nocabinonboard)
proportion_cabin=np.sum(cabinonboard)/np.size(cabinonboard)
print
print "Proportion of nocabin women is "+str(proportion_nocabin*100)+" %."
print "Proportion of cabin women is "+str(proportion_cabin*100)+" %."
print 
print "Women with cabin:"+str(np.size(cabinonboard))
print "Women with no cabin:"+str(np.size(nocabinonboard))
print
print "Excellent!!! Almost all women with a cabin survived."
print
print "----------------Embarked factor-----------------------------------"
print
Cherbourg=women[0::,11]=="C"
Queenstown=women[0::,11]=="Q"
Southampton=women[0::,11]=="S"
Unknown=women[0::,11]==""
Cherbourgonboard=women[Cherbourg,1].astype(np.float)
Queenstownonboard=women[Queenstown,1].astype(np.float)
Southamptononboard=women[Southampton,1].astype(np.float)
Unknownonboard=women[Unknown,1].astype(np.float)
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
print "-------------------Parch-----------------------"
print 
parch0=women[0::,7]=="0"
parch1=women[0::,7]=="1"
parch2=women[0::,7]=="2"
parch3=women[0::,7]=="3"
parch4=women[0::,7]=="4"
parch5=women[0::,7]=="5"
parch6=women[0::,7]=="6"
parch0onboard=women[parch0,1].astype(np.float)
parch1onboard=women[parch1,1].astype(np.float)
parch2onboard=women[parch2,1].astype(np.float)
parch3onboard=women[parch3,1].astype(np.float)
parch4onboard=women[parch4,1].astype(np.float)
parch5onboard=women[parch5,1].astype(np.float)
parch6onboard=women[parch6,1].astype(np.float)
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
print "--------------------SibSp factor----------------------"
print
sib0=women[0::,6]=="0"
sib1=women[0::,6]=="1"
sib2=women[0::,6]=="2"
sib3=women[0::,6]=="3"
sib4=women[0::,6]=="4"
sib5=women[0::,6]=="5"
sib8=women[0::,6]=="8"
sib0onboard=women[sib0,1].astype(np.float)
sib1onboard=women[sib1,1].astype(np.float)
sib2onboard=women[sib2,1].astype(np.float)
sib3onboard=women[sib3,1].astype(np.float)
sib4onboard=women[sib4,1].astype(np.float)
sib5onboard=women[sib5,1].astype(np.float)
sib8onboard=women[sib8,1].astype(np.float)
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
print "Interesting. The less the Siblings/Spouse the more chances to survive"
print
print "----------------Age factor--------------------------"
print
women[ women[0::,5]=="",5] = "1000"
agebin0 = women[women[0::,5]=="1000",1].astype(np.float)
agebin1= women[women[0::,5].astype(np.float)<=20,1].astype(np.float)
agebin2= women[(women[0::,5].astype(np.float)>20)&(women[0::,5].astype(np.float)<=40),1].astype(np.float)
agebin3= women[(women[0::,5].astype(np.float)>40)&(women[0::,5].astype(np.float)<=60),1].astype(np.float)
agebin4= women[(women[0::,5].astype(np.float)>60)&(women[0::,5].astype(np.float)<=80),1].astype(np.float)

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
pclass1=women[0::,2]=="1"
pclass2=women[0::,2]=="2"
pclass3=women[0::,2]=="3"

pclass1onboard=women[pclass1,1].astype(np.float)
pclass2onboard=women[pclass2,1].astype(np.float)
pclass3onboard=women[pclass3,1].astype(np.float)

proportion_pclass1=np.sum(pclass1onboard)/np.size(pclass1onboard)
proportion_pclass2=np.sum(pclass2onboard)/np.size(pclass2onboard)
proportion_pclass3=np.sum(pclass3onboard)/np.size(pclass3onboard)
print "---------------Pclass factor---------------------"
print "Proportion of pclass1 is "+str(proportion_pclass1*100)+" %."
print "Proportion of pclass2 is "+str(proportion_pclass2*100)+" %."
print "Proportion of pclass3 is "+str(proportion_pclass3*100)+" %."
print
print "Excellent again. Almost all the women in 1st and 2nd class survived."
print "-----------------Fare factor--------------------"
print
ticketbin1= women[women[0::,9].astype(np.float)<=10,1].astype(np.float)
ticketbin2= women[(women[0::,9].astype(np.float)>10)&(women[0::,9].astype(np.float)<=20),1].astype(np.float)
ticketbin3= women[(women[0::,9].astype(np.float)>20)&(women[0::,9].astype(np.float)<=30),1].astype(np.float)
ticketbin4= women[women[0::,9].astype(np.float)>30,1].astype(np.float)
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
print "Let's experiment with the variables SibSp and Parch. I will create a new\
 variable Family that will be equal to SibSp and Parch."
print
print "------------------Family factor-------------------------"
print
Family0=women[0::,6].astype(np.float)+women[0::,7].astype(np.float)==0
Family1=women[0::,6].astype(np.float)+women[0::,7].astype(np.float)==1
Family2=women[0::,6].astype(np.float)+women[0::,7].astype(np.float)==2
Family3=women[0::,6].astype(np.float)+women[0::,7].astype(np.float)==3
Family4=women[0::,6].astype(np.float)+women[0::,7].astype(np.float)==4
Family5=women[0::,6].astype(np.float)+women[0::,7].astype(np.float)==5
Family6=women[0::,6].astype(np.float)+women[0::,7].astype(np.float)==6
Family7=women[0::,6].astype(np.float)+women[0::,7].astype(np.float)==7
Family8=women[0::,6].astype(np.float)+women[0::,7].astype(np.float)==8
Family9=women[0::,6].astype(np.float)+women[0::,7].astype(np.float)==9
Family10=women[0::,6].astype(np.float)+women[0::,7].astype(np.float)==10
F0onboard=women[Family0,1].astype(np.float)
F1onboard=women[Family1,1].astype(np.float)
F2onboard=women[Family2,1].astype(np.float)
F3onboard=women[Family3,1].astype(np.float)
F4onboard=women[Family4,1].astype(np.float)
F5onboard=women[Family5,1].astype(np.float)
F6onboard=women[Family6,1].astype(np.float)
F7onboard=women[Family7,1].astype(np.float)
F8onboard=women[Family8,1].astype(np.float)
F9onboard=women[Family9,1].astype(np.float)
F10onboard=women[Family10,1].astype(np.float)
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
print "So, if the woman has less than 4 relatives, has good chances to survive."
print
print "The women of 1st and 2nd class have probability of survival bigger than 90%."
print "So, I will concetrate on them of 3rd class."

wom=women[women[0::,2]=="3"]
print "There are "+str(np.size(wom[0::,0]))+" women in that category, almost the half."
print "I will examine the factors Cabin,Embarked, SibSp, Parch and finally Family."
print
print "---------Cabin factor for women of 3rd class--------------------------"
print
nocab=wom[0::,10]==""
cab=wom[0::,10]!=""
nocabonboard=wom[nocab,1].astype(np.float)
cabonboard=wom[cab,1].astype(np.float)
proportion_nocab=np.sum(nocabonboard)/np.size(nocabonboard)
proportion_cab=np.sum(cabonboard)/np.size(cabonboard)
print
print "Proportion of nocabin women is "+str(proportion_nocab*100)+" %."
print "Proportion of cabin women is "+str(proportion_cab*100)+" %."
print 
print "Women with cabin:"+str(np.size(cabonboard))
print "Women with no cabin:"+str(np.size(nocabonboard))
print
print "Nothing interesting."
print
print "---------Embarked factor for women of 3rd class--------------------------"
Cher=wom[0::,11]=="C"
Queens=wom[0::,11]=="Q"
South=wom[0::,11]=="S"
Cheronboard=wom[Cher,1].astype(np.float)
Queensonboard=wom[Queens,1].astype(np.float)
Southonboard=wom[South,1].astype(np.float)
prop_Cherbourg=np.sum(Cheronboard)/np.size(Cheronboard)
prop_Queenstown=np.sum(Queensonboard)/np.size(Queensonboard)
prop_Southampton=np.sum(Southonboard)/np.size(Southonboard)
print
print "Proportion of passengers from Cherbourg is "+str(prop_Cherbourg*100)+" %."
print "Proportion of passengers from Queenstown is "+str(prop_Queenstown*100)+" %."
print "Proportion of passengers from Southampton is "+str(prop_Southampton*100)+" %."
print np.size(Cheronboard), np.size(Queensonboard), np.size(Southonboard)
print "Slighty interesting. Maybe I will use this."
print
print "---------------Parch factor for women of 3rd class-----------------------"
print 
par0=wom[0::,7]=="0"
par1=wom[0::,7]=="1"
par2=wom[0::,7]=="2"
par3=wom[0::,7]=="3"
par4=wom[0::,7]=="4"
par5=wom[0::,7]=="5"
par6=wom[0::,7]=="6"
par0onboard=wom[par0,1].astype(np.float)
par1onboard=wom[par1,1].astype(np.float)
par2onboard=wom[par2,1].astype(np.float)
par3onboard=wom[par3,1].astype(np.float)
par4onboard=wom[par4,1].astype(np.float)
par5onboard=wom[par5,1].astype(np.float)
par6onboard=wom[par6,1].astype(np.float)
prop_parch0=np.sum(par0onboard)/np.size(par0onboard)
prop_parch1=np.sum(par1onboard)/np.size(par1onboard)
prop_parch2=np.sum(par2onboard)/np.size(par2onboard)
prop_parch3=np.sum(par3onboard)/np.size(par3onboard)
prop_parch4=np.sum(par4onboard)/np.size(par4onboard)
prop_parch5=np.sum(par5onboard)/np.size(par5onboard)
prop_parch6=np.sum(par6onboard)/np.size(par6onboard)
print
print "Proportion of parch=0 is "+str(prop_parch0*100)+" %."
print np.size(par0onboard)
print "Proportion of parch=1 is "+str(prop_parch1*100)+" %."
print np.size(par1onboard)
print "Proportion of parch=2 is "+str(prop_parch2*100)+" %."
print np.size(par2onboard)
print "Proportion of parch=3 is "+str(prop_parch3*100)+" %."
print np.size(par3onboard)
print "Proportion of parch=4 is "+str(prop_parch4*100)+" %."
print np.size(par4onboard)
print "Proportion of parch=5 is "+str(prop_parch5*100)+" %."
print np.size(par5onboard)
print "Proportion of parch=6 is "+str(prop_parch6*100)+" %."
print np.size(par6onboard)
print "Not much information."
print
print "-----------------SibSp factor for women of 3rd class----------------------"
print
s0=wom[0::,6]=="0"
s1=wom[0::,6]=="1"
s2=wom[0::,6]=="2"
s3=wom[0::,6]=="3"
s4=wom[0::,6]=="4"
s5=wom[0::,6]=="5"
s8=wom[0::,6]=="8"
s0onboard=wom[s0,1].astype(np.float)
s1onboard=wom[s1,1].astype(np.float)
s2onboard=wom[s2,1].astype(np.float)
s3onboard=wom[s3,1].astype(np.float)
s4onboard=wom[s4,1].astype(np.float)
s5onboard=wom[s5,1].astype(np.float)
s8onboard=wom[s8,1].astype(np.float)
prop_sib0=np.sum(s0onboard)/np.size(s0onboard)
prop_sib1=np.sum(s1onboard)/np.size(s1onboard)
prop_sib2=np.sum(s2onboard)/np.size(s2onboard)
prop_sib3=np.sum(s3onboard)/np.size(s3onboard)
prop_sib4=np.sum(s4onboard)/np.size(s4onboard)
prop_sib5=np.sum(s5onboard)/np.size(s5onboard)
prop_sib8=np.sum(s8onboard)/np.size(s8onboard)
print
print "Proportion of sib=0 is "+str(prop_sib0*100)+" %."
print np.size(s0onboard)
print "Proportion of sib=1 is "+str(prop_sib1*100)+" %."
print np.size(s1onboard)
print "Proportion of sib=2 is "+str(prop_sib2*100)+" %."
print np.size(s2onboard)
print "Proportion of sib=3 is "+str(prop_sib3*100)+" %."
print np.size(s3onboard)
print "Proportion of sib=4 is "+str(prop_sib4*100)+" %."
print np.size(s4onboard)
print "Proportion of sib=5 is "+str(prop_sib5*100)+" %."
print np.size(s5onboard)
print "Proportion of sib=8 is "+str(prop_sib8*100)+" %."
print np.size(s8onboard)
print 
print "The same thing here."
print
print "------------------Family factor for women of 3rd class-------------------------"
print
Fam0=wom[0::,6].astype(np.float)+wom[0::,7].astype(np.float)==0
Fam1=wom[0::,6].astype(np.float)+wom[0::,7].astype(np.float)==1
Fam2=wom[0::,6].astype(np.float)+wom[0::,7].astype(np.float)==2
Fam3=wom[0::,6].astype(np.float)+wom[0::,7].astype(np.float)==3
Fam4=wom[0::,6].astype(np.float)+wom[0::,7].astype(np.float)==4
Fam5=wom[0::,6].astype(np.float)+wom[0::,7].astype(np.float)==5
Fam6=wom[0::,6].astype(np.float)+wom[0::,7].astype(np.float)==6
Fam7=wom[0::,6].astype(np.float)+wom[0::,7].astype(np.float)==7
Fam8=wom[0::,6].astype(np.float)+wom[0::,7].astype(np.float)==8
Fam9=wom[0::,6].astype(np.float)+wom[0::,7].astype(np.float)==9
Fam10=wom[0::,6].astype(np.float)+wom[0::,7].astype(np.float)==10
F0board=wom[Fam0,1].astype(np.float)
F1board=wom[Fam1,1].astype(np.float)
F2board=wom[Fam2,1].astype(np.float)
F3board=wom[Fam3,1].astype(np.float)
F4board=wom[Fam4,1].astype(np.float)
F5board=wom[Fam5,1].astype(np.float)
F6board=wom[Fam6,1].astype(np.float)
F7board=wom[Fam7,1].astype(np.float)
F8board=wom[Fam8,1].astype(np.float)
F9board=wom[Fam9,1].astype(np.float)
F10board=wom[Fam10,1].astype(np.float)
prop_F0=np.sum(F0board)/np.size(F0board)
prop_F1=np.sum(F1board)/np.size(F1board)
prop_F2=np.sum(F2board)/np.size(F2board)
prop_F3=np.sum(F3board)/np.size(F3board)
prop_F4=np.sum(F4board)/np.size(F4board)
prop_F5=np.sum(F5board)/np.size(F5board)
prop_F6=np.sum(F6board)/np.size(F6board)
prop_F7=np.sum(F7board)/np.size(F7board)
prop_F8=np.sum(F8board)/np.size(F8board)
prop_F9=np.sum(F9board)/np.size(F9board)
prop_F10=np.sum(F10board)/np.size(F10board)
print prop_F0,np.size(F0board)
print prop_F1,np.size(F1board)
print prop_F2,np.size(F2board)
print prop_F3,np.size(F3board)
print prop_F4,np.size(F4board)
print prop_F5,np.size(F5board)
print prop_F6,np.size(F6board)
print prop_F7,np.size(F7board)
print prop_F8,np.size(F8board)
print prop_F9,np.size(F9board)
print prop_F10,np.size(F10board)
print
print "Very interesting factors are Embarked and Family factor"
print
cherbourghwomen=wom[wom[0::,11]=="C"]
queenstownwomen=wom[wom[0::,11]=="Q"]
southamptonwomen=wom[wom[0::,11]=="S"]
print "----Family factor in women from Cherbourgh."
FLC=cherbourghwomen[0::,6].astype(np.float)+cherbourghwomen[0::,7].astype(np.float) < 4
FHC=cherbourghwomen[0::,6].astype(np.float)+cherbourghwomen[0::,7].astype(np.float) >=4
FLConboard=cherbourghwomen[FLC,1].astype(np.float)
FHConboard=cherbourghwomen[FHC,1].astype(np.float)
prop_FLC=np.sum(FLConboard)/np.size(FLConboard)
prop_FHC=np.sum(FHConboard)/np.size(FHConboard)
print
print prop_FLC,np.size(FLConboard)
print prop_FHC,np.size(FHConboard)
print
print "----Family factor in women from Queenstown."
FLQ=queenstownwomen[0::,6].astype(np.float)+queenstownwomen[0::,7].astype(np.float) < 2
FHQ=queenstownwomen[0::,6].astype(np.float)+queenstownwomen[0::,7].astype(np.float) >=2
FLQonboard=queenstownwomen[FLQ,1].astype(np.float)
FHQonboard=queenstownwomen[FHQ,1].astype(np.float)
prop_FLQ=np.sum(FLQonboard)/np.size(FLQonboard)
prop_FHQ=np.sum(FHQonboard)/np.size(FHQonboard)
print
print prop_FLQ,np.size(FLQonboard)
print prop_FHQ,np.size(FHQonboard)
print
print "Excellent. For less than 2 family members women from Queenstown have\
 about 80% chances to survive."
print
print "----Family factor in women from Southampton."
FLS=southamptonwomen[0::,6].astype(np.float)+southamptonwomen[0::,7].astype(np.float) < 1
FHS=southamptonwomen[0::,6].astype(np.float)+southamptonwomen[0::,7].astype(np.float) >=1
FLSonboard=southamptonwomen[FLS,1].astype(np.float)
FHSonboard=southamptonwomen[FHS,1].astype(np.float)
prop_FLS=np.sum(FLSonboard)/np.size(FLSonboard)
prop_FHS=np.sum(FHSonboard)/np.size(FHSonboard)
print
print prop_FLS,np.size(FLSonboard)
print prop_FHS,np.size(FHSonboard)
print
print "I have to examine only women from Cherbourgh and Southampton"
print 
print "----Parch factor in women from Cherbourgh."
print 
cpar0=cherbourghwomen[0::,7]=="0"
cpar1=cherbourghwomen[0::,7]=="1"
cpar2=cherbourghwomen[0::,7]=="2"
cpar3=cherbourghwomen[0::,7]=="3"
cpar0onboard=cherbourghwomen[cpar0,1].astype(np.float)
cpar1onboard=cherbourghwomen[cpar1,1].astype(np.float)
cpar2onboard=cherbourghwomen[cpar2,1].astype(np.float)
cpar3onboard=cherbourghwomen[cpar3,1].astype(np.float)
prop_cparch0=np.sum(cpar0onboard)/np.size(cpar0onboard)
prop_cparch1=np.sum(cpar1onboard)/np.size(cpar1onboard)
prop_cparch2=np.sum(cpar2onboard)/np.size(cpar2onboard)
prop_cparch3=np.sum(cpar3onboard)/np.size(cpar3onboard)
print
print "Proportion of parch=0 is "+str(prop_cparch0*100)+" %."
print np.size(cpar0onboard)
print "Proportion of parch=1 is "+str(prop_cparch1*100)+" %."
print np.size(cpar1onboard)
print "Proportion of parch=2 is "+str(prop_cparch2*100)+" %."
print np.size(cpar2onboard)
print "Proportion of parch=3 is "+str(prop_cparch3*100)+" %."
print np.size(cpar3onboard)
print "----Parch factor in women from Southampton."
print 
spar0=southamptonwomen[0::,7]=="0"
spar1=southamptonwomen[0::,7]=="1"
spar2=southamptonwomen[0::,7]=="2"
spar3=southamptonwomen[0::,7]=="3"
spar0onboard=southamptonwomen[spar0,1].astype(np.float)
spar1onboard=southamptonwomen[spar1,1].astype(np.float)
spar2onboard=southamptonwomen[spar2,1].astype(np.float)
spar3onboard=southamptonwomen[spar3,1].astype(np.float)
prop_sparch0=np.sum(spar0onboard)/np.size(spar0onboard)
prop_sparch1=np.sum(spar1onboard)/np.size(spar1onboard)
prop_sparch2=np.sum(spar2onboard)/np.size(spar2onboard)
prop_sparch3=np.sum(spar3onboard)/np.size(spar3onboard)
print
print "Proportion of parch=0 is "+str(prop_sparch0*100)+" %."
print np.size(spar0onboard)
print "Proportion of parch=1 is "+str(prop_sparch1*100)+" %."
print np.size(spar1onboard)
print "Proportion of parch=2 is "+str(prop_sparch2*100)+" %."
print np.size(spar2onboard)
print "Proportion of parch=3 is "+str(prop_sparch3*100)+" %."
print np.size(spar3onboard)
print "Finally, I will accept that all women from Cherbourgh survive and all\
 women from Southampton died."
 
train_file.close()

test_file = open('test.csv', 'rb')
test_file_object = csv.reader(test_file)
header1 = test_file_object.next()
predictions_file = open("myfourthmodel.csv", "wb")
post = csv.writer(predictions_file)

post.writerow(["PassengerId", "Survived"])
for row in test_file_object:
    if row[3] == 'male':
        post.writerow([row[0],'0'])
    else:
        if row[1]!="3":
            post.writerow([row[0],'1'])
        else:
            if row[10]=="C" or (row[10]=="Q" and float(row[5])+float(row[6])<2):
                post.writerow([row[0],'1'])
            else:
                post.writerow([row[0],'0'])
test_file.close()
predictions_file.close()
                
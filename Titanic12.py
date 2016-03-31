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
# Let's consider men and women separately
males=data[0::,4]=="male"
females=data[0::,4]=="female"
women=data[females]
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
print 
print "So, for men I have three rules. I will assume that everyone died except\
 those that their empbarkation port was not Queenstown, their age was below 15\
 and they had less than 4 family members."
print
print "---------------Pclass factor for women---------------------"
pclass1=women[0::,2]=="1"
pclass2=women[0::,2]=="2"
pclass3=women[0::,2]=="3"

pclass1onboard=women[pclass1,1].astype(np.float)
pclass2onboard=women[pclass2,1].astype(np.float)
pclass3onboard=women[pclass3,1].astype(np.float)

proportion_pclass1=np.sum(pclass1onboard)/np.size(pclass1onboard)
proportion_pclass2=np.sum(pclass2onboard)/np.size(pclass2onboard)
proportion_pclass3=np.sum(pclass3onboard)/np.size(pclass3onboard)
print "Proportion of pclass1 is "+str(proportion_pclass1*100)+" %."
print "Proportion of pclass2 is "+str(proportion_pclass2*100)+" %."
print "Proportion of pclass3 is "+str(proportion_pclass3*100)+" %."
print
print "Excellent!!! Almost all the women in 1st and 2nd class survived."
print
print "I will concetrate on women on 3rd class. My first rule for women is that\
 all women in 1st and 2nd class survived."
print
print "---------Embarked factor for women of 3rd class--------------------------"
wom=women[women[0::,2]=="3"]
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
print "Family-members","Rate-survived","Size"
print " 0",prop_F0,np.size(F0board)
print " 1",prop_F1,np.size(F1board)
print " 2",prop_F2,np.size(F2board)
print " 3",prop_F3,np.size(F3board)
print " 4",prop_F4,np.size(F4board)
print " 5",prop_F5,np.size(F5board)
print " 6",prop_F6,np.size(F6board)
print " 7",prop_F7,np.size(F7board)
print " 8",prop_F8,np.size(F8board)
print " 9",prop_F9,np.size(F9board)
print "10",prop_F10,np.size(F10board)
print
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
 about 80% chances to survive.This is my second rule."
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
print "Finally, I will accept that all women from Cherbourgh survive and all\
 women from Southampton died."
print
print "So, to summarize for women, all women in 1st and 2nd class survived and for the 3rd class\
 those from Southampton died, those from Cherbourgh survived and those from Queenstown with less\
  than 4 family members survived."
train_file.close()
print
test_file = open('test.csv', 'rb')
test_file_object = csv.reader(test_file)
header1 = test_file_object.next()

prediction_file = open("mybestcsvmodel.csv", "wb")
prediction_file_object = csv.writer(prediction_file)

prediction_file_object.writerow(["PassengerId", "Survived"])
for row in test_file_object:
    if row[4]=="":
        row[4]="1000"
    if row[3] == 'female':
        if row[1]!="3":
            prediction_file_object.writerow([row[0],'1'])
        else:
            if row[10]=="C" or (row[10]=="Q" and float(row[5])+float(row[6])<2):
                prediction_file_object.writerow([row[0],'1'])
            else:
                prediction_file_object.writerow([row[0],'0'])
    elif row[3] == "male" and float(row[4])<=15 and row[10]!="Q" and float(row[5])+float(row[6])<4:
        prediction_file_object.writerow([row[0],'1'])
    else:
        prediction_file_object.writerow([row[0],'0'])
test_file.close()
prediction_file.close()
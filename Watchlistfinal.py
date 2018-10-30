# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 12:46:02 2018

@author: Arshia Joshi
"""

import numpy as np
import pandas as pd

df=pd.read_excel(r"C:\Users\Arshia Joshi\Downloads\Book1.xlsx",header=0)

col1 = df.iloc[:,1]
myname = col1.values.tolist()
print(myname)

col2 = df.iloc[:,2]
myaddress = col2.values.tolist()
print(myaddress)

col3 = df.iloc[:,3]
myphone = col3.values.tolist()
print(myphone)

col4 = df.iloc[:,4]
myadhar = col4.values.tolist()
print(myadhar)

col5 = df.iloc[:,5]
mydob = col5.values.tolist()
print(mydob)

col6 = df.iloc[:,6]
myemail = col6.values.tolist()
print(myemail)

df1=pd.read_excel(r"C:\Users\Arshia Joshi\Downloads\Delhi _Sample_addresses.xlsx",header=0)

col = df1.iloc[:,1]
mylist = col.values.tolist()
print(mylist)

col_adhar = df1.iloc[:,4]
adhar = col_adhar.values.tolist()
print(adhar)

col6=df1.iloc[:,6]
email = col6.values.tolist()
print(email)

col3=df1.iloc[:,3]
phone=col3.values.tolist()
print(phone)

col2=df1.iloc[:,2]
address=col2.values.tolist()
print(address)

col5=df1.iloc[:,5]
dob=col5.values.tolist()
print(dob)

col_number=df1.iloc[:,0]
sno=col_number.values.tolist()
print(sno)


cd C:\Users\Arshia Joshi\Downloads\fuzzywuzzy-master\fuzzywuzzy-master\fuzzywuzzy-master

from fuzzywuzzy import fuzz
from fuzzywuzzy import process


i=0
while i<len(myname):
    n=str(myname[i])
    n1= process.extract(n,mylist) [0][0]
    print(n1)
    n2= mylist.index(n1)
    nme= sno[n2]
    print(nme)
    
    a=str(myadhar[i])
    a1=process.extract(a,adhar) [0][0]
    print(a1)
    a2=adhar.index(a1)
    adharfinal=sno[n2]
    print(adharfinal)
    
    e=str(myemail[i])
    e1= process.extract(e,email) [0][0]
    print(e1)
    e2= email.index(e1)
    eml= sno[e2]
    print(eml)
    
    l=str(myaddress[i])
    l1= process.extract(l, address) [0][0]
    print(l1)
    l2= address.index(l1)
    adr= sno[l2]
    print(adr)
    
    p=str(myphone[i])
    p1= process.extract(p, phone) [0][0]
    print(p1)
    p2= phone.index(p1)
    phn= sno[p2]
    print(phn)
    
    d=str(mydob[i])
    d1= process.extract(d, dob) [0][0]
    print(d1)
    d2= dob.index(d1)
    dobfinal= sno[d2]
    print(dobfinal)
    
    
    if adharfinal == nme:
        if adharfinal == eml:
            print("Email Match found (100%)")
        elif adharfinal==phn:
            print("Phone Match found (100%)")
        elif adharfinal==adr:
            print("Address Match found (100%)")
        elif adharfinal==dobfinal:
            print("DOB Match found (100%)")
    else:
        if nme == eml:
            if nme==phn:
                print("Match found (80%)")
            elif nme==adr:
                print("Match found (80%)")
            elif nme==dobfinal:
                print("Match found (80%)")
        elif adharfinal == eml:
            if adharfinal==phn:
                print("Match found (80%)")
            elif adharfinal==adr:
                print("Match found (80%)")
            elif adharfinal==dobfinal:
                print("Match found (80%)")      
        elif nme==phn:
            if nme==adr:
                print("Match found (70%)")
            elif nme==dobfinal:
                print("Match found (70%)")
        elif adharfinal==phn:
            if adharfinal==adr:
                print("Match found (70%)")
            elif adharfinal==dobfinal:
                print("Match found (70%)")        
        else:
            if eml==phn:
                if phn==adr:
                    print("Match found (60%)")
                elif phn==dobfinal:
                    print("Match found (60%)")
            elif eml==adr:
                if adr ==dobfinal:
                    print("Match found (50%)")
            else:
                if phn==adr:
                    if adr==dobfinal:
                        print("Match found (40%)")
                    else:
                        print("Only phone and address matches")
                else:
                    print("No match found")
    i=i+1
    


i=0
dict={}
while i<len(myname):
    dict['Name']=myname[i]
    dict['Address']=myaddress[i]
    dict['Phone']=myphone[i]
    dict['Adhar']=myadhar[i]
    dict['DOB']=mydob[i]
    dict['Email']=myemail[i]
         
    book=pd.Series(dict, name='Name')
    print(book)
    i=i+1
    



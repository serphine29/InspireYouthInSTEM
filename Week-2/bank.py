#!/usr/bin/envpython3

#This is a single line comment
#pythonprogram to illustrate the  use of operators
#Name : Serphine Ouma
#email :serphineachieng52@gmail.com
#Date : 17th february 2023
#file : bank



#write aprogram that calculates 16%
#ranging between 100k   150k
#19% tax income is between 150k  300k
#30%tax income above 300k
#5% tax income if income is less than 100k

#print gross income ,net income


#formulae gross_income = net income + taxes

net_income = int(input("enter your net income"))

#above 300k
if(net_income >=300000):
    gross_income = net income +( (30/100)*net_income)
    print("since your net income is{} your gross income is {}".format(net_income,int(gross_income)))
    
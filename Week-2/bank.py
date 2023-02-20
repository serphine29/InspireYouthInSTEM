#!/usr/bin/envpython3

#This is a single line comment
#pythonprogram to illustrate the  use of operators
#Name : Serphine Ouma
#email :serphineachieng52@gmail.com
#Date : 17th february 2023
#file : bank


# 5% tax income  for  income below 100k
#write aprogram that calculates 16%
#ranging between 100k   150k
#19% tax income is between 150k  300k
#30%tax income above 300k


#print gross income ,net income


#formulae gross_income = net income + taxes



#net_income = int(input("enter your net income"))
gross_income = int(input("what is your gross income"))

tax_group_1 = (gross_income * 0.05)
tax_group_2 = (gross_income * 0.16)
tax_group_3 = (gross_income * 0.19)
tax_group_4 = (gross_income * 0.3)

if gross_income < 100000:
    print("gross_income",gross_income)
    print("net_income", gross_income - tax_group_1)
elif(gross_income >=100001) & (gross_income < 150000):
    print("gross_income",gross_income)
    print("net-income", gross_income -tax_group_2)

elif(gross_income >=150000) &(gross_income < 300000):
    print("gross_income",gross_income)
    print("net_income",gross_income - tax_group_3)

else:
    print("gross_income",gross_income)
    print("net_income",gross_income- tax_group_4)
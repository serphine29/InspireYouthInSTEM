#!/usr/bin/envpython3

#This is a single line comment
#using for loop to draw diamond , triangle , pascals triangle
#Name : Serphine Ouma
#email :serphineachieng52@gmail.com
#Date : 21th february 2023
#file : assignmentlop.py


h = eval( input("enter diamond's height:"))
for x in range(h):
    print("" * (h - x),"*" * (2*x + 1))
for x in range(h - 2, -1,-1):
    print ("" * (h - x ),"*" * (2*x +1))



num = int(input("enter the number:"))
list1 = [] #an emptylist
for i in range (num):
    list1.append([])
    list1[i].append(1)
    for j in range(1 , i):
        list1 [i].append(list1[i - 1](j- 1)+ list1[i - 1][j])
for i in range (num):
    print(" " *(num - i),end = " ", sep = " ")
    for j in range(0, i + 1):
        print('{3:6}'.format(list1[i][j]),end = " ", sep = " ")
        print()



def factorial(n):
    for i in range( 0,n):
        fact_n = n * (n - i)
        return fact_n

print( factorial(3))

#write a program to calculate simple interest using function

def simple_interest( p ,r ,t):
    SI = (p * r * t)/100
    return SI
p = float(input("Enter the principal amount:"))
r = float(input("Enter the rate of interest:"))
t = float(input("Enter the number of years:"))

#calculate simple_interest by using this formula
SI = simple_interest( p ,r ,t )
print("simple_interest : {}".format(SI))
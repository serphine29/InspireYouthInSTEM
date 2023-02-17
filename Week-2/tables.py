from tabulate import tabulate

mydata =[
     ["litrah", "Eldoret"]
     ["Mrema", "kisumu"]
     ["Louis", "Nairobi"]
]
head =["Name","city"]
print(tabulate(mydata,headers=head ,tablefmt="grid"))
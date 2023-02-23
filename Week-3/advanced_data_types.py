

#advanced data types
# mutable vs immutable

#mutable are  data types that can be edited during program life cycle
# add / remove elements 

# immutable are data types that cannot be edited during program life cycle 

#1 list ( mutable 
friends = [" teddy","Baraka","beverly","cecilia"]
# or friends = [] for  empty list 
# add/append/extend
#remove --> pop/delete
students = ["mark","marie","faith"]
friends.extend(students)
friends.append("james")
friends.sort()
friends. reverse()
# 2) tuples( immutable)
# type of list that are immutable 
stationaries = ("pens","pencils","sharpener","ink")

#replace the whole tuple
stationaries = ("ruler","clip board")

for stationary in stationaries:
    print(stationary)
numbers = (1,2,3,4)


#3) dictionaries aka dict
# uses key and value pair
student = {"name" : "Serphine","age" : "18," "gender":"female"}
print(student["name"])
print(student["age"])
print(student["gender"])
print(student["is_tall"])

#"name" :"serphine" -->name(key) serphine(value )
# 4)sets 
my_fruits ={"apple","banana","oranges","mangoeS"}

for fruit in my_fruits:
    print(fruit)
    print(type(my_fruits))
    print(len(my_fruits))
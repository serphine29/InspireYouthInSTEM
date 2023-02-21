 #usr/bin/envpython3

#This is a single #!/line comment
#pythonprogram to illustrate the  use of lists
#Name : Serphine Ouma
#email :serphineachieng52@gmail.com
#Date : 20th february 2023
#file : asignment.py




#create an empty list of favourite musician
#using for loop add five new musicians
#copy the list to a new list called celebs
#sort the list 
# pop out 2 celebrities from the list
#create an empty list of favourite musicians
fav_musicians = []

#using for loop add five new musicians
fav_musicians =["Sauti Sol","Elani","Nviri","Calum Scot","Vijana Barobaro"]
print(fav_musicians)
for musician in fav_musicians:
    print(musician)

fav_musicians.append("Justin Bierber")
print(fav_musicians)


#copy the list to a new list called celebs

celebs = fav_musicians.copy()
print(celebs)

#sort the list 
celebs.sort()
print(celebs)

#count the remaining celebrities in the list
print(len(celebs))


#Pop out two celebs
celebs.pop()
celebs.pop()
print(celebs)

class car:
    def __init__(self , model ,make ,year_of_manufacture):
       self, model = model
       self.make = make
       self.year_of_manufacture = year_of_manufacture
       
    
    def get_model(self):
        return self.model
    
    def get_make(self):
        return self. make

    def get_year(self):
        return self.year_of_manufacture
    

#objects :instances of the class
car1 = car("demio","nissan",2018)

car2 = car("hilux","toyota",2020)

car3 = car("passat","vw",2000)

#getters
print(car1.get_model())
print(car1.get_make())
print(car1.get_year_of_manufacture())

print(car2 .get_model())
print(car2 .get_make())
print(car2 .get_year_of_manufacture())

print(car3 .get_model())
print(car3 .get_make())
print(car3 .get_year_of_manufacture())



#setters : used to set the attributes 
def set_model(self,model):
    self.model = model

def set_make(self,make):
    self.make = make

def set_year(self,year):
    self.year = year
#objects : instances of the class
car1 = car

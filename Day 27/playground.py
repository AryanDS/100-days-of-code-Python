"""
*args Many Positional Arguements
**kwargs Many keyword Arguements
"""

#Unlimited Positional Arguements!
#The arguements are passed into the add function as a TUPLE
from pyexpat import model
from numpy import multiply


def add(*args):
    sum=0
    for n in args:
        sum+=n
    return sum

print(add(1,2,3,4,5))


#Many Keyword Arguements!
#The arguement are passed into the function as a DICTIONARY
def calculate(n, **kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)

    print(kwargs["multiply"])    

    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=9)

#An example of kwargs while making Classes!

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
        #We can use kwargs.get("model") instead of kwargs["model"] since 
        # When the model =" Something" is not passed kwargs.get("model") will return NONE and not crash
        #However when model="Something " is not passed kwargs["model"] will give an error!
        #AN example below
        self.year= kwargs.get("year")

car =  Car(make = "BMW", model ="M-Series")
print(car.make)
print(car.model)

car2 = Car(make="BMW", model="5-Series")
print(car2.year)

car3 = Car(make="BMW", model="5-Series", year=2022)
print(car3.year)

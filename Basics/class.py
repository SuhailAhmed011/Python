from random import randint

class Employee:
    language = "python"
    salary = 15000
 
suhail = Employee()
suhail.name = "Suhail"
print(suhail.name,suhail.language, suhail.salary)

sameer = Employee()
sameer.name = "sameer"
print(sameer.salary , sameer.language, sameer.name)

# the __init__ function is a special method (also called a dunder method 
# because of the double underscores) that acts like a constructor in object-oriented programming.
# It initializes an object when a class is created.
# It sets up initial values for the object’s attributes.
# It is automatically called right after an object is created with the ClassName() syntax.

class Programmer:
    company = "Google"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    
employe1 = Programmer("suhail", 120000, 311001) 
print(employe1.name, employe1.salary, employe1.pin)   

employe2 = Programmer("sachin", 100000, 340912)
print(employe2.name, employe2.salary, employe2.pin, employe2.company)


class Train:
    
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def book(self,  fro, to):
        print(f"the ticket is booked in {self.trainNo} from {fro} to {to}")
    
    def getStatus(self):
        print(f"the train which number {self.trainNo} is running on time.")
    
    def getFare(self, fro, to):
        print(f"the fare of train which number is {self.trainNo} from {fro} to {to} is {randint(100,500)}")
    

person = Train(9118292)
person.book("bhilwara", "manali")  
person.getStatus()
person.getFare("bhilwara", "manali")  
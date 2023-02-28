class Person:
    def __init__(self, firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
        
    def printname(self):
         print(self.firstname,self.lastname)

p1=Person("Tanvir","Anik")
p1.printname()
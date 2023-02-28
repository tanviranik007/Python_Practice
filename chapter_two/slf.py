class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name=name
        mysillyobject.age=age
        
    def myfunc(abc):
        print("Hello My name is"+" " +abc.name)
        
    
p1=Person('Anik',24)
p1.myfunc()
class Person:
    #create a new person,new person is an object of class person
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

newPerson=Person("Ghazi","Ali")
#print(newPerson)
#print(newPerson.fname)
#print(newPerson.lname) 

anotherOne=Person("first","last")
#print(anotherOne.fname)
#print(anotherOne.lname)
newPerson.fname="Cris"
newPerson.lname="Ronaldo"
#print(newPerson.fname)
#print(newPerson.lname)


#del Person.fname
#print(newPerson.fname)
#print(newPerson.lname)

del newPerson
print(newPerson)

#performance, scalable, maintainable,easy to troubleshoot and understand
class person:       #person is a datatype now bcz class is a datatype
    pass

obj=person()
print(type(obj))
obj.fname="Ashmita"     #object level encapsulation
obj.lname="Sarkar"
print(obj.fname,obj.lname)

obj1=person()
print(type(obj))
obj1.fname="Rahul"
obj1.lname="Yadav"
obj1.city="Jalandar"
print(type(obj1))
print(obj1.fname,obj1.lname,obj1.city)

class person():
    city="Bangalore"
    def sayhi(p):
        print("Hi "+p.fname+" "+p.lname)
obj1=person()
obj1.fname="Rahul"
obj1.lname="Yadav"
obj1.city="Jalandar"

obj2=person()
obj2.fname="Ashmita"     #object level encapsulation
obj2.lname="Sarkar"
person.city = "Bokaro"  #changes the value in the attribute city
print(obj2.fname,obj2.lname,obj2.city)
print(person.city)

obj3=obj1.__class__()       #new object created with reference of old object
obj3.fname="Akhil"
obj3.lname="Pemmaraju"
print(obj3.fname)

obj4=person()
obj4.fname="Sajal"
obj4.lname="Gupta"
person.sayhi(obj4)
person.sayhi(obj2)
obj1.__class__.sayhi(obj1)
obj3.sayhi()       #translated to person.sayhi(obj3)
obj4.sayhi()

def setVal(o,f,l):
    o.fname=f
    o.lname=l
class person1():
    def sayhi1(p):
        print("Hi "+p.fname+" "+p.lname)

obj5=person1()
setVal(obj5, "Ashmita","Sarkar")
obj6=person1()
setVal(obj6, "Abhijeet","Kumar")
obj5.sayhi1()
obj6.sayhi1()

class person1():
    def sayhi1(p):
        print("Hi "+p.fname+" "+p.lname)

    def setVal(o, f, l):
        o.fname = f
        o.lname = l
    #def __init__(o1,f1,l1):
    #   o1.fname=f1
    #    o1.lname=l1

obj5=person1()
obj5.setVal("Ashmita","Sarkar")
obj6=person1()
obj6.setVal("Abhijeet","Kumar")
obj5.sayhi1()
obj6.sayhi1()
#obj7=person("Rahul","Yadav")
#obj8=person("Sajal","Gupta")
#obj7.sayhi()
#obj8.sayhi()

#destructor
class person2:
    def sayhi1(p):
        print("Hi "+p.fname+" "+p.lname)
    def __init__(o1,f1,l1):
        o1.fname = f1
        o1.lname = l1
    def __del__(self):
        print("Destructor called for "+self.fname+" "+self.lname)
obj7=person2("Sajal","Gupta")
obj8=person2("Akhil","Pemmaraju")
obj7.sayhi1()
obj8.sayhi1()
obj7.__del__()
obj8.__del__()
del obj7    #we cannot delete objects ourselves, so the variables can be deleted from the stack
del obj8    #obj8.sayhi1() throws an error as the variable is deleted

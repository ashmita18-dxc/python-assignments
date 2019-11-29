class person:
    team="Angular"
    def sayhi(self):
        print("Hi "+self.fname+" "+self.lname)
    def __init__(superman,fname,lname):
        superman.fname=fname
        superman.lname=lname

class employee(person):     #class inheritence
    org="DXC"
    def work(obj):
        print(obj.fname+" is working!")

e1=employee("Akhil","Pemmaraju")        #constructor inheritence
#e1.fname="Akhil"
#e1.lname="Pemmaraju"
e1.work()
e1.sayhi()
print(e1.org,e1.team)

#2
class person:
    team="Angular"
    def sayhi(self):
        print("Hi "+self.fname+" "+self.lname)
    def __init__(superman,fname,lname):
        superman.fname=fname
        superman.lname=lname

class employee(person):         #single inheritence
    org="DXC"
    def __init__(superman,fname,lname,dpt,loc):
        #super.__init__(fname,lname)-->problematic in multiple and hybrid inheritence
        person.__init__(superman,fname,lname)   #calls the constructors of parent class
        superman.dpt=dpt
        superman.loc=loc
    def work(obj):
        print(obj.fname+" is working!")
class manager(employee):        #multilevel inheritence
    def __init__(self,fname,lname,dpt,loc,reportees):
        employee.__init__(self, fname, lname,dpt,loc)  # calls the constructors of parent class
    def manage(self):
        print(self.fname + " is managing!!")

class student(person):
    institute="Python Institute"        #hierarchial inheritence
    def __init__(self,fname,lname,stream):
        person.__init__(self,fname,lname)
        self.stream=stream
    def study(self):
        print(self.fname+" is not studying!!")

class intern(student,employee):     #hybrid inheritence
    def __init__(self,fname,lname,stream,dpt,loc):
        student.__init__(self,fname,lname,stream)
        employee.__init__(self,fname,lname,dpt,loc)

e1=manager("Akhil","Pemmaraju","DTC","Bengaluru",[])
e1.work()
e1.sayhi()
e1.manage()
print(e1.__dict__)

e2=student("Sajal","Gupta","Java")
e2.sayhi()
e2.study()
print(e2.__dict__)

e3=intern("Rahul","Yadav","Angular","DTC","Bengaluru")
e3.study()
e3.sayhi()

print(employee.__bases__)       #to get the name of parent class
print(person.__bases__)
print(manager.__bases__)

#incase of multiple inheritence, the priority is given to the order of parent classes mentioned-->mro(method resolution ordering
class A:
    def sayhi(self):
        print("Hi from A")
class B(A):
    def sayhi(self):
        print("Hi from B")
class C(B,A):       #mro error-->if the two classes have parent-child, then write child class first
    pass

ec=C()
ec.sayhi()
A.sayhi(ec)



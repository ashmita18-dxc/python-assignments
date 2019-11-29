#ability to take more than one forms
#function overloading--passing same function, with different number of arguments
def add(a,b):
    return a+b
print(add(1,2))
print(add(1.87,2.23))
print(add("Hello","World"))
print(add([],[]))

class person:
    team="Angular"
    def sayhi(self):
        print("Hi "+self.fname)
    def __init__(o,f):
        o.fname=f
    def __int__(self):      #gets ability to behave like integer
        return len(self.fname)
    def __str__(self):      #gets ability to behave like string
        return '{fname}'.format(**self.__dict__)
    def __bool__(self):
        return bool(self.fname)

p1=person("Akhil")
print(bool(p1))
print(int(p1))
print(str(p1))

p2=person("")
print(bool(p2))

#operator overloading
class box:
    def __init__(self,itemlist):
        self.itemlist=itemlist
    def __str__(self):
        return str(self.itemlist)
    def __add__(self, other):
        newitems=self.itemlist+other.itemlist
        b=box(newitems)
        return b
    def __gt__(self, other):
        return len(self.itemlist)>len(other.itemlist)

b1=box(["item1","item2"])
b2=box(["item3","item4","item5"])
print(b1)
print(b2)
b3=b1+b2
print(b3)
print(b1<b2)


class person:
    team="Angular"
    def sayhi(self):
        print("Hi "+self.fname+" "+self.lname)
    def __init__(o1,f1,l1):
        o1.fname = f1
        o1.lname = l1
obj=person("Ashmita","Sarkar")
setattr(obj,"pan","ASDFGHJKL123456")
print(obj.pan)
print(getattr(obj,"pan"))
print(hasattr(obj,"pan"))
delattr(obj,"pan")
print(hasattr(obj,"pan"))

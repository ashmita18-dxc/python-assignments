#unparameterised
def greetings():
    print("Hi All")
greetings()
greetings()

#parameterised
def sayhello(name1,name2):
    print("Hi "+name1+" "+name2)
sayhello("Ashmita","Sarkar")        #positional arguments

#return type function
def helloagain(name1,name2):
    return(name1+" "+name2)
data=helloagain("Ashmita","Sarkar")
print("Name: ",data)

#keyworded argument
def hii(name1,name2):
    print("Hi "+name1+" "+name2)
hii(name2="Ashmita",name1="Sarkar")

#mixture
def sayhellonames(name1,name2,name3,name4):
    print("Hi "+name1+" "+name2+" "+name3+" "+name4)
sayhellonames("Ashmita",name2="Bangali",name3="Sarkar",name4="Blah")   #first give all the positional, then the other

#default arguments
def sayhellonamesagain(name1,name3,name4,name2="Bangali"):
    print("Hi "+name1+" "+name2+" "+name3+" "+name4)
sayhellonamesagain("Ashmita",name2,name3="Sarkar",name4="Blah")   #first give all the positional, then the other

#anonymous fn,inline fn,lambda fn
#1:fn should contain only one line
#2. the one line should be return statement

#def sayhi(n1,n2):
#    print("Hi "+n1+" "+n2)

data=(lambda n1,n2: ("Hoo "+n1+" "+n2)) ("Ashmita","Sarkar")
print(data)
inline=lambda n1,n2: ("Moo "+n1+" "+n2)
print(type(inline))
print(inline("Rahul","Yadav"))
print(inline("Akhil","Pemmaraju"))
print(inline("Lakshit","Tandon"))

#function2
again=lambda a,b:(a+b)
print(again(2,3))

#function3-->mapping to lambda
mymap=lambda temp:(32+temp*9/5)
print(mymap(22))

#function4-->filter to lambda
obj=[
    {
    'fname':"Rahul",
    'lname':"Yadav",
    'city':"pata nahi..kabhi bolta hun UP kabhi Punjab"
    },
    {
    'fname':"Lakshit",
    'lname':"Tandon",
    'city':"Ahmedabad"
    },
    {
    'fname':"Akhil",
    'lname':"Pemmaraju",
    'city':"Mumbai"
    },
    {
    'fname':"Sajal",
    'lname':"Gupta",
    'city':"Gwalior"
    },
    {
    'fname':"Rhitik",
    'lname':"Khanna",
    'city':"Delhi(EAST)"
    },
    {
    'fname':"Ashmita",
    'lname':"Sarkar",
    'city':"Bokaro"
    }
]
myfilter=lambda element:element["fname"]=="Akhil"
newobj=filter(myfilter,obj)
for i in newobj:
    print(i)


ng="Hello World!"
print(len(ng))
print(ng.index("o"))
print(ng.index("o",5))       #starts from index5 to end
print(ng.index("o",5,8))     #7 is excluded
print(ng.count("1"))
print(ng.upper())
print(ng.lower())
print(ng.startswith("Hello"))
print(ng.endswith("d!"))
words=(ng.split(" "))
print(words)
print(ng.find("o"))
print(ng.find("o",5))
print(ng.find("o",5,7))
print(ng.replace("World","Python"))

#template string
data="I am a {0} from {1}"
sub1="String"
lang="Python"
print(data.format(sub1,lang))
#keyworded args
temp='"Hello {fname} {lname}, welcome to {city}"'
aString=temp.format(fname="Sajal",lname="Gupta",city="bhaad")
print(aString)
#dictionary split
ob={
    'fname':"Rahul",
    'lname':"Yadav",
    'city':"pata nahi..kabhi bolta hun UP kabhi Punjab"
}

dataString='"Hello I am {fname} {lname}.. I come from {city}"'.format(**ob)
print(dataString)

#assignment
ob1=[
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
    }
]
for i in ob1:
    dataString1 = '"Hello I am {fname} {lname}.. I come from {city}"'.format(**i)
    print(dataString1)


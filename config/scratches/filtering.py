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
def myFilter(element):
    return element["fname"].startswith("A")
newobj=filter(myFilter,obj)
print(type(newobj))
for i in newobj:
    print('{fname} {lname}'.format(**i))

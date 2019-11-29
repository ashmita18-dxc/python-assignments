list1=['a','b','c','d','e','f']
print(len(list1))
#print(sum(list1))      only for list of integers
print(max(list1))
print(min(list1))
list1.append('g')
print(list1)
list2=['h','i','j','k']
list1.extend(list2)
print(list1)
list1.insert(2,'z')
print(list1)
list1.pop(2)
print(list1)
list1.pop()
print(list1)
list1.reverse()
print(list1)
list1.sort(reverse=True)
print(list1)
#dictionary sorting
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
def mysort(element):
    return element["fname"]
ob1.sort(key=mysort)
print(ob1)



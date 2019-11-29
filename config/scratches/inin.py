#tuple of a tuple
t=(
    (1,2),
    (3,4),
    (5,6)
)
print(t[0])
print(t[0][0])
print(t[1][0])

#tuple of list
tol=(
    [1,2],
    [3,4],
    [5,6]
)
print(tol[0])
print(tol[0][0])
print(tol[1][0])
tol[0][0]=100
print(tol)

#tuple of set
tos=(
    {1,2},
    {3,4},
    {5,6}
)
print(tos)

#tuple of dictionary
tod=(
    {
   'fname':"Ashmita",
   'lname':"Sarkar"
    },
    {
   'fname':"Rahul",
   'lname':"Yadav"
    },
    {
   'fname':"Lakshit",
   'lname':"Tandon"
    }
)
print(tod)
print(tod[0].values())

#set of tuple
sot={
    (1,2),
    (3,4)
}
print(sot)

#set of dictionary cannot be formed


#list of tuples
lot=[
    (1,2),
    (3,4),
    (5,6)
]
print(lot[0])
print(lot[0][0])
print(lot[1][0])

#dictionary of tuple
dot={
    (1,2):"Sachin",     #tuples as keys
    (2,3):"Sourav",
    (3,4):"Rahul"
}
print(dot)

#list of dictionary
lod=[
    {
        'fname': "Ashmita",
        'lname': "Sarkar"
    },
    {
        'fname': "Rahul",
        'lname': "Yadav"
    },
    {
        'fname': "Lakshit",
        'lname': "Tandon"
    }
]
print(lod)

#dictionary of dictionary
dod={
        'fname': "Ashmita",
        'lname': "Sarkar",
        'address':{
            'house':"4057",
            'sector':"4A",
            'pin':"827004"
        }
}
print(dod['address']['sector'])

#converting list to dictionary
li=[["A",1],["B",2],["C",3]]    #list of list
print(dict(li))

#list of set to dictionary
los=[{"A",1},{"B",2},{"C",3}]
print(dict(los))
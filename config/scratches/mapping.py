obj1=[22,32,19,43]
def mymap(element):
    return 32+element*9/5
newobj1=map(mymap,obj1)
print(type(newobj1))

for i in newobj1:
    print(i)

#
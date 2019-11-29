data=1,2,3.4,True,None,"Hello"
print(type(data))
print(data[0])
print(data[-1])
print(data[::-1])
print(data[-1][::-1])

#changing tuples
#data[5]="Python"        tuple-items cannot be editted-->immutable
data=1,2,3      #a new tuple object is created
print(data)

#List
data1=[1,2,3.4,False,"Python"]
print(type(data1))
data1[1]=1000   #list is mutable
print(data1)

data2=(2,)  #creating tuple with single entry
print(type(data2))
data3=[2]   #creating list with single entry
print(type(data3))



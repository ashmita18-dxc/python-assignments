#SET
s={False,None,"Hello",1,"Sachin"}  #1 and true are considered duplicate of each other
print(type(s))
print(s)

s1={1,2,3,4}
s2={3,4,5,6}
s3={1,2}
print(s1|s2)    #union
print(s1&s2)    #intersection
print(s1-s2)    #difference
print(s2-s1)    #difference
print(s3<s2)    #subset
print(s3<s1)    #subset

#in python, all immutable objects are hash-able
#set can contain only hash-able objects

#DICTIONARY
d={
    'fname':"Ashmita",
   'lname':"Sarkar"
}

d['batch']="Angular"
print(type(d))
print(d['fname'])
print(d['batch'])
#dictionary maintains set of keys

#datatype conversion
l1=[1,1,2,5,3,76,3]
s1=set(l1)
print(s1)   #the order of the items will be lost
print(list(s1))

str1="hello"
print(type(str1))
s2=list(str1)
print(s2)



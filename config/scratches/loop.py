#while
i=0
while i<=10:
    print(i)
    i+=1
else:
    print("Loop Exhausted!!")   #doesn't execute if we break out of the loop

#factors
number=int(input('Enter a number: '))
i=2
count=0
sum=0
while i<=number/2:
    if number % i == 0:
        print(i)
        count+=1
    i += 1

else:
    if(count>0):
        print("Not Prime")
    else:
        print("Prime")

#for loop
data="Hello Python"
for d in data:
    print(d)

data1=(1,2,3.4,True,None,"Hello")
for d1 in data1:
    print(d1)

data2={
    'fname': "Ashmita",
    'lname': "Sarkar"
    }
for d2 in data2:
    print(data2.values())

#for in range
data=range(100,200,5)       #range is a datatype
print(type(data))
for d in data:
    print(d)

#prime
num=int(input("Enter a number: "))
for i in range(2,num):
    if num%i==0:
        print("Not Prime")
        break
else:
    print("Prime")





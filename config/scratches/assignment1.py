#pattern1
line=int(input('Enter number of lines: '))
for i in range(0,line):
    print(" ")
    for j in range(0,i+1):
        print("*",end=" ")
#pattern2
for i in range(0,line):
    print("* "*i)
    print()
    for i in range(line-1,-1,-1):
        print("* "*i)

#pattern3
num=int(input("Enter a number: "))
sum=0
for i in range(1,num):
    print(i)
    sum+=i
    


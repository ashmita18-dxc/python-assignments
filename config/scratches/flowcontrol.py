#if-else
a=int(input('Enter 1st number: '))
b=int(input('Enter 2nd number: '))
c=int(input('Enter 3rd number: '))
if a>b and a>c:
        print(a)
else:
    if b>c:
        print(b)
    else:
        print(c)

#assignment2
marks=int(input('Enter marks: '))
if marks>0 and marks<=100:
    if marks>=0 and marks<=39:
        print("FAIL!!!")
    elif marks>=40 and marks<=59:
        print("Third")
    elif marks>=60 and marks<=79:
        print("Second")
    else:
        print("First")
else:
    print("INVALID MARKS!!!")


#year assignment
year=int(input('Enter year: '))
if year%400==0:
    print("Leap Year")
elif year%100==0:
    print("Not a leap year")
elif year%4==0:
    print("Leap Year")
else:
    print("Not a leap year")


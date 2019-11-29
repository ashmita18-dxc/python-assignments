days={
    "1":"Friday",
    "2":"Saturday",
    "3":"Sunday",
    "4":"Monday",
    "5":"Tuesday",
    "6":"Wednesday",
    "0":"Thursday"
}
date=int(input("Enter: "))
mod=date%7
print(days[str(mod)])

#factors list
number=int(input("Enter number: "))
factors=[]
for i in range(1,number+1):
    if(number%i==0):
        factors.append(i)
print(factors)

#square list
print(list(map(lambda el:el**2,range(2,11))))







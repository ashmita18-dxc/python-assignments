#global and local variables
data = "Hello.. I am a global variable to the function"     #global variable
def demo():
    print(data)
demo()

def local():
    data1="Hello.. I am a local variable to the function"   #local variables deleted once function is executed
    print(data1)
local()

#2
data4="Hello You"
def outer():
    print(data4)
    def inner():
        print(data4)
    inner()
outer()

#function as datatype
def demo1():
    print("Hello World")

#test=demo()    return of demo is passed
test=demo1    #reference of demo is passed
print(type(test))
test()

def demo2():
    print("Hello")

def caller(a):
    print(type(a))
    print("Inside Caller")
    a()
caller(demo2)

#nested function
def demo3():
    print("Outer")
    def inner():
        print("Inner")
    inner()
demo3()

#number of times a function is called-->lexical reference
def call():
    count=0
    def callagain():
        nonlocal count      #non local can only be called inside a nested function
        count+=1
        print(count)
    return callagain
hello=call()
hello()
hello()
call()
hello()
hello()

#wallet functions
def wallet():
    balance=300;

    def deposit():
        nonlocal balance
        deposit = int(input("Enter depositing amount: "))
        balance += deposit
        print("Available balance: " + str(balance))

    def withdrawl():
        nonlocal balance
        withdraw = int(input("Enter withdrawing amount: "))
        if withdraw < balance:
            balance -= withdraw
            print("Available balance: " + str(balance))
        else:
            print("Insufficient Balance")

    def view():
        nonlocal balance
        print("Available Balance: " + str(balance))
    return {"deposit":deposit, "withdrawl":withdrawl, "view":view}

print("1.Deposit  2.Withdraw  3.View")
a = int(input("Enter choice: "))

final = wallet()
if a==1:
    final["deposit"]
elif a==2:
    final["withdrawl"]
elif a==3:
    final["view"]

#swapping
a=2
b=4
c=9
t=[b,c,a]
a,b,c=(b,c,a)
print(t)










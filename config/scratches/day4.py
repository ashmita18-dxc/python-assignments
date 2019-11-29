#1
def outer(a):
    #print("This is out!")
    def inner():
        print("This is in!")
        print(type(a))
        a()
        print("Done!!")
    return inner
def hello():
    print("Hello World")

demo=outer(hello)       #demo contains inner function->inner function contains hello->so a() implies to hello()
demo()
print("--------------------------")

#2
def outer(a):
    #print("This is out!")
    def inner():
        print("This is in!")
        print(type(a))
        a()
        print("Done!!")
    return inner
def hello():
    print("Hello World")
def sayhi():
    print("Say Hii!!")

demo1=outer(hello)  #demo1 contains inner function->inner function contains hello->so a() implies to hello()
demo1()
demo2=outer(sayhi)  #demo2 contains inner function->inner function contains sayhi->so a() implies to sayhi()
demo2()
print("---------------------------------")

#same kind of business logic to be executed before and after a function-->wrapping is done-->closure is used to give values to the inner function
def outer(a):
    #print("This is out!")
    def inner():
        print("This is in!")
        #print(type(a))
        a()
        print("Done!!")
    return inner
def hello():
    print("Hello World")
def sayhi():
    print("Say Hii!!")

hello=outer(hello)
sayhi=outer(sayhi)
hello()
sayhi()
print("---------------------------------")

#4
def outer(a):
    #print("This is out!")
    def inner():
        print("This is in!")
        #print(type(a))
        a()
        print("Done!!")
    return inner
@outer                          #wrapper class is also called decorator
def hello():
    print("Hello World")
@outer
def sayhi():
    print("Say Hii!!")

hello()
sayhi()
print("---------------------------------")

#5
def outer(a):
    def inner(*args,**kwargs):      #the decorators can take variable number of arguments, so the inner function is made generic
        a(*args,**kwargs)
        print("Done!!")
    return inner
@outer                          #wrapper class is also called decorator
def hello(name):
    print("Hello "+name)
@outer
def sayhi(name1,name2):
    print("Hii "+name1+" "+name2)

hello("Akhil")
sayhi("Rahul","Yadav")
print("---------------------------------")

#6
def allstrings(a):
    def inner(*args,**kwargs):
        for i in args:
            if type(i)!=str:
                print("Invalid")
                break
        else:
            for i in kwargs.values():
                if type(i)!=str:
                    print("Invalid")
                    break
            else:
                a(*args, **kwargs)
        print("Done!!")
    return inner
@allstrings                          #wrapper class is also called decorator
def hello(name):
    print("Hello "+name)
@allstrings
def sayhi(name1,name2):
    print("Hii "+name1+" "+name2)

hello("Rahul")
sayhi("Lakshit","Tandon")
hello(1234)
sayhi(True)
print("---------------------------------")
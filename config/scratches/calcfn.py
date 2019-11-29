#for variable number of positional arguments
def add(*spiderman):
    print(type(spiderman))
    print(spiderman)
    sum=0
    for x in spiderman:
        sum+=x
    print(spiderman,sum)

add(1,2)
add(1,2,3,4)

#variable length with keyworded arguments
def sayhi(**keyargs):
    print(type(keyargs),keyargs)

sayhi(name1="Ashmita")
sayhi(name1="Sajal",name2="Akhil")
sayhi(name1="Rahul",name2="Lakshit",name3="Rhitik")

#for mixture of arguments-->def mixture(*args,**keywargs)-->generic function
def mixtures(*args,**keyargs):
    print(type(keyargs),keyargs)
    print(type(args),args)

mixtures(1,2,3,4,fname="Ashmita",lname="Sarkar")

#
def sayhii(n1,n2,n3):
    print("Hii "+n1+" "+n2+" "+n3)

li=["Sachin","Sourav","Rahul"]
sayhii(*li)
tu=("Sachin","Sourav","Rahul")
sayhii(*tu)
set={"Sachin","Sourav","Rahul"}
sayhii(*set)
di={"n1":"Sachin","n2":"Sourav","n3":"Rahul"}
sayhii(**di)
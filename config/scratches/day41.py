#error handling
try:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    div = a / b
    print(z)
except ZeroDivisionError as e:
    print("Second number cannot be zero")
except ValueError as ve:
    print("Please enter a valid value")
except Exception as ee:  # generic exception handler-->handles all kind of exception-->parent class for all other exception
    print("Genereic Error")            #parent exception class should always be mentioned at last
print("data: ",div)

#example2-->manually raising exception
try:
    names=["Sachin","Sourav","Rahul"]
    name=input("Enter a name: ")
    if name not in names:
        raise Exception("Name not found...")
except ValueError as ve:
    print("Khela hocche eikhaaneee???!!!")

#example3-->custom exception class
class NameNotFound(Exception):      #NameNotFound is child of Exception class
    def __init__(self,msg="Name not found"):
        Exception.__init(self,msg)
try:
    names = ["Sachin", "Sourav", "Rahul"]
    name = input("Enter a name: ")
    if name not in names:
        raise NameNotFound
except NameNotFound as ne:
    print("Khela hocche eikhaaneee???!!!")

# Assignment
    username = {
        "Ashmita": "asarkar34",
        "Akhil": "apemmaraju76",
        "Lakshit": "ltandon56",
        "Rahul": "ryadav77",
        "Sajal": "sgupta22"
    }


    class UserNotFound(Exception):
        def __init__(self, message="Username not found..."):
            Exception.__init__(self,message)
    class InvalidPassword(Exception):
        def __init__(self1,message1="Password is wrong!!"):
            Exception.__init__(self1,message1)
    try:
        user=input("Enter username: ")
        if user in username:
            try:
                password = input("Enter password: ")
                if username[user] == password:
                    print("Login Successful")
                else:
                    print("Wrong password")
            except InvalidPassword as ie:
                print(ie)
        else:
            print("Invalid Username")
    except UserNotFound as unf:
        print(unf)



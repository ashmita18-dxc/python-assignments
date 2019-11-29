data=True
print(data)
print(type(data))

string="""This is a multi
            line string"""
print(string)

#Datatype Conversion
string="Hello"
print(bool(string))    #Empty string gives false(falsy values), space gives true

number=1
print(bool(number))    #0 gives false-->falsy value

decimal1=123.45
decimal2=str(decimal1)
print(type(decimal2))

data1="123.45"
print(int(float(data1)))    #due to decimal point, string needs to be converted to float first and then integer

data2="123hello"
#print(int(data2))
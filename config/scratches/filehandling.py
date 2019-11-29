#with open('demo.txt','w') as fo:
fo=open('demo.txt','w')
fo.write("Hello Akhil \n")
fo.write("Hello Ashmita \n")
fo.write("Hello Lakshit \n")
fo.write("Hello Rahul \n")
fo.write("Hello Rhitik \n")
fo.write("Hello Sajal \n")
fo.close()

#read
fo1=open('demo.txt','r')
print("First:",fo1.read(2))        #reads only first 3 characters
print("Second:",fo1.read(2))        #reads next 3 characters
print("Third:",fo1.readline())      #reads whole character
for line in fo1:
    print(line)
fo1.close()
#to do read and write together-->r+/w+/a+
#r+-->if file not found, error
#w+-->if file not found, creates file but cannot append
#a+-->if file not found, creates file and appends in it

fo2=open('demo.txt','rb')
print(fo2.readline())        #reads only first 3 characters
for line in fo2:
    print(line.decode(),end="")
fo2.close()

with open('demo.txt','wb') as fo3:
    fo3.write("Hello \n".encode())
    fo3.write("Hii \n".encode())
    fo3.write("Hola \n".encode())
    fo3.close()

#for reading again:
fo=open('demo.txt','rb')
print("cursor at ",fo.tell())
for line in fo:
    print(line.decode(),end="")
print("Cursor at ",fo.tell())
print("Reading again:")
fo.seek(0,0)
print("Cursor at ",fo.tell())
for line in fo:
    print(line.decode(),end="")
fo.close()



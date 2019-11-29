#assignment1
#reading a file
fo1=open('dog1.jpg','rb')
data=fo1.read()
fo1.close()

#writing a file
fo2=open('dog2.jpg','wb')
fo2.write(data)
fo2.close()

#assignment2
fo3=open('demo.txt','rb')
data1=fo3.read()
fo3.close()

fo4=open('chunks/demo1.txt','rb')
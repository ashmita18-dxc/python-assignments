import os
print(os.name)
stat=os.stat("dog1.jpg")
print(stat)
print(stat.st_size)
print(stat.st_atime)
print(stat.st_mtime)
print(stat.st_ctime)
#os.system("echo "hi"")
print("-------------------------------------------")

os.system('echo "hi"')
os.system('dir')
#os.system('calc.exe')       #opens calculator
#os.system('notepad os1.py')     #opens the file in notepad
#os.system('python os1.py')
print("-------------------------------------------")

import os.path
filename="C://Users//asarkar34//Documents//assessment-5.txt"
print(os.path.split(filename))
print(os.path.splitext(filename))
print(os.path.dirname(filename))       #parent directory name
print(os.path.basename(filename))    #filename
print(os.path.exists(filename))     #if file exists-->true
print(os.path.isabs(filename))      #if absolute-->true
print(os.path.isdir(filename))      #if directory-->true
print(os.path.isfile(filename))     #if file-->true
print(os.path.islink(filename))
print("---------------------------------------------")

'''
environment variables
print(os.environ(environment name))
os.environ['User']="root
varPath='usr/$User/appdata'
actPath=os.path.expandvars(varPath)
print(actPath)
'''

#assignment--
#os.makedirs("Assign/folder")
#os.makedirs("Assign/folder2")
os.chdir(str(os.getcwd()+"/Assign"))
fo=open('demo1.txt','a')
fo.write("demo1")
fo=open('demo2.txt','a')
fo.write("demo2")
a=os.listdir()
for i in a:
    extension=os.path.splitext(i)
    if extension[1]=='.txt':        #[1]-->splitext() splits the demo1.txt into a tuple (demo1,txt)
        print(i)






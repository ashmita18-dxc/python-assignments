import os
print(os.listdir())     #files in the present directory
print(os.listdir("C://Users//asarkar34//Documents//workspace-spring-tool-suite-4-4.4.0.RELEASE"))   #files in other directory
print(os.getcwd())      #current working directory
#os.chdir("C://Users//asarkar34")            #change directory
filename='demo.txt'
#os.makedirs("test/multiple/levels")
os.removedirs("test/multiple/levels")
os.remove(filename)
#os.mkdir("test")
#os.rmdir("test")

import day42
print(day42.data)
p1=day42.person("Ashmita")
p1.hi()

#not import everything
from day42 import demo,person
demo()
p2=person("Ashmita")
p2.hi()
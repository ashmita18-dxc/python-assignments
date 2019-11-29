'''
REGULAR EXPRESSIONS
WILD CARDS:
a* -->0 or more occurrence of a
a+ --> 1 or more occurs of a
a? --> 0 or 1 a
^a --> starts with a
a$ --> ends with a
QUANTIFIERS:
a{5}-->5 times a
a(5,7}-->accepts number of a's in the  {a,b} including both a(min reqd) and b(max reqd)
a{5,} --> extracts maximum number of continuous a's
[abcd]-->string which has a or b or c or d matches this pattern-->[a-b]
[a-zA-Z]-->all alphabets match this
[a-zA-Z0-9]-->alphanumeric values match this
[^abcd]-->[^a-d]-->accepts anything other than a or b or c or d
\s-->for space
^[0-9]{10}$-->for mobile validation
'''
import re
pattern='this'
text="Does this word occur in my text?"
print((pattern,text))
print(re.search(pattern,text))
if re.search(pattern,text):     #if no match found, none value generated, which is then converted to false by bool()-->falsey value
    print ("found a match")
else:
    print("no match")

pattern1='t[a-z]*'
text1="Would you like to have tea to go?"
print((pattern1,text1))
print(re.search(pattern1,text1))
match=re.search(pattern1,text1)
if match:     #if no match found, none value generated, which is then converted to false by bool()-->falsey value
    print ("found a match")
    match.end()
    text[match.start():match.end()]
else:
    print("no match")
print("--------------------------------")

pattern1='\st[a-z]*'
text1="Would you like to have tea to go?"
#print(re.search(pattern1,text1))
matches=re.finditer(pattern1,text1)
for match in matches:
    print(match.start(),match.end(),text[match.start():match.end()])
print("---------------------------------")

pattern1='t[a-z]*'
text1="Tom, what time do you drink tea?"
matches1=re.findall(pattern1,text1, re.I)       #re.I ignores the upper or lower case
print(matches1)
print("----------------------------------")

#assignment
val="^[0-9]{10}$"
mobile=str(input("Enter mobile number: "))
if(re.search(val,mobile)):
    print("Correct number")
else:
    print("Khelaa hocchee eikhanee")
print("----------------------------------")

import os
email="^[a-zA-Z0-9]*@[a-z]*[.][a-z]*"
os.chdir("C://Users//asarkar34//.PyCharmCE2019.2//config//scratches//Assign")
open1=os.listdir()
for i in open1:
    if os.path.splitext(i)[1]=='.log':
        f = open("C://Users//asarkar34//.PyCharmCE2019.2//config//scratches//Assign/"+i, 'r')
        m=re.finditer(email,f, re.)
        print(m)








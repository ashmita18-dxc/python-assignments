from requests import get
from bs4 import BeautifulSoup
url="http://www.moneycontrol.com/"
response=get(url)
print(response.text)
soup=BeautifulSoup(response.text,'html.parser')
'''lxml'''
print(type(soup))
print(soup.html.head.title)
anchor=soup.find_all('a')
print(anchor)
#links=soup.find_all('a',attrs={'title':'Global Markets'})
#print(links)
for link in anchor:
    print(link.get('href'))
print("---------------------------------")
tables=soup.find_all('table',class_="rhsglTbl")
for table in tables:
    links=table.find_all('a')
    print(links)
#print(tables)

from requests import get
from bs4 import BeautifulSoup
url="http://www.moneycontrol.com/"
response=get(url)
soup=BeautifulSoup(response.text,'html.parser')
tables=soup.find(attrs={'id':'tlNifty'},class_="rhsglTbl")


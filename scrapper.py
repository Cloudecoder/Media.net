
from bs4 import BeautifulSoup
import pandas as pd
import requests
page_count=int(input("enter pages"))

ph_name=[]
ph_price=[]
ph_rating=[]


for i in range(1,page_count+1):
    url="https://www.amazon.in/s?k=mobile&i=electronics&crid=1QKI8R9TVMUQG&sprefix=mobile%2Celectronics%2C1406&ref=nb_sb_noss_"+str(i)
    req=requests.get(url)
    content=BeautifulSoup(req.content, 'html.parser')
    name=content.find_all('span',{"class":"a-size-medium a-color-base a-text-normal"})
    price=content.find_all('span',{"class":"a-price-whole"})
    rating=content.find_all('span',{"class":"a-size-base s-light-weight-text"})

    for i in name:
        print(i.text)
        ph_name.append(i.text)
    for i in price:
        print(i.text)
        ph_price.append(i.text)
    for i in rating:
        print(i.text)
        ph_rating.append(i.text)
data={"phone name":ph_name,"phone price":ph_price,"phone rating":ph_rating}
df=pd.DataFrame(data)
print(df)  

   

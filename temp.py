# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q="
query = input("Enter the product you want to search for: ")
query = query.replace(" ","%20")
url = url+query
source = requests.get(url).content
soup = BeautifulSoup(source,'lxml')
names = soup.findAll('a',{'class':'_2cLu-l'})
for item in names:
	print(item.text)
rating = soup.findAll("div",{"class":"hGSR34 _2beYZw"})
price = soup.findAll("div",{"class":"_1vC4OE"})
for i,j,k in zip(names,rating,price):
	print(i.text,j.text,k.text)
import requests 
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


page_link = 'https://www.investing.com/commodities/crude-oil' #load page with priceof crude oil from Inwesting

response = requests.get(page_link, headers = {'User-Agent': UserAgent().chrome})  #create response with fake user for antiban effect
html = response.content

soup = BeautifulSoup( html, 'html.parser')     # structuring data

obj = soup.find('span', attrs = { 'id' : 'last_last'})    # get data use tag <span> and id = last_last from price page

print (obj.text)

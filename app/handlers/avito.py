import re

import requests
from bs4 import BeautifulSoup
from requests.api import patch

city = "vladikavkaz"
marka = input("Marka: ")
model = input("Model: ")
radius = 0

url = f"https://www.avito.ru/{city}/avtomobili/{marka}/{model}?radius={radius}"
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
main_container = soup.find_all('div',class_= re.compile('iva-item-body*'))




for index, content in enumerate(main_container):
    
    ad_post = content.find("div", {"data-marker": "item-line"})
    if ad_post==None:
        title_info = content.find('a',class_=re.compile('iva-item-title*'))['title'].split(',')
        town_info = content.find('div',class_=re.compile('geo-root*')).find('span').text
        
        car_info = title_info[0]
        was_created = title_info[1]
        city_on_sale = town_info

        print(f"{index+1}. {car_info} - {was_created}. {city_on_sale}")

  


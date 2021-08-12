# aiogram
from ast import parse
from aiogram import types
from aiogram.types.message import ParseMode
from bot import dp
from bot import db


# python
import re
import requests
from bs4 import BeautifulSoup

# default для mvc
city = "vladikavkaz"
radius = 0
allowed_data = ['часов', 'часа','час']
@dp.message_handler(commands='avito')
async def avito_list(message: types.Message):
    splited_message = message.text.split()
    marka = splited_message[1]
    model = splited_message[2]


    url = f"https://www.avito.ru/{city}/avtomobili/{marka}/{model}?radius={radius}"
    response = requests.get(url)
    print(response.status_code)
    soup = BeautifulSoup(response.text,'lxml')
    main_container = soup.find_all('div',class_= re.compile('iva-item-content*'))




    for index, content in enumerate(main_container):
        contaier_of_content = content.find("div",class_=re.compile("iva-item-body*"))
        
        ad_post = contaier_of_content.find("div", {"data-marker": "item-line"})
        
        if ad_post==None:
            fresh_car = contaier_of_content.find("div",{"data-marker":"item-date"}).text.split()[1]
            
            if fresh_car in allowed_data: # проверка на сегодняшний день
            
                title_info = contaier_of_content.find('a',class_=re.compile('iva-item-title*'))['title'].split(',')
                town_info = contaier_of_content.find('div',class_=re.compile('geo-root*')).find('span').text
                link = content.find('a', class_=re.compile('iva-item-sliderLink*'))['href']
                car_info = title_info[0]
                was_created = title_info[1]
                city_on_sale = town_info
                
                await message.answer(f"{car_info} - {was_created}. {city_on_sale}\n<a>https://avito.ru{link}</a>",parse_mode=ParseMode.HTML)
                
                

 
  


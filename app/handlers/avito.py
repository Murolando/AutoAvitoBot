# aiogram
from aiogram import types
from aiogram.types.message import ParseMode
from bot import dp
from bot import db
from aiogram.utils.markdown import hbold, hlink

# user agent
from fake_useragent import UserAgent

# python
import re
import requests
from bs4 import BeautifulSoup

# default для mvc
city = "vladikavkaz"
radius = 100
allowed_data = ['часов', 'часа','час']

@dp.message_handler(commands='avito')
async def avito_list(message: types.Message):
    # Проверим есть ли вообще подписки
    if db.follows_exists(message.from_user.id):

        # Выводим все объявления по подпискам
        follows = db.show_subs(message.from_user.id)

        for follow in follows:
            line = follow[1][0][0]

            with db.connection:
                marka = db.cursor.execute(f"SELECT `avito_mark_name` FROM `marks` WHERE `name` = ?", (line,)).fetchall()
                marka = marka[0][0]

            min_price = follow[2][0][0]
            if follow[3][0][0] == None:
                max_price = follow[2][0][0]*1000
            else:
                max_price = follow[3][0][0]
            #model = "2114_samara"
            #url = f"https://www.avito.ru/{city}/avtomobili/{marka}/{model}?radius={radius}"
            ua = UserAgent()
            url = f"https://www.avito.ru/{city}/avtomobili/{marka}?radius={radius}"
            headers = {
                'User-Agent': f'{ua.google}',
            }
            response = requests.get(url, headers = headers)
            print(response.status_code)
            soup = BeautifulSoup(response.text,'lxml')
            check_empty = False
            main_container = soup.find_all('div',class_= re.compile('iva-item-content*'))

            for index, content in enumerate(main_container):
                contaier_of_content = content.find("div",class_=re.compile("iva-item-body*"))

                ad_post = contaier_of_content.find("div", {"data-marker": "item-line"})

                if ad_post==None:
                    fresh_car = contaier_of_content.find("div",{"data-marker":"item-date"}).text.split()[1]
                    price = content.find('span', class_=re.compile('price-price-*')).find('meta', itemprop="price")[
                        'content']

                    if fresh_car in allowed_data and int(price) <= max_price and int(price) >= min_price: # проверка на сегодняшний день и на подхождение по цене

                        check_empty = True
                        
                        title_info = contaier_of_content.find('a',class_=re.compile('iva-item-title*'))['title'].split(',')
                        town_info = contaier_of_content.find('div',class_=re.compile('geo-root*')).find('span').text
                        datePost_info = contaier_of_content.find('div',class_=re.compile('iva-item-dateInfo*')).find('div').text
                        link = content.find('a', class_=re.compile('iva-item-sliderLink*'))['href']

                        currency = content.find('span', class_=re.compile('price-price-*')).find('meta')['content']
                        car_info = title_info[0]
                        was_created = title_info[1]
                        city_on_sale = town_info

                        card = f'{hlink(car_info+" - "+was_created,"https://avito.ru"+link)}\n' \
                            f'{hbold("Город: ", city_on_sale)}\n' \
                            f'{hbold("Цена: ", price, currency)}'
                        
                        await message.answer(card)

            #Проверка на то, что есть ли какие то автомобили по нужной цене
            if not check_empty:
                await message.answer("Нету автомобилей с нужной вам ценой")

    else:
        await message.answer("У вас нет ни одной подписки")




 
  


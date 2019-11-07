from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.get('https://www.mvideo.ru/televizory-i-video')
time.sleep(5)

###  Когда входишь на страницу через хромдрайвер появлется всплывающее окно, его можно закрыть 2 способами:
### - крестиком, данная кнопка имеет clsaa =button = driver.find_element_by_class_name('PushTip-close')
### - через кнопку понятно - button = driver.find_element_by_class_name('PushTip-button')

print('Вход на страницу МВИДЕО')

while True:
    try:
        button = WebDriverWait(driver,40).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'PushTip-close'))
        )
        button.click()
    except Exception as e:
        print('Не было всплывающего окна')
        break
### Ограничиавам количество прохоодв не более 3 раз, такак е ясно сколько там товаров и страниц

pages = 1
while pages<4:
    try:
        button = WebDriverWait(driver,50).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'sel-hits-button-next'))
        )

        button.click()
        pages +=1
        print(f'переход на страницу {pages} произведен')
    except Exception as e:
        print(e)
        break



goods = driver.find_elements_by_class_name('accessories-product-list')
goods_list = []
goods_dict = {}
for good in goods:
    time.sleep(10)
    good_dict['descr'] = good.find_element_by_class_name('sel-product-tile-title').text
    good_dict['link'] = good.find_element_by_class_name('sel-product-tile-title').get_attribute('href')
    good_dict['price'] = good.find_element_by_class_name('sel-product-tile-price').text
    goods_list.append(goods_dict)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['MVIDEO']
letters = db.letters

for i in goods_list:
    letters.insert_one(i)

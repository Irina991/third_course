from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://e.mail.ru/login')

assert "Вход - Почта Mail.ru" in driver.title



elem.send_keys('contestbook@mail.ru')
elem.send_keys(Keys.RETURN)
assert "Вход - Почта Mail.ru" in driver.title


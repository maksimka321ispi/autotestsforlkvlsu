from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get('https://lk.www1.vlsu.ru/Account/Login')

username=browser.find_element(by=By.NAME, value='Login')
username.send_keys('pepespepes123')

password=browser.find_element(by=By.ID, value='Password')
password.send_keys('***')

button = browser.find_element(By.NAME, "loginBtn")
button.click()

try:
    assert 'Анкета студента – Личный кабинет ВлГУ' in browser.title
    assert "Корнюшин Максим Николаевич" in browser.page_source
    print('Тест на авторизацию успешно пройден')
except Exception as err:
    print('Тест на авторизацию провален')

browser.close()
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
    print('Авторизован')
except Exception as err:
    print('Не авторизован')


link = browser.find_element(By.XPATH, "//a[text()='Расписание преподавателей']")
link.click()

teacher = browser.find_element(by=By.ID, value='FIO')
teacher.send_keys('Хлызова Валерия Григорьевна')
buttons = browser.find_element(by=By.ID, value='searchBtn')
buttons.click()

browser.implicitly_wait(10)

link = browser.find_element(by=By.CSS_SELECTOR, value="a.btn.btn-success")
link.click()

try:
    assert "Хлызова Валерия Григорьевна" in browser.page_source
    print('Тест на просмотр расписания преподавателя пройден успешно')
except Exception as err:
    print('Тест на просмотр расписания преподавателя провален')

browser.close()
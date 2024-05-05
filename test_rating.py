from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


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


link = browser.find_element(By.ID, "RatingList")
link.click()

select_element = browser.find_element(By.ID, value="Semesters")

select = Select(select_element)
browser.implicitly_wait(2)

select.select_by_visible_text("3")

try:
    selected_option = select.first_selected_option
    assert selected_option.text == '3'
    print('Тест на просмотр рейтинг-контроля успешно пройден')
except Exception as err:
    print('Тест на просмотр рейтинг-контроля не пройден')

browser.close()
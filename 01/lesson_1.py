# 1. Сейчас мы будем эмулировать действия пользователя в браузере
# 2. Узнать версию гугл хрома
# 3. Качаем архив с версией под нужную ОС (вебдрайвер)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from auth_data import username, password
import random


def login(username, password):
    try:
        browser = webdriver.Chrome('E:\PycharmProjects\\Insta\\01\\chromedriver.exe')
        browser.get('https://www.instagram.com')



        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

        browser.close()
        browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


login(username, password)
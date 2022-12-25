# 1. Сейчас мы будем эмулировать действия пользователя в браузере
# 2. Узнать версию гугл хрома
# 3. Качаем архив с версией под нужную ОС (вебдрайвер)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from auth_data import username, password
import random
from selenium.webdriver.common.by import By

def login(username, password):
    try:
        driver = webdriver.Chrome('E:\PycharmProjects\\Insta\\01\\chromedriver.exe')
        driver.get('https://www.instagram.com')



        time.sleep(random.randrange(3, 5))

        username_input = driver.find_element(By.NAME, 'username')
        username_input.clear()             # очистим на всякий случай поле
        username_input.send_keys(username)     # вводим

        time.sleep(2)

        password_input = driver.find_element(By.NAME, 'password')

        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

        driver.close()
        driver.quit()

    except Exception as ex:
        print(ex)
        driver.close()
        driver.quit()


login(username, password)
from auth_data import username, password
from selenium import webdriver
import time, random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def login(username, password):
    browser = webdriver.Chrome('../chromedriver')
    browser.implicitly_wait(5)
    browser.get('http://www.instagram.com')
    time.sleep(random.randrange(2,7))

    username_input = browser.find_element(By.NAME, "username")
    username_input.clear()
    username_input.send_keys(username)

    time.sleep(random.randrange(1,3))

    password_input = browser.find_element(By.NAME, 'password')
    password_input.clear()
    password_input.send_keys(password)

    password_input.send_keys(Keys.ENTER)
    # login_button = browser.find_element(By.CSS_SELECTOR,'button[type="submit"]')
    # login_button.click()

    time.sleep(20)



    browser.close()
    browser.quit()


login(username,password)


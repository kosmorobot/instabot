from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from auth_data import username, password
import time
import random


def hashtag_search(username, password,hashtag):
    browser = webdriver.Chrome('../chromedriver')

    try:
        browser.get('http://www.instagram.com')
        time.sleep(random.randrange(3,5))

        username_input = browser.find_element(By.NAME, 'username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(5)

            hrefs = browser.find_elements(By.TAG_NAME, 'a')

            posts_urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]
            print(posts_urls)

            # posts_urls = []
            # for item in hrefs:
            #     href = item.get_attribute('href')
            #     if "/p/" in href:
            #         posts_urls.append('href')
            #         print(href)

            for url in posts_urls[0:1]:
                browser.get(url)

                like_button = browser.find_element('/html/body/div[14]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button/div[1]/svg').click()
                time.sleep(5)


            browser.close()
            browser.quit()
        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


hashtag_search(username, password, 'guitar')


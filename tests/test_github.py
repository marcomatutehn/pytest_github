import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SCROLL_PAUSE_TIME = 0.5


def test_pytest_guthub():
    driver = webdriver.Chrome(executable_path='../pythonProject/drivers/chromedriver')

    driver.get('http://github.com')
    driver.maximize_window()

    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys("react")
    search_box.send_keys(Keys.ENTER)

    driver.execute_script("window.scrollTo(0, 500)")

    btn_advance_search = driver.find_element(By.CSS_SELECTOR, 'a.f6')
    btn_advance_search.click()

    time.sleep(SCROLL_PAUSE_TIME)

    driver.close()

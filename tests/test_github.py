from selenium import webdriver


def test_pytest_guthub():
    chrome_driver = webdriver.Chrome(executable_path='../pythonProject/drivers/chromedriver')

    chrome_driver.get('http://github.com')
    chrome_driver.maximize_window()

    chrome_driver.close()

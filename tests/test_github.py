from selenium import webdriver

driver = webdriver.Chrome(executable_path='../pythonProject/drivers/chromedriver')

driver.get('http://www.google.com')


driver.close()

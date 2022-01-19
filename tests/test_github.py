import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SCROLL_PAUSE_TIME = 50


# Selectors
class GitHubAutomation:
    def test_pytest_guthub(self):
        driver = webdriver.Chrome(executable_path='../pythonProject/drivers/chromedriver')

        driver.get('http://github.com')
        driver.maximize_window()

        txt_search_box = driver.find_element(By.NAME, 'q')
        txt_search_box.send_keys("react")
        txt_search_box.send_keys(Keys.ENTER)

        driver.execute_script("window.scrollTo(0, 500)")

        btn_advance_search = driver.find_element(By.CSS_SELECTOR, 'a.f6')
        btn_advance_search.click()

        dd_search_language = driver.find_element(By.ID, 'search_language')
        dd_search_language.click()

        lbl_javascript = driver.find_element(By.XPATH, '//*[@id="search_language"]/optgroup[1]/option[13]')
        lbl_javascript.click()

        dd_search_state = driver.find_element(By.ID, 'search_state')
        dd_search_state.click()
        lbl_state = driver.find_element(By.XPATH, '//*[@id="search_state"]/option[3]')
        lbl_state.click()

        txt_search_stars = driver.find_element(By.ID, 'search_stars')
        txt_search_stars.send_keys(">45")

        txt_search_followers = driver.find_element(By.ID, 'search_followers')
        txt_search_followers.send_keys(">50")

        dd_search_license = driver.find_element(By.ID, 'search_license')
        dd_search_license.click()

        lbl_license = driver.find_element(By.XPATH, '//*[@id="search_license"]/optgroup[1]/option[10]')
        lbl_license.click()

        driver.execute_script("window.scrollTo(0, 500)")

        btn_search = driver.find_element(By.XPATH, '//*[@id="search_form"]/div[2]/div/div/button')
        btn_search.click()
        # Verify the repository
        # Verify that the result list includes this repository: `mvoloskov/decider`
        btn_repository = driver.find_element(By.XPATH,
                                             '//*[@id="js-pjax-container"]/div/div[3]/div/ul/li/div[2]/div[1]/div[1]/a')
        btn_repository.click()

        btn_readme = driver.find_element(By.XPATH,
                                         '//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[5]/div[2]/span/a')
        btn_readme.click()

       # readme_text = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/div[2]/div/div/readme-toc/div/div[2]/article')
        # Review this part
        #readme_text.text
        #print("Result : " + readme_text)

        time.sleep(SCROLL_PAUSE_TIME)

        driver.close()


githubautomation = GitHubAutomation()
githubautomation.test_pytest_guthub()

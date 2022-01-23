import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SCROLL_PAUSE_TIME = 0.5

# Selectors
EXECUTABLE_PATH = '../pythonProject/drivers/chromedriver'
URL_GITHUB = 'http://github.com'

TXT_SEARCHBOX = 'q'
TXT_SEARCHBOX_KEYS = "react"

BTN_ADVANCE_SEARCH = 'a.f6'

DD_SEARCH_LANGUAGE = 'search_language'

LBL_JAVASCRIPT = '//*[@id="search_language"]/optgroup[1]/option[13]'

DD_SEARCH_STATE = 'search_state'

LBL_STATE = '//*[@id="search_state"]/option[3]'

TXT_SEARCH_STARS = 'search_stars'
TXT_SEARCH_STARS_KEYS = ">45"

TXT_SEARCH_FOLLOWERS = 'search_followers'
TXT_SEARCH_FOLLOWERS_KEYS = ">50"

DD_SEARCH_LICENSE = 'search_license'

LBL_LICENSE = '//*[@id="search_license"]/optgroup[1]/option[10]'

BTN_SEARCH = '//*[@id="search_form"]/div[2]/div/div/button'

LBL_REPOSITORY_NUMBER = '//*[@id="js-pjax-container"]/div/div[2]/nav[1]/a[1]/span'
LBL_REPOSITORY_NAME = '//*[@id="js-pjax-container"]/div/div[3]/div/ul/li/div[2]/div[1]/div[1]/a'

BTN_REPOSITORY = '//*[@id="js-pjax-container"]/div/div[3]/div/ul/li/div[2]/div[1]/div[1]/a'

BTN_README = '//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[5]/div[2]/span/a'

BTN_RAWURL = 'raw-url'

LBL_README_TEXT = '/html/body/pre'


class GitHubAutomation:

    def test_pytest_guthub(self):
        driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH)

        driver.get(URL_GITHUB)
        driver.maximize_window()
        time.sleep(3)
        txt_search_box = driver.find_element(By.NAME, TXT_SEARCHBOX)
        txt_search_box.send_keys(TXT_SEARCHBOX_KEYS)
        txt_search_box.send_keys(Keys.ENTER)

        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1.5)
        btn_advance_search = driver.find_element(By.CSS_SELECTOR, BTN_ADVANCE_SEARCH)
        btn_advance_search.click()
        time.sleep(1.5)
        dd_search_language = driver.find_element(By.ID, DD_SEARCH_LANGUAGE)
        dd_search_language.click()

        lbl_javascript = driver.find_element(By.XPATH, LBL_JAVASCRIPT)
        lbl_javascript.click()

        dd_search_state = driver.find_element(By.ID, DD_SEARCH_STATE)
        dd_search_state.click()
        lbl_state = driver.find_element(By.XPATH, LBL_STATE)
        lbl_state.click()

        txt_search_stars = driver.find_element(By.ID, TXT_SEARCH_STARS)
        txt_search_stars.send_keys(TXT_SEARCH_STARS_KEYS)

        txt_search_followers = driver.find_element(By.ID, TXT_SEARCH_FOLLOWERS)
        txt_search_followers.send_keys(TXT_SEARCH_FOLLOWERS_KEYS)

        dd_search_license = driver.find_element(By.ID, DD_SEARCH_LICENSE)
        dd_search_license.click()

        lbl_license = driver.find_element(By.XPATH, LBL_LICENSE)
        lbl_license.click()

        driver.execute_script("window.scrollTo(0, 500)")

        btn_search = driver.find_element(By.XPATH, BTN_SEARCH)
        btn_search.click()

        # Verify the repository
        assert "1" in driver.find_element(By.XPATH, LBL_REPOSITORY_NUMBER).text

        # Verify that the result list includes this repository: `mvoloskov/decider`
        assert "mvoloskov/decider" in driver.find_element(By.XPATH,
                                                          LBL_REPOSITORY_NAME).text

        btn_repository = driver.find_element(By.XPATH,
                                             BTN_REPOSITORY)
        btn_repository.click()
        btn_readme = driver.find_element(By.XPATH,
                                         BTN_README)
        btn_readme.click()
        time.sleep(1.5)

        btn_rawurl = driver.find_element(By.ID, BTN_RAWURL)
        btn_rawurl.click()

        readme_text = driver.find_element(By.XPATH, LBL_README_TEXT).text

        print("\n\n=======================================================")
        print("\n\nTITLE: First 300 characters (WITH space) of readme:")
        readme_str_withspace = readme_text[0:299]
        print("\n" + readme_str_withspace)
        print("\n\n=======================================================")

        print("\n\n=======================================================")
        print("\n\nTITLE: First 300 characters (WITHOUT space) of readme:")
        readme_text_withouspace = readme_text.replace(" ", "")
        readme_str_withoutspace = readme_text_withouspace[0:299]
        print("\n" + readme_str_withoutspace)
        print("\n\n=======================================================")
        time.sleep(SCROLL_PAUSE_TIME)

        driver.close()


githubautomation = GitHubAutomation()
githubautomation.test_pytest_guthub()

import pyperclip
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    text_title_xpath= "//h1[1]"

    def confirmHomePage(self):
        return self.driver.find_element(By.XPATH, self.text_title_xpath).text
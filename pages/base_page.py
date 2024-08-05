from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, browser):
        self.browser = browser


    def open_home_page(self):
        self.browser.get("https://sbis.ru/")

    def find_element(self, args):
        # wait = WebDriverWait(self.browser, 10)
        # return wait.until(EC.visibility_of_element_located(args))
        return self.browser.find_element(*args)

    def find_elements(self, args):
        return self.browser.find_elements(*args)

    def find_element_in_block(self, block, by, value):
        return block.find_element(by, value)

    def find_elements_in_block(self, block, by, value):
        return block.find_elements(by, value)
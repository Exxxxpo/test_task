from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, browser):
        self.browser = browser


    def open_home_page(self):
        self.browser.get("https://sbis.ru/")

    def find(self, args):
        return self.browser.find_element(*args)

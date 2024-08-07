from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def close_cookie_agreement_footer(self):
        wait = WebDriverWait(self.browser, 20)
        cookie_alert_close = wait.until(EC.element_to_be_clickable(BasePageSelectors.footer_cookie_agriement_selector))
        cookie_alert_close.click()

    def open_home_page(self):
        self.browser.get("https://sbis.ru/")
        self.close_cookie_agreement_footer()

    def find_element(self, args):
        return self.browser.find_element(*args)

    def find_elements(self, args):
        return self.browser.find_elements(*args)

    def find_element_in_block(self, block, by, value):
        return block.find_element(by, value)

    def find_elements_in_block(self, block, by, value):
        return block.find_elements(by, value)


class BasePageSelectors:
    footer_cookie_agriement_selector = (By.CLASS_NAME, 'sbis_ru-CookieAgreement__close')

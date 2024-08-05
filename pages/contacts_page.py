from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.tenzor_page import TenzorPage


button_selector = (By.LINK_TEXT, 'Контакты')
logo_tensor_selector = (By.XPATH, "//a[@href='https://tensor.ru/' and @class='sbisru-Contacts__logo-tensor mb-12']")
tensor_block_4_selector = (By.CSS_SELECTOR, "div.tensor_ru-Index__block4-content.tensor_ru-Index__card")
tensor_block_4_selector_text = (By.XPATH, ".//p[contains(text(), 'Сила в людях')]")


class ContactsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def button_contacts(self):
        return self.find_element(button_selector)

    @property
    def logo_tenzor(self):
        return self.find_element(logo_tensor_selector)

    @property
    def logo_tenzor_click(self):
        self.logo_tenzor.click()
        self.browser.switch_to.window(self.browser.window_handles[1]) # переходим на открывшуюся вкладку
        return self.browser

    # @staticmethod
    def tenzor_block_4_open(browser):
        """
        На главной странице переходит в раздел контакты, затем кликает по логотипу tenzor
        :param browser:
        :return: current_page возвращает объект страницы TenzorPage
        """
        current_page = BasePage(browser)
        current_page.open_home_page()
        current_page = ContactsPage(current_page.browser)
        current_page.button_contacts.click()
        current_page = TenzorPage(current_page.logo_tenzor_click)
        return current_page






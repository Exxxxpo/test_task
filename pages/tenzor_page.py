from pages.base_page import BasePage
from selenium.webdriver.common.by import By


logo_tensor_selector = (By.XPATH, "//a[@href='https://tensor.ru/' and @class='sbisru-Contacts__logo-tensor mb-12']")
tensor_block_4_selector = (By.CSS_SELECTOR, "div.tensor_ru-Index__block4-content.tensor_ru-Index__card")
tensor_block_4_selector_text = (By.XPATH, ".//p[contains(text(), 'Сила в людях')]")
tensor_block_4_about_link_click_selector = (By.LINK_TEXT, "Подробнее")

class TenzorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # @property
    # def logo_tenzor(self):
    #     return self.find(logo_tensor_selector)
    #
    # def logo_tenzor_click(self):
    #     self.logo_tenzor.click()
    #     self.browser.switch_to.window(self.browser.window_handles[1])  # переходим на открывшуюся вкладку
    #     return self.browser

    @property
    def tensor_block_4(self):
        result_block = self.find(tensor_block_4_selector)
        self.browser.execute_script("arguments[0].scrollIntoView();", result_block)  # скролим до нужного блока
        return result_block

    @property
    def tensor_block_4_text(self):
        return self.tensor_block_4.find_element(*tensor_block_4_selector_text)

    @property
    def tensor_block_4_about_link(self):
        return self.tensor_block_4.find_element(*tensor_block_4_about_link_click_selector)

    @staticmethod
    def tensor_block_4_about_link_click(browser):
        current_page = TenzorPage(browser)
        current_page.tensor_block_4_about_link.click()
        return current_page

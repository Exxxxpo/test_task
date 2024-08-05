from pages.base_page import BasePage
from selenium.webdriver.common.by import By


tensor_block_4_selector = (By.CSS_SELECTOR, "div.tensor_ru-Index__block4-content.tensor_ru-Index__card")
tensor_block_4_selector_text = (By.XPATH, ".//p[contains(text(), 'Сила в людях')]")
tensor_block_4_about_link_click_selector = (By.LINK_TEXT, "Подробнее")

class TenzorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)


    @property
    def tensor_block_4(self):
        result_block = self.find_element(tensor_block_4_selector)
        self.browser.execute_script("arguments[0].scrollIntoView();", result_block)  # скролим до нужного блока
        return result_block

    @property
    def tensor_block_4_text(self):
        return self.find_element_in_block(self.tensor_block_4, *tensor_block_4_selector_text)

    @property
    def tensor_block_4_about_link(self):
        return self.find_element_in_block(self.tensor_block_4, *tensor_block_4_about_link_click_selector)


    # @staticmethod
    def tensor_block_4_about_link_click(browser):
        current_page = TenzorPage(browser)
        current_page.tensor_block_4_about_link.click()
        return current_page

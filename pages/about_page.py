from pages.base_page import BasePage
from selenium.webdriver.common.by import By


work_block_selector = (By.CSS_SELECTOR, ".tensor_ru-container.tensor_ru-section.tensor_ru-About__block3")
images_block_selector = (By.CSS_SELECTOR, '.tensor_ru-About__block3-image.new_lazy')


class AboutPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def work_block(self):
        result_block = self.find_element(work_block_selector)
        self.browser.execute_script("arguments[0].scrollIntoView();", result_block)
        return result_block

    def images_block(self):
        return self.find_elements_in_block(self.work_block, *images_block_selector)

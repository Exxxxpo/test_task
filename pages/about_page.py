from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AboutPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def find_tensor_block_3(self):
        result_block = self.find_element(AboutPageSelectors.tensor_block_3_selector)
        self.browser.execute_script("arguments[0].scrollIntoView();", result_block)
        return result_block

    def find_tensor_block_3_images(self):
        return self.find_elements_in_block(self.find_tensor_block_3, *AboutPageSelectors.tensor_block_3_images_selector)


class AboutPageSelectors:
    tensor_block_3_selector = (By.CSS_SELECTOR, ".tensor_ru-container.tensor_ru-section.tensor_ru-About__block3")
    tensor_block_3_images_selector = (By.CSS_SELECTOR, '.tensor_ru-About__block3-image.new_lazy')

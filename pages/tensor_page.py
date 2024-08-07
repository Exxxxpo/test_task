from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class TensorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def find_tensor_block_4(self):
        result_block = self.find_element(TensorPageSelectors.tensor_block_4_selector)
        self.browser.execute_script("arguments[0].scrollIntoView();", result_block)  # скролим до нужного блока
        return result_block

    @property
    def find_tensor_block_4_text(self):
        return self.find_element_in_block(self.find_tensor_block_4, *TensorPageSelectors.tensor_block_4_selector_text)

    @property
    def find_tensor_block_4_about_link(self):
        return self.find_element_in_block(self.find_tensor_block_4,
                                          *TensorPageSelectors.tensor_block_4_about_link_click_selector)

    def click_tensor_block_4_about_link(self):
        self.find_tensor_block_4_about_link.click()
        return TensorPage(self.browser)

    def close_cookie_agreement_footer(self):
        wait = WebDriverWait(self.browser, 20)
        cookie_alert_close = wait.until(EC.element_to_be_clickable(TensorPageSelectors.tensor_cookie_agreement))
        cookie_alert_close.click()
        return TensorPage(self.browser)


class TensorPageSelectors:
    """
    Селекторы используемые в TenzorPage
    """
    tensor_block_4_selector = (By.CSS_SELECTOR, "div.tensor_ru-Index__block4-content.tensor_ru-Index__card")
    tensor_block_4_selector_text = (By.CSS_SELECTOR, ".tensor_ru-Index__card-title.tensor_ru-pb-16")
    tensor_block_4_about_link_click_selector = (By.LINK_TEXT, "Подробнее")
    tensor_cookie_agreement = (
        By.CSS_SELECTOR,
        ".tensor_ru-CookieAgreement__close.icon-Close.ws-flex-shrink-0.ws-flexbox.ws-align-items-center")

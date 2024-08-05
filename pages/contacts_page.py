from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.tenzor_page import TenzorPage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


button_selector = (By.LINK_TEXT, 'Контакты')
logo_tensor_selector = (By.XPATH, "//a[@href='https://tensor.ru/' and @class='sbisru-Contacts__logo-tensor mb-12']")
tensor_block_4_selector = (By.CSS_SELECTOR, "div.tensor_ru-Index__block4-content.tensor_ru-Index__card")
tensor_block_4_selector_text = (By.XPATH, ".//p[contains(text(), 'Сила в людях')]")
contacts_top_block_selector = (By.CSS_SELECTOR, ".sbis_ru-container.sbisru-Contacts__relative")
contacts_top_block_link_region_selector = (By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text.sbis_ru-link")
contacts_list_partners_selector = (By.CSS_SELECTOR, ".sbisru-Contacts-List__city.sbisru-text--standart.sbisru-Contacts__text--500.sbisru-Contacts__text--md-xm.pl-24.pl-xm-0.pt-16.pt-xm-12.pb-4.pb-xm-8.ws-flexbox.ws-justify-content-between.ws-align-items-start")
region_panel_list_selector = (By.CSS_SELECTOR, ".sbis_ru-Region-Panel__list-l")
change_region_selector = (By.CSS_SELECTOR, "span[title='Камчатский край']")
contacts_top_block_link_region_click_wait = (By.CSS_SELECTOR, ".controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-Search__nativeField_caretEmpty.controls-Search__nativeField_caretEmpty_theme_sbisru.controls-InputBase__nativeField_hideCustomPlaceholder")


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

    @property
    def contacts_top_block(self):
        """
        Верхний блок в разделе контакты, содержащий смену региона
        """
        return self.find_element(contacts_top_block_selector)

    @property
    def contacts_top_block_link_region(self):
        """
        Ссылка на смену региона в разделе Контакты.
        """
        return self.find_element_in_block(self.contacts_top_block, *contacts_top_block_link_region_selector)

    @property
    def contacts_list_partners(self):
        """
        Блок партнеров в разделе Контакты.
        """
        return self.find_element(contacts_list_partners_selector)

    def contacts_top_block_link_region_click(self):
        """
        Кликает по смене региона в разделе "Контакты".
        """
        self.contacts_top_block_link_region.click()

    @property
    def region_panel_list(self):
        """
        Блок регионов в панели смены региона.
        """
        elems = self.find_element(region_panel_list_selector)
        return elems

    def change_region(self):
        """
        Меняет регион на Камчатский край
        """
        self.find_element_in_block(self.region_panel_list, *change_region_selector).click()
        self.contacts_top_block_link_region

    def region_panel_list_wait(self):
        """
        Отлавливает "Загрузку" при клике на смену региона
        """
        self.find_element(contacts_top_block_link_region_click_wait)


    # def region_panel_list_wait(self):
    #     """
    #     Отлавливает "Загрузку" при клике на смену региона
    #     """
    #     # self.find_element(contacts_top_block_link_region_click_wait)
    #     wait = WebDriverWait(self.browser, 30)  # Увеличим время ожидания
    #     loading_indicators = [
    #         (By.CLASS_NAME, 'controls-loading-indicator_content'),
    #     ]
    #
    #     for indicator in loading_indicators:
    #         try:
    #             # Wait for the loading indicator to be present
    #             wait.until(EC.presence_of_element_located(indicator))
    #
    #             # Wait for the loading indicator to be invisible using different methods
    #             wait.until(EC.invisibility_of_element_located(indicator))
    #
    #             # Additional checks for visibility using JavaScript and CSS properties
    #             wait.until(lambda browser: not self.is_element_visible(browser, indicator))
    #         except TimeoutException:
    #             print(f'таймаут {indicator}')
    #             pass
    #
    # def is_element_visible(self, driver, locator):
    #     """
    #     Проверяет, виден ли элемент с помощью различных методов.
    #     """
    #     element = driver.find_element(*locator)
    #     if element.is_displayed():
    #         return False
    #
    #     style = element.get_attribute('style')
    #     if 'display: none;' in style or 'visibility: hidden;' in style:
    #         return False
    #
    #     # Проверка размера элемента
    #     size = element.size
    #     if size['width'] == 0 and size['height'] == 0:
    #         return False
    #
    #     # Использование JavaScript для проверки видимости
    #     return driver.execute_script("return arguments[0].offsetParent === null;", element)


    def contacts_click(self):
        """
        Переходит в раздел контакты
        """
        current_page = BasePage(self.browser)
        current_page.open_home_page()
        current_page = ContactsPage(current_page.browser)
        current_page.button_contacts.click()
        return current_page



    def tenzor_block_4_open(self):
        """
        В разделе контакты кликает по логотипу tenzor
        :param browser:
        :return: возвращает объект страницы TenzorPage
        """
        contacts_page = self.contacts_click()
        return TenzorPage(contacts_page.logo_tenzor_click)









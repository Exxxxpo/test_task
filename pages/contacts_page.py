from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.tenzor_page import TenzorPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


button_selector = (By.LINK_TEXT, 'Контакты')
logo_tensor_selector = (By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor.mb-12")
tensor_block_4_selector = (By.CSS_SELECTOR, ".s-Grid-col.s-Grid-col--6.s-Grid-col--sm12")
tensor_block_4_selector_text = (By.CSS_SELECTOR, ".tensor_ru-Index__card-title.tensor_ru-pb-16")
contacts_top_block_selector = (By.CSS_SELECTOR, ".sbis_ru-container.sbisru-Contacts__relative")
contacts_top_block_link_region_selector = (By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text.sbis_ru-link")
contacts_city_partners_selector = (By.CSS_SELECTOR, ".sbisru-Contacts-List__city.sbisru-text--standart.sbisru-Contacts__text--500.sbisru-Contacts__text--md-xm.pl-24.pl-xm-0.pt-16.pt-xm-12.pb-4.pb-xm-8.ws-flexbox.ws-justify-content-between.ws-align-items-start")
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
    def city_of_partners(self):
        """
        Город парнеров в разделе контакты
        """
        return self.find_element(contacts_city_partners_selector)

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
        return self.find_element(region_panel_list_selector)

    def change_region(self):
        """
        Меняет регион на Камчатский край
        """
        self.region_panel_list_wait()
        self.find_element_in_block(self.region_panel_list, *change_region_selector).click()


    def region_panel_list_wait(self):
        """
        Ждет пока появится поле ввода при смене региона
        """
        self.find_element(contacts_top_block_link_region_click_wait)

    def after_change_region_wait(self):
        """
        Ждет пока загрузится список партнеров после смены региона
        """
        wait = WebDriverWait(self.browser, 10)
        return wait.until(
            EC.text_to_be_present_in_element(contacts_city_partners_selector, "Петропавловск-Камчатский")
        )


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









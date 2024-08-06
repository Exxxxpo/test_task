import os
from settings import PROJECT_PATH
import time
import re


from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



footer_selector = (By.CSS_SELECTOR, '.sbisru-Footer__container')
footer_download_link_selector = (By.LINK_TEXT, 'Скачать локальные версии')
footer_download_selector = (By.PARTIAL_LINK_TEXT, 'Скачать (Exe')
# cookie_agriement_selector = (By.CSS_SELECTOR, '.sbisru-CookieAgreement__close.ws-flex-shrink-0.ws-flexbox.ws-align-items-center')
footer_cookie_agriement_selector =  (By.CLASS_NAME, 'sbis_ru-CookieAgreement__close')
test_selector = (By.LINK_TEXT, "Тарифы")

class DownloadPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)


    def find_footer(self):
        """
        Загружает футер.
        """
        return self.find_element(footer_selector)

    def click_footer_download_link(self):
        """
        Кликает по "Скачать локальные версии" в футере.
        """
        wait = WebDriverWait(self.browser, 20)
        link = wait.until(EC.element_to_be_clickable(footer_download_link_selector))
        link.click()


    def click_download_link(self):
        """
        Кликает по "Скачать Веб-установщик".
        """

        wait = WebDriverWait(self.browser, 20)
        link = wait.until(EC.element_to_be_clickable(footer_download_selector))
        link.click()


    def get_expires_size_file(self):
        """
        Возвращает размер файла, указанный в ссылке на сайте
        """
        wait = WebDriverWait(self.browser, 10)
        link = wait.until(EC.element_to_be_clickable(footer_download_selector))
        size_file = re.search(r'(\d+\.\d+)', link.text).group(0)  # запишем размер установщика из текста ссылки
        return size_file


    @staticmethod
    def check_downloading(timeout=120):
        """
        Проверяет, что файл загружен.
        """
        directory = os.path.join(PROJECT_PATH, 'tests')
        seconds = 0
        while seconds < timeout:
            time.sleep(1)
            for fname in os.listdir(directory):
                if fname == 'sbisplugin-setup-web.exe':
                    return True
            seconds += 1
        return False

    @staticmethod
    def check_size():
        """
        Возвращает размер файла в Мб.
        """
        file_path = os.path.join(PROJECT_PATH, 'tests/sbisplugin-setup-web.exe')
        file_size = round(os.path.getsize(file_path)/(1024**2), 2)
        return file_size
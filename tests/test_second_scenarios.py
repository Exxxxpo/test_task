import time

import config

from pages.contacts_page import ContactsPage
from pages.tenzor_page import TenzorPage
from pages.about_page import AboutPage
import pytest

#################################################################
# Поскольку алогоритмы проверки 1-ого сценария последовательные,
# то между тестами нет смысла закрывать драйвер
#################################################################

def test_contacts_region_correct(browser):
    """
    Регион определился верно
    """
    contacts_page = ContactsPage(browser).contacts_click()
    assert contacts_page.contacts_top_block_link_region.text == 'Свердловская обл.'


def test_contacts_list_partners_is_displayed(browser):
    """
    Проверка отображения списка партнеров
    """
    contacts_page = ContactsPage(browser).contacts_click()
    assert contacts_page.contacts_list_partners.is_displayed()
    assert contacts_page.contacts_list_partners.text == "Екатеринбург"


def test_change_region(browser):
    """
    Проверка смены региона
    """
    contacts_page = ContactsPage(browser).contacts_click()
    contacts_page.contacts_top_block_link_region_click()
    contacts_page.region_panel_list_wait()
    contacts_page.change_region()
    contacts_page.after_change_region_wait()
    assert contacts_page.contacts_top_block_link_region.text == 'Камчатский край'


def test_partners_after_change_region(browser):
    contacts_page = ContactsPage(browser)
    assert contacts_page.contacts_list_partners.is_displayed()
    assert contacts_page.contacts_list_partners.text == "Петропавловск-Камчатский"

def test_url_after_change_region(browser):
    contacts_page = ContactsPage(browser)
    assert contacts_page.browser.current_url == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'


def test_title_after_change_region(browser):
    contacts_page = ContactsPage(browser)
    assert contacts_page.browser.title == 'СБИС Контакты — Камчатский край'
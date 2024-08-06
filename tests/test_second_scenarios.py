import settings
from pages.contacts_page import ContactsPage


def test_contacts_region_correct(browser):
    """
    Регион автоматически опеределен верно.
    """
    contacts_page = ContactsPage(browser).click_contacts()
    assert contacts_page.find_link_change_region_in_contacts_block.text == 'Свердловская обл.'


def test_contacts_list_partners_is_displayed(browser):
    """
    Проверка отображения списка партнеров.
    """
    contacts_page = ContactsPage(browser)
    assert contacts_page.find_city_of_partners.is_displayed()
    assert contacts_page.find_city_of_partners.text == "Екатеринбург"


def test_change_region(browser):
    """
    Проверка смены региона.
    """
    contacts_page = ContactsPage(browser)
    contacts_page.click_to_change_region_in_contacts()
    contacts_page.change_region()
    contacts_page.wait_after_change_region()
    assert contacts_page.find_link_change_region_in_contacts_block.text == 'Камчатский край'


def test_partners_after_change_region(browser):
    """
    Проверка смены города в разделе "Партнеры".
    """
    contacts_page = ContactsPage(browser)
    assert contacts_page.find_city_of_partners.is_displayed()
    assert contacts_page.find_city_of_partners.text == "Петропавловск-Камчатский"

def test_url_after_change_region(browser):
    """
    URL корректно сменился после смены региона.
    """
    contacts_page = ContactsPage(browser)
    assert contacts_page.browser.current_url == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'


def test_title_after_change_region(browser):
    """
    Title корректно сменился после смены региона
    """
    contacts_page = ContactsPage(browser)
    assert contacts_page.browser.title == 'СБИС Контакты — Камчатский край'

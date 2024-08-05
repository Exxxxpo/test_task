import config

from pages.contacts_page import ContactsPage
from pages.tenzor_page import TenzorPage
from pages.about_page import AboutPage
import pytest

#################################################################
# Поскольку алогоритмы проверки 1-ого сценария последовательные,
# то между тестами нет смысла закрывать драйвер
#################################################################

def test_tenzor_block_4_is_displayed(browser):
    """
    Проверка отображения блока "Сила в людях" на странице контактов
    """
    tenzor_page = ContactsPage.tenzor_block_4_open(browser)
    assert tenzor_page.tensor_block_4.is_displayed()
    assert tenzor_page.tensor_block_4_text.text == 'Сила в людях'
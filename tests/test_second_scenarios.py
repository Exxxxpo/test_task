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
    Проверка отображения блока "Сила в людях" на странице контактов
    """
    contacts_page =
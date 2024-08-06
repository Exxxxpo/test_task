import settings

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
    contacts_page = ContactsPage(browser)
    tenzor_page = contacts_page.open_tenzor_block_4()
    assert tenzor_page.tensor_block_4.is_displayed()
    assert tenzor_page.tensor_block_4_text.text == 'Сила в людях'


def test_tensor_block_4_link_about_redirect(browser):
    """
    Проверка перехода по ссылке "Подробнее"
    """
    tenzor_page = TenzorPage(browser)
    about_page = TenzorPage.tensor_block_4_about_link_click(tenzor_page.browser) # переходим по ссылке "Подробнее"
    assert 'https://tensor.ru/about' == about_page.browser.current_url


def test_tensor_about_size_images(browser):
    """
    Проверка размеров изображений в разделе "Работаем"
    """
    about_page = AboutPage(browser)
    images = about_page.images_block() # список изображений в разделе "Работаем"
    first_image = images[0]
    for image in images[1:]:
        assert image.size['height'] == first_image.size['height']
        assert image.size['width'] == first_image.size['width']





if __name__ == "__main__":
    pytest.main()

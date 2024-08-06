import pytest
from pages.about_page import AboutPage
from pages.contacts_page import ContactsPage
from pages.tensor_page import TensorPage


@pytest.mark.usefixtures("logger")
def test_tensor_block_4_is_displayed(browser, logger):
    """
    Проверка отображения блока "Сила в людях" на странице контактов
    """
    logger.info(f"Начало теста {test_tensor_block_4_is_displayed.__name__}")
    contacts_page = ContactsPage(browser).click_contacts()
    tensor_page = TensorPage(contacts_page.click_logo_tensor)
    tensor_page = tensor_page.close_cookie_agreement_footer()
    assert tensor_page.find_tensor_block_4.is_displayed()
    assert tensor_page.find_tensor_block_4_text.text == 'Сила в людях'
    logger.info(f"Завершение теста{test_tensor_block_4_is_displayed.__name__}")


@pytest.mark.usefixtures("logger")
def test_tensor_block_4_link_about_redirect(browser, logger):
    """
    Проверка перехода по ссылке "Подробнее"
    """
    logger.info(f"Начало теста {test_tensor_block_4_is_displayed.__name__}")
    tensor_page = TensorPage(browser)
    about_page = tensor_page.click_tensor_block_4_about_link()
    logger.info(f"Перешли по ссылке 'Подробнее'")
    assert 'https://tensor.ru/about' == about_page.browser.current_url
    logger.info(f"Завершение теста{test_tensor_block_4_is_displayed.__name__}")


@pytest.mark.usefixtures("logger")
def test_tensor_about_size_images(browser, logger):
    """
    Проверка размеров изображений в разделе "Работаем"
    """
    about_page = AboutPage(browser)
    images = about_page.find_tensor_block_3_images()  # список изображений в разделе "Работаем"
    first_image = images[0]
    for image in images[1:]:
        assert image.size['height'] == first_image.size['height']
        assert image.size['width'] == first_image.size['width']

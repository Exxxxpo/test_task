from pages.about_page import AboutPage
from pages.contacts_page import ContactsPage
from pages.tensor_page import TensorPage


def test_tensor_block_4_is_displayed(browser):
    """
    Проверка отображения блока "Сила в людях", на странице tensor.ru
    """
    contacts_page = ContactsPage(browser).click_contacts()
    tensor_page = TensorPage(contacts_page.click_logo_tensor)
    tensor_page = tensor_page.close_cookie_agreement_footer()
    assert tensor_page.find_tensor_block_4.is_displayed()
    assert tensor_page.find_tensor_block_4_text.text == 'Сила в людях'


def test_tensor_block_4_link_about_redirect(browser):
    """
    Проверка перехода по ссылке "Подробнее"
    """
    tensor_page = TensorPage(browser)
    about_page = tensor_page.click_tensor_block_4_about_link()
    assert 'https://tensor.ru/about' == about_page.browser.current_url


def test_tensor_about_size_images(browser):
    """
    Проверка размеров изображений в разделе "Работаем"
    """
    about_page = AboutPage(browser)
    images = about_page.find_tensor_block_3_images()  # список изображений в разделе "Работаем"
    first_image = images[0]
    for image in images[1:]:
        assert image.size['height'] == first_image.size['height']
        assert image.size['width'] == first_image.size['width']

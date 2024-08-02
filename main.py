import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_navigate_to_contacts_and_click_tensor_banner(driver):
    driver.get("https://sbis.ru/")

    # Переход в раздел "Контакты"
    driver.find_element(By.LINK_TEXT, "Контакты").click()

    # Переход по логотипу на сайт tensor.ru
    tensor_logo_link = driver.find_element(
        By.XPATH, "//a[@href='https://tensor.ru/' and @class='sbisru-Contacts__logo-tensor mb-12']"
    ).click()

    # Переключение на новую вкладку
    driver.switch_to.window(driver.window_handles[1])

    # Открытие блока "Сила в людях"
    tensor_block_4 = driver.find_element(
        By.CSS_SELECTOR, "div.tensor_ru-Index__block4-content.tensor_ru-Index__card"
    )
    driver.execute_script("arguments[0].scrollIntoView();", tensor_block_4) # скролим до нужного блока

    # Проверка наличия текста "Сила в людях" внутри найденного блока
    tensor_block_4_text = tensor_block_4.find_element(By.XPATH, ".//p[contains(text(), 'Сила в людях')]")
    assert tensor_block_4_text.is_displayed()
    assert tensor_block_4_text.text == 'Сила в людях'


    contacts_link = tensor_block_4.find_element(By.LINK_TEXT, "Подробнее").click()
    assert "tensor.ru/about" in driver.current_url

    # Открытие блока "Работаем"
    working_block = driver.find_element(
        By.CSS_SELECTOR, ".tensor_ru-container.tensor_ru-section.tensor_ru-About__block3"
    )
    driver.execute_script("arguments[0].scrollIntoView();", working_block) # скролим до нужного блока

    images_div = working_block.find_elements(By.CSS_SELECTOR, '.tensor_ru-About__block3-image.new_lazy')
    tmp_images = images_div[0]  # сравним все размеры изображений с первой картинкой
    for image in images_div[1:]:
        assert image.size['height'] == tmp_images.size['height']
        assert image.size['width'] == tmp_images.size['width']


# def test_check_sila_v_lyudyah_block_and_open_details(driver):
#     driver.get("https://tensor.ru/")
#
#     # Проверка наличия блока "Сила в людях"
#     sila_v_lyudyah_block = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Сила в людях')]"))
#     )
#     assert sila_v_lyudyah_block.is_displayed()
#
#     # Переход по ссылке "Подробнее"
#     more_details_link = sila_v_lyudyah_block.find_element(By.LINK_TEXT, "Подробнее")
#     more_details_link.click()
#
#     # Проверка, что открывается страница https://tensor.ru/about
#     assert "tensor.ru/about" in driver.current_url
#
#
# def test_check_images_dimensions_in_rabotaem_section(driver):
#     driver.get("https://tensor.ru/about")
#
#     # Поиск раздела "Работаем"
#     rabotaem_section = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//section[@id='rabotaem']"))
#     )
#
#     # Проверка, что у всех фотографий хронологии одинаковые height и width
#     images = rabotaem_section.find_elements(By.TAG_NAME, "img")
#     dimensions = [(img.size['height'], img.size['width']) for img in images]
#
#     # Убедимся, что все размеры одинаковые
#     first_dimension = dimensions[0]
#     assert all(dim == first_dimension for dim in dimensions)


if __name__ == "__main__":
    pytest.main()

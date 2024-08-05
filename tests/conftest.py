import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

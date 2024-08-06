import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from settings import BASE_DIR

chrome_options = Options()
download_dir = os.path.join(BASE_DIR, 'tests')
chrome_options.add_experimental_option('prefs', {
    'download.default_directory': download_dir,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
    file_path = os.path.join(BASE_DIR, 'tests/sbisplugin-setup-web.exe')
    if os.path.exists(file_path):
        os.remove(file_path)

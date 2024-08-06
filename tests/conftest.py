from settings import PROJECT_PATH
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



download_dir = os.getcwd()
chrome_options = Options()
download_dir = os.path.join(PROJECT_PATH, 'tests')
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

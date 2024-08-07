from pages.base_page import BasePage
from pages.download_page import DownloadPage


def test_downloading_complete(browser):
    """
    Проверка загрузки СБИС плагина.
    """
    main_page = BasePage(browser)
    main_page.open_home_page()
    main_page_footer = DownloadPage(main_page.browser)
    main_page_footer.click_footer_download_link()
    download_page = DownloadPage(browser)
    download_page.click_download_link()
    assert download_page.check_downloading() == True


def test_size_downloaded_file(browser):
    """
    Проверка размера файла скачанного и указанного на сайте.
    """
    download_page = DownloadPage(browser)
    real_file_size = str(download_page.check_size())
    assert real_file_size == download_page.get_expires_size_file_from_link()

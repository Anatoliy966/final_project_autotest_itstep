import pytest
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
from ..settings import sets
# Две точки означают абсолютный путь. Без них в виндовс будет ошибка. В линукс - скорее всего их надо будет убрать
# ..settings надо поставить и в base_page.py

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        pass

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_main_page_header(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_login()
        page.is_button_feedback()
        page.is_button_delivery()
        page.is_button_warranty()
        page.is_number_telephon()
        page.is_button_currency()
        page.is_button_uah()
        page.is_button_eur()
        page.is_button_usd()

    # def test_login_logout(self, browser):
    #     link_to_site = browser.current_url

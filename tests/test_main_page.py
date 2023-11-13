import pytest
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
import random
from ..settings import sets
# Две точки означают абсолютный путь. Без них в виндовс будет ошибка. В линукс - скорее всего их надо будет убрать
# ..settings надо поставить и в base_page.py


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        hash_name = "%032x" % random.getrandbits(128)
        self.email_for_subscribe = f"{hash_name}@mail.com"

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
        page.is_element_logo()
        page.is_search_input_field()
        page.is_search_button()
        page.is_wish_button()
        page.is_cart_button()
        page.is_hity_button()
        page.is_skidki_button()
        page.is_novinki_button()
        page.is_samsung_category()
        page.is_samsung_j701()

    def test_main_page_content(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_my_slider()
        page.is_cat_zaryadki()
        page.is_sub_cat_power_bank()
        page.is_info_block_vozvrat_sredstv()
        page.is_info_block_dostavka()
        page.is_info_block_otsrochka()
        page.is_info_block_support()
        page.is_button_show_new_product()
        page.is_button_prev_new_product()
        page.is_button_next_new_product()
        page.is_selection_new_products()
        page.is_new_products_8()
        page.is_button_show_hits()
        page.is_button_prev_hits()
        page.is_button_next_hits()
        page.is_section_hits()
        page.is_button_prev_trend()
        page.is_button_next_trend()

    def test_main_page_footer(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_subscribe()
        page.is_logo_footer()

    def test_main_page_subscribe_action(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.subscribe_action(self.email_for_subscribe)
        page.is_allert_succers_after_sbscr()







    # def test_main_page_subscribe_action(self, browser):
    #     self.link_to_cabinet = browser.current_url
    #     page = MainPage(browser, self.link_to_cabinet)
    #     page.subscribe_action(self.email_for_subscribe)
    #     page.is_allert_succers_after_sbscr()



        # page.is_elem_newsletter_input()
        # page.is_elem_footer_logo()




    # def test_login_logout(self, browser):
    #     link_to_site = browser.current_url

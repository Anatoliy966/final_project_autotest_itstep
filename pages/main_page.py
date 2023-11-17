from ..pages import base_page, locators
import inspect


class MainPage(base_page.BasePage):
    def is_button_login(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGIN_SIGNUP), \
            "Button login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_feedback(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.FEEDBACK), \
            "Button feedback is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_delivery(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Доставка' is not present"
        assert self.is_element_present(*locators.BasePageLocators.DELIVERY), \
                "Button DELIVERY is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_warranty(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
                "Element 'Гарантия' is not present"
        assert self.is_element_present (*locators.BasePageLocators.WARRANTY), \
                "Button WARRANTY is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_number_telephon(self):
        assert self.is_element_present (*locators.BasePageLocators.PHONE), \
                    "Element 'PHONE' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_currency(self):
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY), \
            "Element 'CURRENCY' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_uah(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_eur(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_usd(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_element_logo(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO), \
            "The element logo is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_input_field(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_INPUT), \
            "The search input field is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_button(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_BUTTON), \
            "The search button is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_wish_button(self):
        assert self.is_element_present(*locators.BasePageLocators.WISH_BUTTON), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_cart_button(self):
        assert self.is_element_present(*locators.BasePageLocators.CART_BUTTON), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_hity_button(self):
        assert self.is_element_present(*locators.BasePageLocators.HITY), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_skidki_button(self):
        assert self.is_element_present(*locators.BasePageLocators.SKIDKI), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_novinki_button(self):
        assert self.is_element_present(*locators.BasePageLocators.NOVINKI), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_samsung_category(self):
        assert self.is_element_present(*locators.BasePageLocators.HEAD_CAT_SAMSUNG), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_samsung_j701(self):
        assert self.hover_action(*locators.BasePageLocators.HEAD_CAT_SAMSUNG), \
            "The element is not present"
        assert self.is_element_present(*locators.BasePageLocators.SAMSUNG_J701), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_my_slider(self):
        assert self.is_element_present(*locators.MainPageLocators.SCREEN_SLIDER), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_cat_zaryadki(self):
        assert self.is_element_present(*locators.MainPageLocators.CAT_ZARYADKI), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_sub_cat_power_bank(self):
        assert self.hover_action(*locators.MainPageLocators.CAT_ZARYADKI), \
            "Element 'Зарядки' is not present"
        assert self.is_element_present(*locators.MainPageLocators.SUB_CAT_POWER_BANK), \
            "Button POWER_BANK is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_vozvrat_sredstv(self):
        assert self.is_element_present(*locators.MainPageLocators.INFO_BLOCK_VOZVRAT_SREDSTV), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_dostavka(self):
        assert self.is_element_present(*locators.MainPageLocators.INFO_BLOCK_DOSTAVKA), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_otsrochka(self):
        assert self.is_element_present(*locators.MainPageLocators.INFO_BLOCK_OTSROCHKA), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_support(self):
        assert self.is_element_present(*locators.MainPageLocators.INFO_BLOCK_SUPPORT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_show_new_product(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_SHOW_NEW_PRODUCTS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_prev_new_product(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_PREV_NEW_PRODUCTS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_next_new_product(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_NEXT_NEW_PRODUCTS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_selection_new_products(self):
        assert self.is_element_present(*locators.MainPageLocators.SELECTION_NEW_PRODUCTS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_new_products_8(self):
        assert self.is_element_present(*locators.MainPageLocators.NEW_PRODUCT_8), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_show_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_SHOW_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_prev_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_PREV_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_next_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_NEXT_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_section_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.SECTION_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_prev_trend(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_PREV_TREND), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_next_trend(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_NEXT_TREND), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")




    def is_button_subscribe(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBE), \
            "The element subscribe is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_input_subscribe(self):
        assert self.is_element_present(*locators.BasePageLocators.INPUT_SUBSCRIBE), \
            "The element subscribe is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_logo_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_FOOTER), \
            "The element footer logo is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def subscribe_action(self, email):
        assert self.input_data(*locators.BasePageLocators.INPUT_SUBSCRIBE, email), \
            "The element is not present"
        self.explicit_wait(5) # добавили ожидание 5 секунд
        assert self.click_element(*locators.BasePageLocators.SUBSCRIBE), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_allert_succers_after_sbscr(self):
        assert self.is_element_appears_after_while(*locators.BasePageLocators.ALERT_SUCCESS, timeout=5), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")











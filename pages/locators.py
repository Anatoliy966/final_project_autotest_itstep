from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_SIGNUP = (By.XPATH, "//div[@class='top_bar_user']/a[@href='user/login']")
    DETAILS = (By.XPATH, "//a[text()='Детали сотрудничества']")
    FEEDBACK = (By.XPATH, "//a[text()='Обратная связь']")
    DELIVERY = (By.XPATH, "//a[text()='Доставка']")
    WARRANTY = (By.XPATH, "//a[text()='Гарантия']")
    PHONE = (By.XPATH, "//*[text()='+38 098 911 95 22']")
    CURRENCY = (By.XPATH, "//select[@id='currency']")

    UAH = (By.XPATH, "//option[text()='UAH']")
    USD = (By.XPATH, "//option[text()='USD']")
    EUR = (By.XPATH, "//option[text()='EUR']")
    LOGO = (By.XPATH, "//img[@src='images/logo.png']")
    SEARCH_INPUT = (By.XPATH, "//input[@id='typeahead']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    WISH_BUTTON = (By.XPATH, "//a[@href='wish/show']")
    CART_BUTTON = (By.XPATH, "//a[@href='cart/show']")

    HITY = (By.XPATH, "//span[text()='Хиты']")
    SKIDKI = (By.XPATH, "//span[text()='Скидки']")
    NOVINKI = (By.XPATH, "//span[text()='Новинки']")

    HEAD_CAT_SAMSUNG = (By.XPATH, "//div[@class='search-by-level-1' and text()='Samsung']")
    SAMSUNG_J701 = (By.XPATH, "//a[text()='Samsung J701']")

    SUBSCRIBE = (By.XPATH, "//button[text()='Подписаться!']")
    INPUT_SUBSCRIBE = (By.XPATH, "//input[@name='submail']")
    LOGO_FOOTER = (By.XPATH, "//img[@src='images/logo-footer.png']")

    ALERT_SUCCESS = (By.XPATH, "//div[@id='alert-success']")
    ALERT_ERROR = (By.XPATH, "//div[@id='alert-error']")


class MainPageLocators:
    SCREEN_SLIDER = (By.XPATH, "//div[@class='screen_slider']")
    CAT_ZARYADKI = (By.XPATH, "//a[@href='category/zaryadki']")
    SUB_CAT_POWER_BANK = (By.XPATH, "//ul[@class='cat_menu']/li[5]/ul/li[6]")
    INFO_BLOCK_VOZVRAT_SREDSTV = (By.XPATH, "//div[@class='characteristics']//div[@class='row']/div[1]/div")
    INFO_BLOCK_DOSTAVKA = (By.XPATH, "//div[@class='characteristics']//div[@class='row']/div[2]/div")
    INFO_BLOCK_OTSROCHKA = (By.XPATH, "//div[@class='characteristics']//div[@class='row']/div[3]/div")
    INFO_BLOCK_SUPPORT = (By.XPATH, "//div[@class='characteristics']//div[@class='row']/div[4]/div")
    BUTTON_SHOW_NEW_PRODUCTS = (By.XPATH, "//div[@class='new_arrivals_title clearfix']//a[@href='main/showNew']")
    BUTTON_PREV_NEW_PRODUCTS = (By.XPATH, "//div[@class='new_arrivals']//div[@class='arrivals_nav arrivals_prev']")
    BUTTON_NEXT_NEW_PRODUCTS = (By.XPATH, "//div[@class='new_arrivals']//div[@class='arrivals_nav arrivals_next']")
    SELECTION_NEW_PRODUCTS = (By.XPATH, "//div[@class='new_arrivals']//div[@class='slick-list draggable']")
    NEW_PRODUCT_8 = (By.XPATH, "//div[@class='new_arrivals']//div[@class='slick-list draggable']/div/div[3]/div[2]")
    BUTTON_SHOW_HITS = (By.XPATH, "//div[@class='best_sellers']//a[@href='main/showHit']")

    BUTTON_PREV_HITS = (By.XPATH, "//div[@class='best_sellers']//div[@class='best_prev best_nav']/i")
    BUTTON_NEXT_HITS = (By.XPATH, "//div[@class='best_sellers']//div[@class='best_next best_nav']/i")
    SECTION_HITS = (By.XPATH, "//div[@class='best_sellers']//div[@class='bestsellers_panel panel active']")
    BUTTON_PREV_TREND = (By.XPATH, "//div[@class='trends']//div[@class='trends_prev trends_nav slick-arrow']/i")
    BUTTON_NEXT_TREND = (By.XPATH, "//div[@class='trends']//div[@class='trends_next trends_nav slick-arrow']/i")






class SignupLoginPageLocators:
    pass


class OrderPageLocators:
    pass


class CabinetPageLocators:
    pass


class CategoryPageLocators:
    pass


class SearchPageLocators:
    pass




from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_SIGNUP = (By.XPATH, "//div[@class='top_bar_user']/a[@href='user/login']")
    FEEDBACK = (By.XPATH, "//a[text()='Обратная связь']")
    DELIVERY = (By.XPATH, "//a[text()='Доставка']")
    WARRANTY = (By.XPATH, "//a[text()='Гарантия']")
    PHONE = (By.XPATH, "//*[text()='+38 098 911 95 22']")
    CURRENCY = (By.XPATH, "//select[@id='currency']")
    CURRENCY_USD = (By.XPATH, "//option[text()='USD']")
    CURRENCY_EUR = (By.XPATH, "//option[text()='EUR']")
    CURRENCY_UAH = (By.XPATH, "//option[text()='UAH']")
    LOGO = (By.XPATH, "//img[@src='images/logo.png']")
    SEARCH_FIELD = (By.XPATH, "//input[@id='typeahead']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    WISH_SHOW = (By.XPATH, "//a[@href='wish/show']")
    CART_SHOW = (By.XPATH, "//a[@href='cart/show']")


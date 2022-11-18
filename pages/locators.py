from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators:
    BASKET_BUTTON = (By.XPATH, "//form[@id='add_to_basket_form']/button")
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    NAME_IN_ALERT = (By.XPATH, "(//div[@id='messages']//strong) [1]")
    PRICE_IN_ALERT = (By.XPATH, "(//div[@id='messages']//strong) [3]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div [1]") 

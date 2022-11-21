from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a.btn")
    USER_ICON = (By.CLASS_NAME, "icon-user")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_EMAIL_INPUT = (By.ID, "id_login-username")
    LOGIN_PASSWORD_INPUT = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form .btn")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_INPUT_1 = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_INPUT_2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form .btn")

class ProductPageLocators:
    BASKET_BUTTON = (By.XPATH, "//form[@id='add_to_basket_form']/button")
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    NAME_IN_ALERT = (By.XPATH, "(//div[@id='messages']//strong) [1]")
    PRICE_IN_ALERT = (By.XPATH, "(//div[@id='messages']//strong) [3]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div [1]") 

class BasketPageLocators:
    EMPTY_BASKET_TITLE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
import math

class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def should_be_product_in_basket(self):
        self.should_be_same_name()
        self.should_be_same_price()

    def should_be_same_name(self):
        self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not on the page"
        self.is_element_present(*ProductPageLocators.NAME_IN_ALERT), "Product name is not in the alert after adding to basket"
        name_in_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_in_alert = self.browser.find_element(*ProductPageLocators.NAME_IN_ALERT).text
        assert name_in_product == name_in_alert, "Product name and name in alert do not match"

    def should_be_same_price(self):
        self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not on the page"
        self.is_element_present(*ProductPageLocators.PRICE_IN_ALERT), "Product price is not in the alert after adding to basket"
        price_in_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_alert = self.browser.find_element(*ProductPageLocators.PRICE_IN_ALERT).text
        assert price_in_product == price_in_alert, "Product name and name in alert do not match"

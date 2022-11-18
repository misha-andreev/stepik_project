from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
	def should_not_be_products_in_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
			"Items are in basket but they should not be"

	def should_be_empty_basket_title(self):
		assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TITLE), \
			"There is no empty basket title but it should not be"
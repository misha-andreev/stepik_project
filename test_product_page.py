from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)  
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.parametrize('code', [*range(1,7), pytest.param(7, 
    marks=pytest.mark.xfail(reason="some bug")), *range(8,10)])
@pytest.mark.skip(reason="Not neccesary")
def test_guest_can_add_product_to_basket(browser, code):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{code}"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_product_in_basket()

@pytest.mark.xfail(reason="Guest have to see success message")
@pytest.mark.skip(reason="Not neccesary")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.should_not_be_success_message()

@pytest.mark.skip(reason="Not neccesary")
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Message doesn't dissappear")
@pytest.mark.skip(reason="Not neccesary")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.message_is_dissappeared()   

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()   

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_not_be_products_in_basket()
    page.should_be_empty_basket_title()

# python3 pytest -v -rx --tb=line /Users/mac/stepik_project/test_product_page.py
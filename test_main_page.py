from .base_page import BasePage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, link)  
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)  
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
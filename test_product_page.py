from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By
import  pytest

@pytest.mark.parametrize('code', [*range(1,7), pytest.param(7, marks=pytest.mark.xfail), *range(8,10)])
def test_guest_can_add_product_to_basket(browser, code):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{code}"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_product_in_basket()

# python3 pytest -v -s --tb=line /Users/mac/stepik_project/test_product_page.py
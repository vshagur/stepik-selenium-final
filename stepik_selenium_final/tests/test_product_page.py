import sys

import pytest

from stepik_selenium_final.common import User
from stepik_selenium_final.pages import ProductPage, MainPage

PROMO_ENDPOINTS = [
    pytest.param(
        f'catalogue/coders-at-work_207/?promo=offer{num}',
        marks=pytest.mark.xfail(num == 7, reason='')) for num in range(10)
]


@pytest.mark.skipif('--browser_name=firefox' in sys.argv, reason='before fix bug')
@pytest.mark.need_review
@pytest.mark.parametrize('endpoint', PROMO_ENDPOINTS)
def test_guest_can_add_product_to_basket(browser, url, endpoint):
    page = ProductPage(browser, url + endpoint)
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.check_message_product_added_to_cart()
    page.check_message_cart_total()


@pytest.mark.xfail()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, url):
    endpoint = 'catalogue/coders-at-work_207/'
    page = ProductPage(browser, url + endpoint)
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.check_not_message_product_added_to_cart()


def test_guest_cant_see_success_message(browser, url):
    endpoint = 'catalogue/coders-at-work_207/'
    page = ProductPage(browser, url + endpoint)
    page.check_not_message_product_added_to_cart()


@pytest.mark.xfail()
def test_message_disappeared_after_adding_product_to_basket(browser, url):
    endpoint = 'catalogue/coders-at-work_207/'
    page = ProductPage(browser, url + endpoint)
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.check_message_product_added_to_cart_is_disappearing()


def test_guest_should_see_login_link_on_product_page(browser, url):
    endpoint = 'en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, url + endpoint)
    page.check_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser, url):
    endpoint = 'en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, url + endpoint)
    login_page = page.go_to_login_page()
    login_page.check_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, url):
    page = ProductPage(browser, url)
    cart_page = page.go_to_cart_page()
    cart_page.check_cart_is_empty()
    cart_page.check_message_cart_is_empty()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='class', autouse=True)
    def setup(self, browser, url):
        user = User()
        page = MainPage(browser, url)
        login_page = page.go_to_login_page()
        login_page.register_new_user(user.email, user.password)
        login_page.check_authorized_user()

    def test_user_cant_see_success_message(self, browser, url):
        endpoint = 'catalogue/coders-at-work_207/'
        page = ProductPage(browser, url + endpoint)
        page.check_not_message_product_added_to_cart()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, url):
        endpoint = "catalogue/coders-at-work_207/"
        page = ProductPage(browser, url + endpoint)
        page.add_product_to_cart()
        page.check_message_product_added_to_cart()
        page.check_message_cart_total()

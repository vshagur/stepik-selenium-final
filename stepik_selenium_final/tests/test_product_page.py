import pytest

from stepik_selenium_final.pages import ProductPage

ENDPOINTS = [
    "catalogue/coders-at-work_207/?promo=offer0",
    "catalogue/coders-at-work_207/?promo=offer1",
    "catalogue/coders-at-work_207/?promo=offer2",
    "catalogue/coders-at-work_207/?promo=offer3",
    "catalogue/coders-at-work_207/?promo=offer4",
    "catalogue/coders-at-work_207/?promo=offer5",
    "catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    "catalogue/coders-at-work_207/?promo=offer8",
    "catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_guest_can_add_product_to_basket(browser, url, endpoint):
    page = ProductPage(browser, url + endpoint)
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.check_message_product_added_to_cart()
    page.check_message_cart_total()


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


def test_guest_can_go_to_login_page_from_product_page(browser, url):
    endpoint = 'en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, url + endpoint)
    login_page = page.go_to_login_page()
    login_page.check_login_page()

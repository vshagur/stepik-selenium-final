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
    "catalogue/coders-at-work_207/?promo=offer7",
    "catalogue/coders-at-work_207/?promo=offer8",
    "catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_guest_can_add_product_to_basket(browser, url, endpoint):
    page = ProductPage(browser, url + endpoint)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.check_message_product_added_to_cart()
    page.check_message_cart_total()

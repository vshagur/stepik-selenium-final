from stepik_selenium_final.pages import MainPage


def test_guest_can_go_to_login_page(browser, url):
    page = MainPage(browser, url)
    login_page = page.go_to_login_page()
    login_page.check_login_page()


def test_guest_should_see_login_link(browser, url):
    page = MainPage(browser, url)
    page.check_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, url):
    page = MainPage(browser, url)
    cart_page = page.go_to_cart_page()
    cart_page.check_cart_is_empty()
    cart_page.check_message_cart_is_empty()

from stepik_selenium_final.pages import ProductPage


def test_guest_can_add_product_to_basket(browser, url):
    endpoint = 'catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, url + endpoint)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()

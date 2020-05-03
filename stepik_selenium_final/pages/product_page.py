from stepik_selenium_final.locators import ProductPageLocators
from stepik_selenium_final.pages import BasePage


class ProductPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.title = None
        self.price = None

    def add_product_to_cart(self):
        self.title = self.get_element(*ProductPageLocators.PRODUCT_TITLE).text
        self.price = self.get_element(*ProductPageLocators.PRODUCT_PRICE).text
        self.get_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def check_message_product_added_to_cart(self):
        text = self.get_element(*ProductPageLocators.MESSAGE_PRODUCT_ADDED).text
        assert self.title == text

    def check_message_cart_total(self):
        text = self.get_element(*ProductPageLocators.MESSAGE_CART_TOTAL).text
        assert self.price == text

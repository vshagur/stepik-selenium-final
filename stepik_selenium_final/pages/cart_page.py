from stepik_selenium_final.locators import CardPageLocators
from stepik_selenium_final.pages import BasePage


class CartPage(BasePage):
    def check_cart_is_empty(self):
        self.is_not_element_present(*CardPageLocators.PRODUCTS_IN_CART_BLOCK)
        self.is_disappearing_element(*CardPageLocators.PRODUCTS_IN_CART_BLOCK)

    def check_message_cart_is_empty(self):
        text = self.get_element(*CardPageLocators.MESSAGE_ABOUT_PRODUCTS_IN_CART).text
        assert text


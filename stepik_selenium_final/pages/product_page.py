from stepik_selenium_final.locators import ProductPageLocators
from stepik_selenium_final.pages import BasePage


class ProductPage(BasePage):
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

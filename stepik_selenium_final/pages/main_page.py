from stepik_selenium_final.locators import MainPageLocators
from stepik_selenium_final.pages import BasePage


class MainPage(BasePage):
    def go_to_cart_page(self):
        self.browser.find_element(*MainPageLocators.GO_TO_CART_BUTTON).click()
        from stepik_selenium_final.pages import CartPage
        return CartPage(browser=self.browser, url=self.browser.current_url)

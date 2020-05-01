from stepik_selenium_final.locators import MainPageLocators

from stepik_selenium_final.pages import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), \
            "Login link is not presented"

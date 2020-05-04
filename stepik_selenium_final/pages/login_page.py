from stepik_selenium_final.locators import LoginPageLocators
from stepik_selenium_final.pages import BasePage


class LoginPage(BasePage):
    def check_login_page(self):
        self.check_login_url()
        self.check_login_form()
        self.check_register_form()

    def check_login_url(self):
        assert 'login' in self.browser.current_url, \
            'The url of the login page does not match'

    def check_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'Login form is not presented'

    def check_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'Register form is not presented'

    def register_new_user(self, email, password):
        self.get_element(*LoginPageLocators.REGISTER_EMAIL_FIELD).send_keys(email)
        self.get_element(*LoginPageLocators.REGISTER_PASSWORD1_FIELD).send_keys(password)
        self.get_element(*LoginPageLocators.REGISTER_PASSWORD2_FIELD).send_keys(password)
        self.get_element(*LoginPageLocators.REGISTER_FORM_BUTTON).click()

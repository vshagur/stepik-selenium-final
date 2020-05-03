from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from stepik_selenium_final.handlers import calc
from stepik_selenium_final.locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, opened=True):
        self.browser = browser
        self.url = url
        if opened:
            self.open()

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by, locator):
        try:
            self.browser.find_element(by, locator)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, by, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            return True

        return False

    def is_disappearing_element(self, by, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            return False

        return True

    def get_element(self, by, locator):
        assert self.browser.find_element(by, locator)
        return self.browser.find_element(by, locator)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        _, _, num, _ = alert.text.split(' ', 3)
        answer = calc(num)
        alert.send_keys(answer)
        alert.accept()
        try:
            alert_text = self.browser.switch_to.alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        from stepik_selenium_final.pages import LoginPage
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def check_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not presented"

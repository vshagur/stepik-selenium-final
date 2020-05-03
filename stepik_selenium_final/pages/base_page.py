from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

from stepik_selenium_final.handlers import calc


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by, locator):
        try:
            self.browser.find_element(by, locator)
        except NoSuchElementException:
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

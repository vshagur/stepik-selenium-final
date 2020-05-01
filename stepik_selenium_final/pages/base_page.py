from selenium.common.exceptions import NoSuchElementException


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

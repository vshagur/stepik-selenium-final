from stepik_selenium_final.pages import MainPage


def test_guest_can_go_to_login_page(browser, url):
    page = MainPage(browser, url)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser, url):
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_link()


from stepik_selenium_final.pages import MainPage


def test_guest_can_go_to_login_page(browser, url):
    page = MainPage(browser, url)
    page.open()
    page.go_to_login_page()

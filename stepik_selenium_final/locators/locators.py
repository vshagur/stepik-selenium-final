from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    GO_TO_CART_BUTTON = (By.CSS_SELECTOR, 'span.btn-group > a.btn.btn-default')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main > p.price_color')
    MESSAGE_PRODUCT_ADDED = (
        By.CSS_SELECTOR,
        '#messages > div.alert:nth-child(1) > div.alertinner > strong'
    )
    MESSAGE_CART_TOTAL = (
        By.CSS_SELECTOR,
        '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > '
        'p:nth-child(1) > strong'
    )


class CardPageLocators:
    MESSAGE_ABOUT_PRODUCTS_IN_CART = (By.CSS_SELECTOR, '#content_inner > p')
    PRODUCTS_IN_CART_BLOCK = (By.CSS_SELECTOR, '#basket_formset > div.basket-items')

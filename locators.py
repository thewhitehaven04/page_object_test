from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span>a.btn-default")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items>div")
    BASKET_EMPTINESS = (By.CSS_SELECTOR, "#content_inner>p")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ItemPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, 'form>button.btn-add-to-basket')
    PRODUCT_NAME_POP_UP = (By.CSS_SELECTOR, 'div>div>div.alertinner>strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div>div>h1')


class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages>div.alert-success')

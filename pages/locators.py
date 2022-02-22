from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_lonk_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini span a.btn')


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, '.content .basket-items')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '.page_inner .content #content_inner p')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    login_url = (By.CSS_SELECTOR, '.page_inner .active')
    login_form = (By.CSS_SELECTOR, '#login_form')
    register_form = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert')
    add_to_basket_button = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    added_product_name = (By.CSS_SELECTOR, '.breadcrumb .active')
    product_name_in_basket = (By.CSS_SELECTOR, '#messages .alert-success .alertinner strong')
    added_product_price = (By.CSS_SELECTOR, '.product_main .price_color')
    product_price_in_basket = (By.CSS_SELECTOR, '#messages .alert-info .alertinner p strong')

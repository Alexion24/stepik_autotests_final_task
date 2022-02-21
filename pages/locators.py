from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    login_url = (By.CSS_SELECTOR, '.page_inner .active')
    login_form = (By.CSS_SELECTOR, '#login_form')
    register_form = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    add_to_basket_button = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    added_product_name = (By.CSS_SELECTOR, '.breadcrumb .active')
    product_name_in_basket = (By.CSS_SELECTOR, '#messages strong')
    added_product_price = (By.CSS_SELECTOR, '.product_main .price_color')
    product_price_in_basket = (By.CSS_SELECTOR, '#messages p strong')

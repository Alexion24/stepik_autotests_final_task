from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.add_to_basket_button)
        add_to_basket.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.add_to_basket_button), 'Add to basket button is not presented'

    def should_be_equal_names(self):
        added_product_name = self.browser.find_element(*ProductPageLocators.added_product_name).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.product_name_in_basket).text
        assert added_product_name in product_name_in_basket, 'Products not equal'

    def should_be_equal_prices(self):
        added_product_price = self.browser.find_element(*ProductPageLocators.added_product_price).text
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.product_price_in_basket).text
        assert added_product_price in product_price_in_basket, 'Products prices not equal'
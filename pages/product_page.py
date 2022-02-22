from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.add_to_basket_button), \
            'Add to basket button is not presented'

    def should_be_equal_names(self):
        added_product_name = self.browser.find_element(*ProductPageLocators.added_product_name).text
        product_name_in_basket = self.browser.find_elements(*ProductPageLocators.product_name_in_basket)[0].text
        assert added_product_name == product_name_in_basket, 'Products not equal'

    def should_be_equal_prices(self):
        added_product_price = self.browser.find_element(*ProductPageLocators.added_product_price).text
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.product_price_in_basket).text
        assert added_product_price == product_price_in_basket, 'Products prices not equal'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

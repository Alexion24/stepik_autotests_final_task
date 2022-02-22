from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        register_user = self.browser.find_element(By.NAME, 'registration-email')
        register_user.send_keys(email)

        user_password = self.browser.find_element(By.NAME, 'registration-password1')
        user_password.send_keys(password)

        confirm_password = self.browser.find_element(By.NAME, 'registration-password2')
        confirm_password.send_keys(password)
        register_button = self.browser.find_element(By.NAME, 'registration_submit')
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Login url is not presented"
        assert self.is_element_present(*LoginPageLocators.login_url), "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), "Register form is not presented"
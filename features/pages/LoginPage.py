from selenium.webdriver.common.by import By

from features.pages.AccountPage import AccountPage
from features.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    email_address_field_xpath="//input[@id='input-email']"
    password_field_xpath="//input[@id='input-password']"
    login_button_xpath="//input[@value='Login']"
    warning_message_xpath="//div[@class='alert alert-danger alert-dismissible']"

    def enter_email_address(self,email_text):
        self.type_into_element("email_address_field_xpath",self.email_address_field_xpath,email_text)



    def enter_password(self,password_text):
        self.type_into_element("password_field_xpath",self.password_field_xpath,password_text)



    def click_on_login_button(self):
        self.click_on_element("login_button_xpath",self.login_button_xpath)
        return AccountPage(self.driver)

    def display_status_of_warning_message(self,expected_warning_text):
        return self.retrieved_element_text_contains("warning_message_xpath",self.warning_message_xpath,expected_warning_text)



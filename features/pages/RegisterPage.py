from selenium.webdriver.common.by import By

from features.pages.AccountSuccessPage import AccountSuccessPage
from features.pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    first_name_field_xpath= "//input[@id='input-firstname']"
    last_name_field_xpath= "//input[@id='input-lastname']"
    email_field_xpath="//input[@id='input-email']"
    telephone_field_xpath="//input[@id='input-telephone']"
    password_field_xpath="//input[@id='input-password']"
    password_confirm_xpath="//input[@id='input-confirm']"
    privacy_policy_option_name_xpath="//input[@type='checkbox']"
    continue_button_xpath= "//input[@type='submit']"
    yes_radio_button_xpath="//label[@class='radio-inline'][1]/input"
    duplicate_email_warning_xpath="//div[text()='Warning: E-Mail Address is already registered!']"
    privacy_policy_warning_xpath="//div[text()='Warning: You must agree to the Privacy Policy!']"
    first_name_warning_xpath= "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_xpath="//input[@id='input-lastname']/following-sibling::div"
    email_warning_xpath="//input[@id='input-email']/following-sibling::div"
    telephone_warning_xpath="//input[@id='input-telephone']/following-sibling::div"
    password_warning_xpath="//input[@id='input-password']/following-sibling::div"

    def enter_first_name(self,first_name_text):
        self.type_into_element("first_name_field_xpath",self.first_name_field_xpath,first_name_text)

    def enter_last_name(self,last_name_text):
        self.type_into_element("last_name_field_xpath",self.last_name_field_xpath,last_name_text)


    def enter_email(self,email_text):
        self.type_into_element("email_field_xpath",self.email_field_xpath,email_text)


    def enter_telephone(self,telephone_text):
        self.driver.find_element(By.XPATH,self.telephone_field_xpath).send_keys(telephone_text)

    def enter_password(self,password_text):
        self.type_into_element("password_field_xpath",self.password_field_xpath,password_text)


    def enter_password_confirm(self,password_confirm_text):
        self.type_into_element("password_confirm_xpath",self.password_confirm_xpath,password_confirm_text)

    def select_privacy_policy(self):
        self.click_on_element("privacy_policy_option_name_xpath",self.privacy_policy_option_name_xpath)


    def click_on_continue_button(self):
        self.click_on_element("continue_button_xpath",self.continue_button_xpath)
        return AccountSuccessPage(self.driver)

    def select_yes_radio_newsletter_button(self):
        self.click_on_element("yes_radio_button_xpath",self.yes_radio_button_xpath)


    def display_status_of_duplicate_email_warning(self,expected_warning_text):
        self.retrieved_element_text_contains("duplicate_email_warning_xpath",self.duplicate_email_warning_xpath,expected_warning_text)
        return self.driver.find_element(By.XPATH,self.duplicate_email_warning_xpath).text.__contains__(expected_warning_text)

    def display_status_of_all_warning_message(self,expected_privacy_warning,expected_first_name_warning,expected_last_warning,expected_email_warning,expected_telephone_warning,expected_password_warning):
        privacy_status=self.retrieved_element_text_contains("privacy_policy_warning_xpath",self.privacy_policy_warning_xpath,expected_privacy_warning)
        first_name_status=self.retrieved_element_text_equals("first_name_warning_xpath",self.first_name_warning_xpath,expected_first_name_warning)
        last_name_status=self.retrieved_element_text_equals("last_name_warning_xpath", self.last_name_warning_xpath,expected_last_warning)
        email_status=self.retrieved_element_text_equals("email_warning_xpath", self.email_warning_xpath,expected_email_warning)
        telephone_status=self.retrieved_element_text_equals("telephone_warning_xpath", self.telephone_warning_xpath, expected_telephone_warning)
        password_status = self.retrieved_element_text_equals("password_warning_xpath", self.password_warning_xpath,expected_password_warning)
        return self.return_and_status(privacy_status,first_name_status,last_name_status,email_status,telephone_status, password_status)


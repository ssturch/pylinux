from base_app import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocator:
    LOCATOR_BUTTON = (By.CSS_SELECTOR, "button")
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PSWD_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_CONTACT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_BUTTON_CONTACT = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")


class OperationHelper(BasePage):

    def enter_login(self, text):
        login_field = self.find_element(TestSearchLocator.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(text)

    def enter_password(self, text):
        pass_field = self.find_element(TestSearchLocator.LOCATOR_PSWD_FIELD)
        pass_field.clear()
        pass_field.send_keys(text)

    def click_button(self):
        btn = self.find_element(TestSearchLocator.LOCATOR_BUTTON)
        btn.click()

    def click_contact(self):
        btn_contact = self.find_element(TestSearchLocator.LOCATOR_CONTACT)
        btn_contact.click()

    def enter_name(self, text):
        name_field = self.find_element(TestSearchLocator.LOCATOR_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(text)

    def enter_email(self, text):
        email_field = self.find_element(TestSearchLocator.LOCATOR_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(text)

    def enter_content(self, text):
        content_field = self.find_element(TestSearchLocator.LOCATOR_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(text)

    def click_button_contact(self):
        btn = self.find_element(TestSearchLocator.LOCATOR_BUTTON_CONTACT)
        btn.click()

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text
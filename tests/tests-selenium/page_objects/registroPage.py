from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.link_registration_xpath = "/html/body/div/div/div[1]/a[2]"
        self.name_input_xpath = '/html/body/div/div/div[2]/form/div[1]/input'
        self.email_input_xpath = '/html/body/div/div/div[2]/form/div[2]/input'
        self.password_input_xpath = '/html/body/div/div/div[2]/form/div[3]/input'
        self.confirm_password_input_xpath = '/html/body/div/div/div[2]/form/div[4]/input'
        self.register_button_xpath = "/html/body/div/div/div[2]/form/div[5]/button"
        self.message_text_pass='/html/body/div/div/div[2]/form/div[3]/div/p'
        self.message_text_email='/html/body/div/div/div[2]/form/div[2]/div/p'

    def navigate_to_registration(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.link_registration_xpath))
        ).click()

    def enter_name(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.name_input_xpath))
        )
        element.send_keys(name)

    def enter_email(self, email):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.email_input_xpath))
        )
        element.send_keys(email)

    def enter_password(self, password):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.password_input_xpath))
        )
        element.send_keys(password)

    def enter_confirm_password(self, confirm_password):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.confirm_password_input_xpath))
        )
        element.send_keys(confirm_password)

    def click_register(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.register_button_xpath))
        ).click()

    def message_pass(self):
        try:
            elemento = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.message_text_pass))
            )
            return elemento.text
        except TimeoutException:
            return ""
    def message_email(self):
        try:
            elemento = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.message_text_email))
            )
            return elemento.text
        except TimeoutException:
            return ""
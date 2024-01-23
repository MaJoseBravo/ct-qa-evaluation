import unittest

import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from Elements import Elements
from Errors import Errors
from User import User
from dependencias import dependency


class AllTests(unittest.TestCase):
    user = User('Veronica', 'veronica@gmail.com', '12345678')
    url = "http://localhost"

    def setUp(self):
        options = Options()
        
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = WebDriver(options=options)

    @dependency()
    def test_register_process(self):
        self.driver.get(self.url)
        self._get_element(Elements.LINK_REGISTRATION_XPATH).click()
        self._get_element(Elements.NAME_INPUT_XPATH).send_keys(self.user.name)
        self._get_element(Elements.EMAIL_INPUT_XPATH).send_keys(self.user.email)
        self._get_element(Elements.PASSWORD_INPUT_XPATH).send_keys(self.user.password)
        self._get_element(Elements.CONFIRM_PASSWORD_INPUT_XPATH).send_keys(self.user.password)
        self._get_element(Elements.REGISTER_BUTTON_XPATH).click()

        if Errors.is_error_password(self._get_message(Elements.MESSAGE_TEXT_PASS)):
            self.fail(
                "Fallo en la prueba: Se encontró el mensaje de error de credenciales, la contraseña tiene menos de 8 "
                "caracteres")

        if Errors.is_error_email(self._get_message(Elements.MESSAGE_TEXT_EMAIL)):
            self.fail("Fallo en la prueba: Se encontró el mensaje de error de credenciales, el email ya está en uso.")

    @dependency(depends=['test_register_process'], scope='class') 
    def test_login_process(self,delay_time=10):
         
        self.driver.get(self.url)
        self._get_element(Elements.LOGIN_BUTTON).click()
        self._get_element(Elements.EMAIL_FIELD_REGISTER).send_keys(self.user.email)
        self._get_element(Elements.PASSWORD_FIELD_LOGIN).send_keys(self.user.password)
        self._get_element(Elements.SAVE_LOGIN_BUTTON,delay_time).click()

    def _get_element(self, element: Elements, delay_time=10):
        return WebDriverWait(self.driver, delay_time).until(
            ec.visibility_of_element_located((By.XPATH, element.value))
        )

    def _get_message(self, element: Elements, delay_time=5):
        try:
            return self._get_element(element, delay_time).text
        except TimeoutException:
            return ""
    @dependency(depends=['test_login_process'], scope='class')
    def test_change_password(self):
        self.driver.get(self.url)
        new_password = "12345ABCD"
        self.test_login_process(100)
        self._get_element(Elements.PROFILE_DROPDOWN, delay_time=10).click()
        self._get_element(Elements.PROFILE_BUTTON).click()
        self._get_element(Elements.CURRENT_PASSWORD_INPUT).send_keys(self.user.password)
        self._get_element(Elements.NEW_PASSWORD_INPUT).send_keys(new_password)
        self._get_element(Elements.CONFIRM_NEW_PASSWORD_INPUT).send_keys(new_password)
        
        if Errors.is_error_password(self._get_message(Elements.MESSAGE_TEXT_PASS)):
            self.fail("Fallo en la prueba: Se encontró el mensaje de error de credenciales, la contraseña tiene menos de 8 "
                    "caracteres")



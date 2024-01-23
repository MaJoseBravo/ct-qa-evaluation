from Elements import Elements
from Errors import Errors
from Test import Test
from User import User


class RegisterTest(Test):
    def __init__(self):
        super().__init__()

    def execute(self, user: User):
        super().setUp()
        self._selenium.get(self._url)
        self._get_element(Elements.LINK_REGISTRATION_XPATH).click()
        self._get_element(Elements.NAME_INPUT_XPATH).send_keys(user.name)
        self._get_element(Elements.EMAIL_INPUT_XPATH).send_keys(user.email)
        self._get_element(Elements.PASSWORD_INPUT_XPATH).send_keys(user.password)
        self._get_element(Elements.CONFIRM_PASSWORD_INPUT_XPATH).send_keys(user.password)
        self._get_element(Elements.REGISTER_BUTTON_XPATH).click()

        if Errors.is_error_password(self._get_message(Elements.MESSAGE_TEXT_PASS)):
            self.fail(
                "Fallo: La contraseña tiene menos de 8 caracteres")

        if Errors.is_error_email(self._get_message(Elements.MESSAGE_TEXT_EMAIL)):
            self.fail("Fallo: El email ya está en uso.")
            
        
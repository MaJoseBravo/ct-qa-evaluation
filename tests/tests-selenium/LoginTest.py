from Elements import Elements
from Test import Test


class LoginTest(Test):
    def __init__(self):
        super().__init__()

    def execute(self, user):
        super().setUp()
        self._selenium.get(self._url)
        self._get_element(Elements.LOGIN_BUTTON).click()
        self._get_element(Elements.EMAIL_FIELD_LOGIN).send_keys(user.email)
        self._get_element(Elements.PASSWORD_INPUT_XPATH).send_keys(user.password)

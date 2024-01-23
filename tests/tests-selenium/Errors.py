from enum import Enum


class Errors(Enum):
    ERROR_PASSWORD_IN_REGISTER = "The password must be at least 8 characters."
    ERROR_EMAIL_IN_REGISTER = "The email has already been taken."
    ERROR_EMAIL_IN_LOGIN = "These credentials do not match our records."

    @staticmethod
    def is_error_password(message):
        return Errors.ERROR_PASSWORD_IN_REGISTER.value in message

    @staticmethod
    def is_error_email(message):
        return Errors.ERROR_EMAIL_IN_REGISTER.value in message

    @staticmethod
    def is_error_email_in_login(message):
        return Errors.ERROR_EMAIL_IN_LOGIN.value in message


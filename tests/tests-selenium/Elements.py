from enum import Enum


class Elements(Enum):
    EMAIL_FIELD_REGISTER = "/html/body/div/div/div[2]/form/div[1]/input"
    EMAIL_FIELD_LOGIN = "/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]"
    PASSWORD_FIELD_LOGIN = "/html/body/div/div/div[2]/form/div[2]/input"
    
    PASSWORD_FIELD_REGISTER = "/html/body/div/div/div[2]/form/div[2]/input"
    LOGIN_BUTTON = "/html[1]/body[1]/div[1]/div[1]/div[1]/a[1]"
    SAVE_LOGIN_BUTTON = "/html/body/div/div/div[2]/form/div[4]/button"
    MESSAGE_TEXT = '/html/body/div/div/div[2]/form/div[1]/div/p'
    PROFILE_DROPDOWN = "/html/body/div/div/div[2]/nav/div[1]/div/div[2]/div[2]"
    PROFILE_BUTTON = "/html/body/div/div/div[2]/nav/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/a"
    LOGOUT_BUTTON = '/html/body/div/div/div[2]/nav/div[1]/div/div[2]/div[2]/div/div[3]/div/form/div/button'
    CURRENT_PASSWORD_INPUT = ('/html/body/div[1]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/form/div['
                              '1]/div/div[1]/input')
    NEW_PASSWORD_INPUT = ('/html/body/div[1]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/form/div[1]/div/div['
                          '2]/input')
    CONFIRM_NEW_PASSWORD_INPUT = ('/html/body/div[1]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/form/div['
                                  '1]/div/div[3]/input')
    SAVE_BUTTON_XPATH = "/html/body/div[1]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/form/div[2]/button"
    NEW_NAME_INPUT_XPATH = '/html/body/div[1]/div/div[2]/main/div/div/div[1]/div[1]/div[2]/form/div[1]/div/div[1]/input'
    SAVE_PROFILE_BUTTON_XPATH = '/html/body/div[1]/div/div[2]/main/div/div/div[1]/div[1]/div[2]/form/div[2]/button'
    NAME_CHECK_XPATH = '/html/body/div[1]/div/div[2]/nav/div[1]/div/div[2]/div[2]'
    LINK_REGISTRATION_XPATH = "/html/body/div/div/div[1]/a[2]"
    NAME_INPUT_XPATH = '/html/body/div/div/div[2]/form/div[1]/input'
    EMAIL_INPUT_XPATH = '/html/body/div/div/div[2]/form/div[2]/input'
    PASSWORD_INPUT_XPATH ='/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/div[3]/input[1]'
    CONFIRM_PASSWORD_INPUT_XPATH = '/html/body/div/div/div[2]/form/div[4]/input'
    REGISTER_BUTTON_XPATH = "/html/body/div/div/div[2]/form/div[5]/button"
    MESSAGE_TEXT_PASS = '/html/body/div/div/div[2]/form/div[3]/div/p'
    MESSAGE_TEXT_EMAIL = '/html/body/div/div/div[2]/form/div[2]/div/p'
    

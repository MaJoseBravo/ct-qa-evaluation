from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = "/html/body/div/div/div[2]/form/div[1]/input"
        self.password_field = "/html/body/div/div/div[2]/form/div[2]/input"
        self.login_button = "/html/body/div/div/div[1]/a[1]"
        self.save_login_button = "/html/body/div/div/div[2]/form/div[4]/button"
        self.message_text = '/html/body/div/div/div[2]/form/div[1]/div/p'
        self.profile_dropdown_xpath = "/html/body/div/div/div[2]/nav/div[1]/div/div[2]/div[2]"
        self.profile_button_xpath = "/html/body/div/div/div[2]/nav/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/a"
        self.profile_dropdown_xpath = "/html/body/div/div/div[2]/nav/div[1]/div/div[2]/div[2]"
        self.profile_button_xpath = "/html/body/div/div/div[2]/nav/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/a"
        self.logout_button_xpath='/html/body/div/div/div[2]/nav/div[1]/div/div[2]/div[2]/div/div[3]/div/form/div/button'
        self.current_password_input_xpath = '/html/body/div[1]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/form/div[1]/div/div[1]/input'
        self.new_password_input_xpath = '/html/body/div[1]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/form/div[1]/div/div[2]/input'
        self.confirm_new_password_input_xpath = '/html/body/div[1]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/form/div[1]/div/div[3]/input'
        self.save_button_xpath = "/html/body/div[1]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/form/div[2]/button"
        self.new_name_input_xpath='/html/body/div[1]/div/div[2]/main/div/div/div[1]/div[1]/div[2]/form/div[1]/div/div[1]/input'
        self.save_profile_button_xpath='/html/body/div[1]/div/div[2]/main/div/div/div[1]/div[1]/div[2]/form/div[2]/button'
        self.name_check_xpath='/html/body/div[1]/div/div[2]/nav/div[1]/div/div[2]/div[2]'
        
    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.login_button))
        ).click()
        
    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.email_field))
        ).send_keys(email)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.password_field))
        ).send_keys(password)

    def click_save_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.save_login_button))
        ).click()
    
    def message(self):
        try:
            elemento = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.message_text))
            )
            return elemento.text
        except TimeoutException:
            return ""
    
    def navigate_to_profile(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.profile_dropdown_xpath))
        ).click()
    
    def click_profile(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.profile_button_xpath))
        ).click()
        
    def click_LogOut(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.logout_button_xpath))
        ).click()
        
    def update_password(self, current_password, new_password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.current_password_input_xpath))
        ).send_keys(current_password)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.new_password_input_xpath))
        ).send_keys(new_password)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.confirm_new_password_input_xpath))
        ).send_keys(new_password)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.save_button_xpath))
        ).click()
        
    def update_Name_Profile(self,new_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.new_name_input_xpath))
        ).send_keys(new_name)
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.save_profile_button_xpath))
        ).click()
        
    def check_name_profile(self):
        try:
            elemento = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.name_check_xpath))
            )
            return elemento.text
        except TimeoutException:
            return ""
    def delete_text_name_profile(self):
    # Esperar a que el elemento sea visible
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.new_name_input_xpath))
        )

        # Seleccionar todo el texto en el campo y borrarlo
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
            
        
        
        

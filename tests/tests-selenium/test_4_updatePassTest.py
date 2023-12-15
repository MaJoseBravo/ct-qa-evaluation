import unittest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from page_objects.loginPage import LoginPage
from user_data_utils import load_user_data,update_user_password
from password_utils import generate_random_password
from url_proyecto import url
import time


class UpdateTest(unittest.TestCase):

    def setUp(self):
        """Parametros necesarios para ejecutar el test
        """
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = WebDriver(options=options)

    def test_update_password_process(self):
        self.driver.get(url) # Navegar a la URL
        login_page = LoginPage(self.driver) # Crear una instancia de LoginPage
        login_page.click_login()
        user_data = load_user_data()
        email = user_data['email']
        password = user_data['password']
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_save_login()
        
        if "These credentials do not match our records." in login_page.message():
            self.fail("Fallo en la prueba: Se encontró el mensaje de error de credenciales")
        
        login_page.navigate_to_profile()
        
        login_page.click_profile()
        
        random_password = generate_random_password()
        
        login_page.update_password(password,random_password)
        
        update_user_password(random_password)
        
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
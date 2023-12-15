import unittest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from page_objects.loginPage import LoginPage
from user_data_utils import load_user_data, update_user
from url_proyecto import url
import time

class UpdateProfileFailTest(unittest.TestCase):

    def setUp(self):
        """Configuración inicial antes de cada prueba"""
        self.driver = self.initialize_headless_driver()

    def initialize_headless_driver(self):
        """Inicializa y devuelve un WebDriver sin interfaz gráfica"""
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        return WebDriver(options=options)

    def test_update_profile_fail_process(self):
        # Iniciar el navegador y abrir la URL del proyecto
        self.driver.get(url)

        # Crear una instancia de LoginPage e iniciar sesión
        login_page = LoginPage(self.driver)
        self.perform_login(login_page)

        # Navegar al perfil y realizar acciones en la página de perfil
        self.perform_update_profile_fail(login_page)

    def perform_login(self, login_page):
        """Realizar el proceso de inicio de sesión"""
        user_data = load_user_data()
        email, password = user_data['email'], user_data['password']
        login_page.login(email, password)

        # Manejar posibles errores de inicio de sesión
        error_message = "These credentials do not match our records."
        self.assertNotIn(error_message, login_page.message(), f"Fallo en la prueba: {error_message}")

    def perform_update_profile_fail(self, login_page):
        """Realizar el proceso de actualización de perfil fallido"""
        login_page.navigate_to_profile()
        login_page.click_profile()
        login_page.delete_text_name_profile()

        new_name = 'ExampleNewName'

        login_page.update_Name_Profile(new_name)
        time.sleep(3)

        # Verificar si el nombre de usuario no se actualizó correctamente
        if login_page.check_name_profile() == new_name:
            self.fail("Fallo en la prueba: Se encontró el nombre de usuario en Perfil")

        # Cerrar sesión
        login_page.navigate_to_profile()
        login_page.click_logout()
        time.sleep(2)

    def tearDown(self):
        """Cerrar el navegador después de cada prueba"""
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

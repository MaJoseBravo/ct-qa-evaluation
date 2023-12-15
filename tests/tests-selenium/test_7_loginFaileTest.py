import unittest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from page_objects.loginPage import LoginPage
from url_proyecto import url

class LoginFailTest(unittest.TestCase):

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

    def test_login_fail_process(self):
        # Iniciar el navegador y abrir la URL del proyecto
        self.driver.get(url)

        # Crear una instancia de LoginPage
        login_page = LoginPage(self.driver)

        # Credenciales incorrectas
        email, password = 'example_fail@example.com', 'failfail123123'

        # Realizar el proceso de inicio de sesión
        self.perform_login(login_page, email, password)

    def perform_login(self, login_page, email, password):
        """Realizar el proceso de inicio de sesión"""
        login_page.click_login()
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_save_login()

        # Verificar si se muestra el mensaje de error
        error_message = "These credentials do not match our records."
        self.assertNotIn(error_message, login_page.message(), f"Fallo en la prueba: {error_message}")

    def tearDown(self):
        """Cerrar el navegador después de cada prueba"""
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

import unittest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from page_objects.loginPage import LoginPage
from user_data_utils import load_user_data, update_user
from url_proyecto import url
import time

class UpdateProfileTest(unittest.TestCase):

    def setUp(self):
        """Configuración inicial antes de cada prueba
        """
        self.driver = self.initialize_headless_driver()

    def initialize_headless_driver(self):
        """Inicializa y devuelve un WebDriver sin interfaz gráfica
        """
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        return WebDriver(options=options)

    def test_update_profile_process(self):
        # Iniciar el navegador y abrir la URL del proyecto
        self.driver.get(url)
        
        # Iniciar sesión con credenciales
        login_page = LoginPage(self.driver)
        user_data = load_user_data()
        email, password = user_data['email'], user_data['password']
        login_page.login(email, password)

        # Manejar posibles errores de inicio de sesión
        error_message = "These credentials do not match our records."
        if error_message in login_page.message():
            self.fail(f"Fallo en la prueba: Se encontró el mensaje de error de credenciales: {error_message}")

        # Navegar al perfil y realizar acciones en la página de perfil
        login_page.navigate_to_profile()
        login_page.click_profile()
        
        # Borrar el texto del nombre de perfil
        login_page.delete_text_name_profile()
        
        # Actualizar el nombre del perfil
        new_name = 'ExampleName'
        login_page.update_name_profile(new_name)
        
        # Esperar brevemente para permitir que la página se actualice completamente (podrías reemplazar esto con WebDriverWait)
        time.sleep(5)
        
        # Verificar si el nombre del perfil se actualizó correctamente
        if login_page.check_name_profile() != new_name:
            self.fail("Fallo en la prueba: No se encontró el nombre de usuario en el perfil")
        
        # Actualizar el nombre en el sistema de usuario
        update_user(new_name)
        
        # Navegar al perfil y realizar acciones en la página de perfil
        login_page.navigate_to_profile()
        login_page.click_logout()
        
        # Esperar brevemente antes de cerrar el navegador
        time.sleep(2)

    def tearDown(self):
        """Cerrar el navegador después de cada prueba
        """
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

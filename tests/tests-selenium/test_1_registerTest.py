import unittest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from page_objects.registroPage import RegistrationPage
from user_data_utils import save_user_data
from url_proyecto import url

class RegisterTest(unittest.TestCase):

    def setUp(self):
        """Configuración inicial antes de cada prueba
        """
        options = Options()
        options.add_argument("--headless")  # Ejecución sin interfaz gráfica
        options.add_argument("--disable-gpu")  # Desactivar la aceleración de GPU
        options.add_argument("--no-sandbox")  # Desactivar características de seguridad de aislamiento
        options.add_argument("--disable-dev-shm-usage")  # Evitar uso de memoria compartida
        self.driver = WebDriver(options=options)

    def test_register_process(self):
        # Iniciar el navegador y abrir la URL del proyecto
        driver = self.driver
        driver.get(url)

        # Inicializar la página de registro
        registration_page = RegistrationPage(driver)

        # Navegar al formulario de registro
        registration_page.navigate_to_registration()

        # Rellenar el formulario de registro
        user = 'Michael2034'
        email = 'Michael2034_a@example.com'
        password = '3434565698thg'
        registration_page.enter_name(user)
        registration_page.enter_email(email)
        registration_page.enter_password(password)
        registration_page.enter_confirm_password(password)

        # Enviar el formulario
        registration_page.click_register()

        # Manejar posibles errores
        if "The password must be at least 8 characters." in registration_page.message_pass():
            self.fail("Fallo en la prueba: Se encontró el mensaje de error de credenciales, la contraseña tiene menos de 8 caracteres")

        if "The email has already been taken." in registration_page.message_email():
            self.fail("Fallo en la prueba: Se encontró el mensaje de error de credenciales, el email ya está en uso.")

        # Guardar los datos del usuario en un archivo JSON
        save_user_data(user, email, password)
        
    def tearDown(self):
        """Cerrar el navegador después de cada prueba
        """
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

import unittest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from Elements import Elements


class Test(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self._selenium = None
        self._url = "http://localhost"

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self._selenium = WebDriver(options=options)

    def tearDown(self):
        self._selenium.close()

    def _get_element(self, element: Elements, delay_time=10):
        return WebDriverWait(self._selenium, delay_time).until(
            ec.visibility_of_element_located((By.XPATH, element.value))
        )

    def _get_message(self, element: Elements, delay_time=5):
        try:
            return self._get_element(element, delay_time).text
        except TimeoutException:
            return ""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

class TestDetalleVenta:
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element(By.XPATH, "//a[text() = 'Iniciar Sesion']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@gmail.com")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("cinnamonroll")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(11)
        #Entrar a el detalle venta
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Detalle Venta')]").click()
        time.sleep(10)

    def teardown_method(self):
        self.driver.quit()
        print(" Prueba Completa")

    def test_Ver(self):
        #Ver gaaa
        self.driver.find_element(By.XPATH, "//tbody//tr//td//span[contains(text(), '390')]//parent::td//parent::tr//span[contains(text(), 'Vista previa')]").click()
        time.sleep(25)
        actual = self.driver.find_element(By.XPATH, "//tbody//tr//td//span[contains(text(), '390')]").text
        time.sleep(1)
        esperado = "390"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"

    def test_Borrar(self):
        #Borrar gaaa
        #aca para fucionar debe haber un detalle venta con:
        #  - Kate Spade NY 0SK174 - Lentes deportivos cant 1 precio 200
        self.driver.find_element(By.XPATH, "//tbody//tr//td//span[contains(text(), 'Lentes deportivos')]//parent::span//parent::td//parent::tr//span[contains(text(), 'Eliminar')]").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Eliminar')]").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//input[@type='search']").send_keys("Lentes deportivos")
        time.sleep(20)
        actual = self.driver.find_element(By.XPATH, "//td[@class='dataTables_empty']").text
        time.sleep(1)
        esperado = "No se encontraron elementos"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
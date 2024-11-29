from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

class TestRegistro:
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
        time.sleep(1)

    def teardown_method(self):
        self.driver.quit()
        print(" Prueba Completa")

    def test_Despliegue(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, "/html/body/div/aside/div/div[2]/ul/li[7]/a/span").click()
        time.sleep(1)
        actual = self.driver.find_element(By.XPATH, "/html/body/div/aside/div/div[2]/ul/li[7]/div/a[1]/span").text
        esperado = "Proveedores"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
        
    def test_entrar_boton_Proveedor(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, "/html/body/div/aside/div/div[2]/ul/li[7]/a/span").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div/aside/div/div[2]/ul/li[7]/div/a[1]/span").click()
        time.sleep(10)
        actual = self.driver.find_element(By.XPATH, "//h1[@class='text-capitalize mb-0']").text
        esperado = "Proveedores"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
    
    def test_entrar_boton_Compra(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, "/html/body/div/aside/div/div[2]/ul/li[7]/a/span").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div/aside/div/div[2]/ul/li[7]/div/a[2]/span").click()
        time.sleep(10)
        actual = self.driver.find_element(By.XPATH, "//h1[@class='text-capitalize mb-0']").text
        esperado = "Compras"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
        
    def test_entrar_boton_DetalleCompra(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, "/html/body/div/aside/div/div[2]/ul/li[7]/a/span").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div/aside/div/div[2]/ul/li[7]/div/a[3]/span").click()
        time.sleep(10)
        actual = self.driver.find_element(By.XPATH, "//h1[@class='text-capitalize mb-0']").text
        esperado = "Detalle Compras"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
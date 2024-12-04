from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

class TestSucursales:
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
        time.sleep(12)
        #Entrar a sucursales
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Sucursales')]").click()
        time.sleep(10)

    def teardown_method(self):
        self.driver.quit()
        print(" Prueba Completa")

    def test_Create(self):
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary']//child::span").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//input[@name='nombre']").send_keys("Sucursal Test")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='direccion']").send_keys("Direccion Test")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(25)
        actual = self.driver.find_element(By.XPATH, "//tbody//tr//td//span[contains(text(), 'Sucursal Test')]").text
        time.sleep(1)
        esperado = "Sucursal Test"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
    
    def test_Editar(self):
        #Editar gaaa
        self.driver.find_element(By.XPATH, "//tbody//tr//td//span[contains(text(), 'Sucursal Test')]//parent::td//parent::tr//span[contains(text(), 'Editar')]").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//input[@name='nombre']").send_keys("Editado ")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(25)
        actual = self.driver.find_element(By.XPATH, "//tbody//tr//td//span[contains(text(), 'Editado')]").text
        time.sleep(1)
        esperado = "Editado"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"

    def test_Borrar(self):
        #Borrar gaaa
        self.driver.find_element(By.XPATH, "//tbody//tr//td//span[contains(text(), 'Sucursal Test')]//parent::td//parent::tr//span[contains(text(), 'Eliminar')]").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Eliminar')]").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//input[@type='search']").send_keys("Editado Sucursal Test")
        time.sleep(20)
        actual = self.driver.find_element(By.XPATH, "//td[@class='dataTables_empty']").text
        time.sleep(1)
        esperado = "No se encontraron elementos"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
        
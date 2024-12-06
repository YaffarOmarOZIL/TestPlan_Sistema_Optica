from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

class TestProveedor:
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
        
    def test_Create(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//span[text()='Gestion de Suministros']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[text()='Proveedores']").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary']//child::span").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//input[@name='nombre']").send_keys("TestCase")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='contacto']").send_keys("TestCase Contacto")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='telefono']").send_keys("77766889")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(25)
        actual = self.driver.find_element(By.XPATH, "//tbody//tr//td//span[contains(text(), 'TestCase')]").text
        time.sleep(1)
        esperado = "TestCase"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
    
    def test_Editar(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//span[text()='Gestion de Suministros']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[text()='Proveedores']").click()
        time.sleep(10)
        #Editar gaaa
        self.driver.find_element(By.XPATH, "//tbody//tr//td//span[contains(text(), 'TestCase')]//parent::td//parent::tr//span[contains(text(), 'Editar')]").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//input[@name='nombre']").send_keys("TestCase Editado")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(25)
        actual = self.driver.find_element(By.XPATH, "//tbody//tr//td//span[contains(text(), 'TestCase Editado')]").text
        time.sleep(1)
        esperado = "TestCase Editado"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"

    def test_Borrar(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//span[text()='Gestion de Suministros']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[text()='Proveedores']").click()
        time.sleep(10)
        #Borrar gaaa
        self.driver.find_element(By.XPATH, "//tbody//tr//td//span[contains(text(), 'TestCase')]//parent::td//parent::tr//span[contains(text(), 'Eliminar')]").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Eliminar')]").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//input[@type='search']").send_keys("TestCase Editado")
        time.sleep(20)
        actual = self.driver.find_element(By.XPATH, "//td[@class='dataTables_empty']").text
        time.sleep(1)
        esperado = "No se encontraron elementos"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
        
        

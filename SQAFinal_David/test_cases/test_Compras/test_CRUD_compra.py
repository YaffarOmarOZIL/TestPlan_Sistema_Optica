from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.keys import Keys

class TestCompra:
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
        #Entrar a la compra
        self.driver.find_element(By.XPATH, "//span[text()='Gestion de Suministros']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[text()='Compras']").click()
        time.sleep(10)

    def teardown_method(self):
        self.driver.quit()
        print(" Prueba Completa")
        
    def test_Create(self):
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary']//child::span").click()
        time.sleep(10)
        #crear gaaaaa
        self.driver.find_element(By.XPATH, "//select[@class='form-control montura-select']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//select[@class='form-control montura-select']//option[@value=4]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//select[@class='form-control lente-select']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//select[@class='form-control lente-select']//option[@value=4]").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//button[@id='agregar-detalle']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[2]//div[5]//button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@id='agregar-detalle']").send_keys(Keys.TAB)
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(25)
        actual = self.driver.find_element(By.XPATH, "//tbody//tr//td//span[contains(text(), '171')]").text
        time.sleep(1)
        esperado = "171"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
    
    def test_Editar(self):
        #Editar gaaa
        self.driver.find_element(By.XPATH, "//tbody//tr//td//span[contains(text(), '171')]//parent::td//parent::tr//span[contains(text(), 'Editar')]").click()
        time.sleep(10)

        self.driver.find_element(By.XPATH, "//select[@name='proveedor_id']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//select[@name='proveedor_id']//option[@value='5']").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(25)
        actual = self.driver.find_element(By.XPATH, "//tbody//tr//td//span[contains(text(), 'Lentes & Más')]").text
        time.sleep(1)
        esperado = "Lentes & Más"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"

    def test_Borrar(self):
        #Borrar gaaa
        self.driver.find_element(By.XPATH, "//tbody//tr//td//span[contains(text(), 'Lentes & Más')]//parent::span//parent::td//parent::tr//span[contains(text(), 'Eliminar')]").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Eliminar')]").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//input[@type='search']").send_keys("Lentes & Más")
        time.sleep(20)
        actual = self.driver.find_element(By.XPATH, "//td[@class='dataTables_empty']").text
        time.sleep(1)
        esperado = "No se encontraron elementos"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
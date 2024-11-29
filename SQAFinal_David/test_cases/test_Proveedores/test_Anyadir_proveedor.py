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
        self.driver.find_element(By.XPATH, "/html/body/div/aside/div/div[2]/ul/li[7]/a/span").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div/aside/div/div[2]/ul/li[7]/div/a[1]/span").click()
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
        
        

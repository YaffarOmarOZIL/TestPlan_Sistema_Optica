# Incluir acá los test cases para el módulo específico.
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
 
class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[text() = 'App Movil']").click()
        time.sleep(2)
    
    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completa")
    
    def test_verificar_quienes_somos(self):
        actual = self.driver.find_element(By.XPATH, "//div[@class='KL4NAf']").text
        esperado = "Optica Medop.apk"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
        

    

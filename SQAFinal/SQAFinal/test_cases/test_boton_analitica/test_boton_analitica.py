# Incluir acá los test cases para el módulo específico.
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
 
class TestAnalitica:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element(By.XPATH, "//a[text() = 'Iniciar Sesion']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("cinnamonroll")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
    
    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completa")
    
    def test_verificar_graficos_analitica(self):
        self.driver.find_element(By.XPATH, "//a[text() = 'Analítica']").click()
        time.sleep(2)
        for i in range(1, 10):
            esperado = f"Gráfico {i}"
            actual = self.driver.find_element(By.XPATH, f"//img[@alt='{esperado}']").get_attribute("alt")
            assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
            


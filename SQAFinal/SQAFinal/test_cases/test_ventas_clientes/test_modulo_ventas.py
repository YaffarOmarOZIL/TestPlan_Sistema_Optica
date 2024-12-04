# Incluir acá los test cases para el módulo específico.
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

 
class TestLogin:
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
        time.sleep(5)
    
    def teardown_method(self):
        self.driver.quit()
        print(" Prueba visual completa")

    def test_vefiricar_entrar_ventas(self):
        self.driver.find_element(By.XPATH, "//*[@id='mobile-menu']/ul/li[5]/a").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/venta']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//h1[@class='text-capitalize mb-0']").text
        esperado = "Ventas"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"

    def test_vefiricar_buscador_ventas(self):
        self.driver.find_element(By.XPATH, "//*[@id='mobile-menu']/ul/li[5]/a").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/venta']").click()
        time.sleep(2)
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='form-control']")))
        self.driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("Ana")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='dtr-control']//child::span")))
        actual = self.driver.find_element(By.XPATH, "//td[@class='dtr-control']//child::span").text
        esperado = "Ana"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
    
    def test_verificar_agregar_venta(self):
        self.driver.find_element(By.XPATH, "//*[@id='mobile-menu']/ul/li[5]/a").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/venta']").click()
        time.sleep(2)
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//i[@class='la la-plus']")))
        self.driver.find_element(By.XPATH, "//i[@class='la la-plus']").click()
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//select[@name='cliente_id']")))
        self.driver.find_element(By.XPATH, "//select[@name='cliente_id']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/main/div/div/div/form/div[1]/div/div[1]/select/option[15]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//select[@name='montura_id[]']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='detalles-venta']/div/div[1]/select/option[4]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//select[@name='lente_id[]']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//select[@name='lente_id[]']//child::option[@value='1']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='cantidad[]']").send_keys("1")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='precio_unitario[]']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary mt-3']").send_keys(Keys.TAB)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary mt-3']").send_keys(Keys.TAB)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary mt-3']").send_keys(Keys.TAB)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary mt-3']").send_keys(Keys.TAB)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary mt-3']").send_keys(Keys.TAB)
        self.driver.find_element(By.XPATH, "//span[@data-value='save_and_back']").click()
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='form-control']")))
        self.driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("Valentina")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='dtr-control']//child::span")))
        actual = self.driver.find_element(By.XPATH, "//td[@class='dtr-control']//child::span").text
        esperado = "Valentina"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"

    def test_verificar_Editar_venta(self):
        self.driver.find_element(By.XPATH, "//*[@id='mobile-menu']/ul/li[5]/a").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/venta']").click()
        time.sleep(2)
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='crudTable']/tbody/tr[1]/td[4]/a[2]/span")))
        self.driver.find_element(By.XPATH, "//*[@id='crudTable']/tbody/tr[1]/td[4]/a[2]/span").click()
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//select[@name='cliente_id']")))
        self.driver.find_element(By.XPATH, "//select[@name='cliente_id']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/main/div/div/div/form/div[1]/div/div[1]/select/option[8]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='detalleventas[0][precio_unitario]']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").send_keys(Keys.TAB)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").send_keys(Keys.TAB)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").send_keys(Keys.TAB)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").send_keys(Keys.TAB)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").send_keys(Keys.TAB)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[@data-value='save_and_back']").click()
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='form-control']")))
        self.driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("Lucía")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='dtr-control']//child::span")))
        actual = self.driver.find_element(By.XPATH, "//td[@class='dtr-control']//child::span").text
        esperado = "Lucía"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"


        
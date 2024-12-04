# Incluir acá los test cases para el módulo específico.
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    def test_vefiricar_entrar_lentes(self):
        self.driver.find_element(By.XPATH, "//*[@id='mobile-menu']/ul/li[6]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/lente']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//h1[@class='text-capitalize mb-0']").text
        esperado = "Lentes"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"

    def test_vefiricar_buscador_lentes(self):
        self.driver.find_element(By.XPATH, "//*[@id='mobile-menu']/ul/li[6]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/lente']").click()
        time.sleep(2)
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='form-control']")))
        self.driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("Lentes de contacto diarios")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='dtr-control']//child::span")))
        actual = self.driver.find_element(By.XPATH, "//td[@class='dtr-control']//child::span").text
        esperado = "Lentes de contacto diarios"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
    
    def test_verificar_agregar_lentes(self):
        self.driver.find_element(By.XPATH, "//*[@id='mobile-menu']/ul/li[6]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/lente']").click()
        time.sleep(2)
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//i[@class='la la-plus']")))
        self.driver.find_element(By.XPATH, "//i[@class='la la-plus']").click()
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='tipo']")))
        self.driver.find_element(By.XPATH, "//input[@name='tipo']").send_keys("BlueBlock")
        self.driver.find_element(By.XPATH, "//input[@name='precio']").send_keys("130")
        self.driver.find_element(By.XPATH, "//input[@name='inventario']").send_keys("50")
        self.driver.find_element(By.XPATH, "//span[@data-value='save_and_back']").click()
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='form-control']")))
        self.driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("BlueBlock")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='dtr-control']//child::span")))
        actual = self.driver.find_element(By.XPATH, "//td[@class='dtr-control']//child::span").text
        esperado = "BlueBlock"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"

    def test_verificar_Editar_lentes(self):
        self.driver.find_element(By.XPATH, "//*[@id='mobile-menu']/ul/li[6]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/lente']").click()
        time.sleep(2)
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='crudTable']/tbody/tr[1]/td[4]/a[2]/span")))
        self.driver.find_element(By.XPATH, "//*[@id='crudTable']/tbody/tr[1]/td[4]/a[2]/span").click()
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='tipo']")))
        self.driver.find_element(By.XPATH, "//input[@name='tipo']").send_keys("s")
        self.driver.find_element(By.XPATH, "//span[@data-value='save_and_back']").click()
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='form-control']")))
        self.driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("sBlueBlock")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='dtr-control']//child::span")))
        actual = self.driver.find_element(By.XPATH, "//td[@class='dtr-control']//child::span").text
        esperado = "sBlueBlock"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
    
    def test_verificar_Eliminar_lentes(self):
        self.driver.find_element(By.XPATH, "//*[@id='mobile-menu']/ul/li[6]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/lente']").click()
        time.sleep(2)
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='crudTable']/tbody/tr[1]/td[4]/a[3]/span")))
        self.driver.find_element(By.XPATH, "//*[@id='crudTable']/tbody/tr[1]/td[4]/a[3]/span").click()
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='swal-button swal-button--delete bg-danger']")))
        self.driver.find_element(By.XPATH, "//button[@class='swal-button swal-button--delete bg-danger']").click()
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='form-control']")))
        self.driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("sBlueBlock")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='dataTables_empty']")))
        actual = self.driver.find_element(By.XPATH, "//td[@class='dataTables_empty']").text
        esperado = "No se encontraron elementos"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
        
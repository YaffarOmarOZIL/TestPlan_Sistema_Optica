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

    def test_vefiricar_entrar_clientes(self):
        self.driver.find_element(By.XPATH, "//*[@id='mobile-menu']/ul/li[5]/a").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/cliente']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//h1[@class='text-capitalize mb-0']").text
        esperado = "Clientes"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"

    def test_vefiricar_buscador_clientes(self):
        self.driver.find_element(By.XPATH, "//*[@id='mobile-menu']/ul/li[5]/a").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/cliente']").click()
        time.sleep(2)
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='form-control']")))
        self.driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("Elvis")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='dtr-control']//child::span")))
        actual = self.driver.find_element(By.XPATH, "//td[@class='dtr-control']//child::span").text
        esperado = "Elvis"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
    
    def test_verificar_agregar_cliente(self):
        self.driver.find_element(By.XPATH, "//*[@id='mobile-menu']/ul/li[5]/a").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/cliente']").click()
        time.sleep(2)
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//i[@class='la la-plus']")))
        self.driver.find_element(By.XPATH, "//i[@class='la la-plus']").click()
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='nombre']")))
        self.driver.find_element(By.XPATH, "//input[@name='nombre']").send_keys("Jhoel")
        self.driver.find_element(By.XPATH, "//input[@name='apellido']").send_keys("Neuenshwander")
        self.driver.find_element(By.XPATH, "//input[@name='correo']").send_keys("joelneu@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@name='telefono']").send_keys("74576543")
        self.driver.find_element(By.XPATH, "//span[@data-value='save_and_back']").click()
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='form-control']")))
        self.driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("Jhoel")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='dtr-control']//child::span")))
        actual = self.driver.find_element(By.XPATH, "//td[@class='dtr-control']//child::span").text
        esperado = "Jhoel"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"

    def test_verificar_Editar_cliente(self):
        self.driver.find_element(By.XPATH, "//*[@id='mobile-menu']/ul/li[5]/a").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/cliente']").click()
        time.sleep(2)
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='crudTable']/tbody/tr[1]/td[5]/a[2]/span")))
        self.driver.find_element(By.XPATH, "//*[@id='crudTable']/tbody/tr[1]/td[5]/a[2]/span").click()
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='nombre']")))
        self.driver.find_element(By.XPATH, "//input[@name='nombre']").send_keys("J")
        self.driver.find_element(By.XPATH, "//input[@name='apellido']").send_keys("N")
        self.driver.find_element(By.XPATH, "//input[@name='correo']").send_keys("n")
        self.driver.find_element(By.XPATH, "//span[@data-value='save_and_back']").click()
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='form-control']")))
        self.driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("JJhoel")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='dtr-control']//child::span")))
        actual = self.driver.find_element(By.XPATH, "//td[@class='dtr-control']//child::span").text
        esperado = "JJhoel"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
    
    def test_verificar_Eliminar_cliente(self):
        self.driver.find_element(By.XPATH, "//*[@id='mobile-menu']/ul/li[5]/a").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/cliente']").click()
        time.sleep(2)
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='crudTable']/tbody/tr[1]/td[5]/a[3]/span")))
        self.driver.find_element(By.XPATH, "//*[@id='crudTable']/tbody/tr[1]/td[5]/a[3]/span").click()
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='swal-button swal-button--delete bg-danger']")))
        self.driver.find_element(By.XPATH, "//button[@class='swal-button swal-button--delete bg-danger']").click()
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='form-control']")))
        self.driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("JJhoel")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='dataTables_empty']")))
        actual = self.driver.find_element(By.XPATH, "//td[@class='dataTables_empty']").text
        esperado = "No se encontraron elementos"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
        
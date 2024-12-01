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

    def test_vefiricar_entrar_usuario(self):
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/user']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//h1[@class='text-capitalize mb-0']").text
        esperado = "Usuarios"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"

    def test_vefiricar_buscador_usuario(self):
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/user']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("admin")
        time.sleep(20)
        actual = self.driver.find_element(By.XPATH, "//td[@class='dtr-control']//child::span").text
        esperado = "admin"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
    
    def test_vefiricar_agregar_usuario(self):
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/user']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//i[@class='la la-plus']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='name']").send_keys("David Carpio")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("dacar@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("DavidCarpio56")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[@data-value='save_and_back']").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("David Carpio")
        time.sleep(20)
        actual = self.driver.find_element(By.XPATH, "//td[@class='dtr-control']//child::span").text
        esperado = "David Carpio"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
        
    def test_vefiricar_Eliminar_usuario(self):
        self.driver.find_element(By.XPATH, "//a[@href ='http://127.0.0.1:8000/admin/user']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='crudTable']/tbody/tr[1]/td[3]/a[3]/span").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='swal-button swal-button--delete bg-danger']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("David Carpio")
        time.sleep(20)
        actual = self.driver.find_element(By.XPATH, "//td[@class='dataTables_empty']").text
        esperado = "No se encontraron elementos"
        assert esperado in actual, f"ERROR: Actual es: {actual} y el Esperado: {esperado}"
from selenium.webdriver.common.by import By #importaciones necesarias para ejecutar las funciones
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BugBank: #lleva a la pagina del formulario de registro
    register_button = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[3]/button[2]')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_field(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.register_button))

    def clic_register(self):
        self.driver.find_element(*self.register_button).click()


class RegisterForm: #llenar el formulario con los datos del usuario
    email_field = (By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/form/div[2]/input')
    nome_field = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[3]/input')
    sehna_field = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[4]/div/input')
    conf_senha_field = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[5]/div/input')
    cadastrar_button = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/button')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.nome_field))

    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def set_nome(self, nome):
        self.driver.find_element(*self.nome_field).send_keys(nome)

    def set_sehna(self, senha):
        self.driver.find_element(*self.sehna_field).send_keys(senha)

    def set_conf_sehna(self, conf_senha):
        self.driver.find_element(*self.conf_senha_field).send_keys(conf_senha)

    def wait_for_load_button2(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.conf_senha_field))

    def clik_cadastrar(self):
        self.driver.find_element(*self.cadastrar_button).click()


class fechar:   #confirmacion de la creacion de la cuenta
    fechar_button = (By.XPATH, '//*[@id="btnCloseModal"]')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_field(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.fechar_button))

    def clik_fechar(self):
        self.driver.find_element(*self.fechar_button).click()


class acessar: #ingreso del usuario a la cuenta
    email_field = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[1]/input')
    senha_field = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[2]/div/input')
    acessar_button = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[3]/button[1]')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_field(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.acessar_button))

    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def set_sehna(self, senha):
        self.driver.find_element(*self.senha_field).send_keys(senha)

    def clik_acessar(self):
        self.driver.find_element(*self.acessar_button).click()


class sair: #el usuario puede salir de la web
    sair_button = (By.CSS_SELECTOR, '#btnExit')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_field(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.sair_button))

    def clik_sair(self):
        self.driver.find_element(*self.sair_button).click()



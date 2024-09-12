import time  #importaciones necesarias para ejecutar las pruebas
import data
import main
from selenium import webdriver


class TestBugBank:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_bugbank(self):
        self.driver.get(data.URL_BUGBANK)
        bugbank = main.BugBank(self.driver)
        bugbank.wait_for_load_field()
        bugbank.clic_register()

        assert data.URL_BUGBANK == 'https://bugbank.netlify.app/'

    def test_register_form(self):
        self.test_bugbank()
        register_form = main.RegisterForm(self.driver)
        register_form.wait_for_load_button()
        register_form.set_email(data.EMAIL)
        register_form.set_nome(data.NOME)
        register_form.set_sehna(data.SEHNA)
        register_form.set_conf_sehna(data.CONF_SEHNA)
        register_form.wait_for_load_button2()
        register_form.clik_cadastrar()
        time.sleep(2)

        assert data.URL_BUGBANK == 'https://bugbank.netlify.app/'

    def test_fechar(self):
        self.test_register_form()
        fechar = main.fechar(self.driver)
        fechar.wait_for_load_field()
        fechar.clik_fechar()

        assert data.URL_BUGBANK == 'https://bugbank.netlify.app/'

    def test_acessar(self):
        self.test_fechar()
        acessar = main.acessar(self.driver)
        acessar.wait_for_load_field()
        acessar.set_email(data.EMAIL)
        acessar.set_sehna(data.SEHNA)
        acessar.clik_acessar()

        assert data.URL_BUGBANK == 'https://bugbank.netlify.app/'

    def test_sair(self):
        self.test_acessar()
        sair = main.sair(self.driver)
        sair.wait_for_load_field()
        sair.clik_sair()

        assert data.URL_BUGBANK == 'https://bugbank.netlify.app/'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()






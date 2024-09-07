# Proyecto BugBank


*En este proyecto se automatiza el registro y acceso del usuario en la pagina web BugBank con el patron POM.

**Es necesario importar selenium para poder realizar la automatizacion. Dentro de cada archivo importaremos otros soportes requeridos adicionalmente a selenium, dependiendo de las necesidades de cada prueba.**

## El proyecto BugBank cuenta con tres archivos:

1. Data.py, este archivo cuenta con los datos necesarios para realizar la automatizacion.

    1. El URL de la pagina web.
    2. Las variantes del correo electronico  
    3. La variante nombre del usuario
    4. La variante de la contrasena
    5. La variante de la confirmacion de la contrasena

2. Main.py, en este archivo se encuentra:

    i. Las importaciones necesarias son las siguientes:

       `from selenium.webdriver.common.by import By` Esta importacion es necesaria parala busqueda de los elementos.

       `from selenium.webdriver.support import expected_conditions` Esta importacion es necesaria para saber que es lo que se esta esperando en el metodo `Explicit Wait`

       `from selenium.webdriver.support.wait import WebDriverWait` Esta importacion es necesaria para la pagina web espere y se ejecute el metodo `Explicit Wait`.

    ii. El metodo  `Explicit Wait` se encuentra en aquellas clases donde se cambian de pantalla y por lo tanto es necesario un poco mas de tiempo para encontrar el elemento solicitado.

    iii. Todas las clases tienen como primer metodo __int__ para establecer el Driver.

    iv. Cada clase contiene los localizadores necesarios para ubicar dichos elementos en la pagina y poder realizar las interacciones con funciones. Para la ejecucion de las pruebas se utilizan los metodos para hacer Clic, Explicit Wait, Self. Driver entre otros.

**Listado de las Clases:**

    * class BugBank
    * class RegisterForm
    * class fechar
    * class acessar
    * class sair

3. Test_bug_bank.py, en este archivo se ejecutan la pruebas de automatizazon para crear y acceder a una cuenta en la web de BugBank.
  Las importaciones necesarias para ejecutar las pruebas son:
    *import time
    *import data
    *import main
    *from selenium import webdriver

  Comenzamos con el metodo de clase @classmethod y el metodo setup_class(cls) declarando a clase como un argumento y controlando el driver.  En este caso Chrome.

**Listado de las Test:**

    * def test_bugbank(self): te lleva a la pagina del formulario
    * def test_register_form(self): llena el formulario para la creacion de una nueva cuenta
    * def test_fechar(self): acepta la creacion de una nueva cuenta
    * def test_acessar(self): accede a la cuenta
    * def test_sair(self): sale de la cuenta del usuario

 Por ultimo el metodo teardown_class() finaliza las pruebas cerrando el navegador y detiene el driver.

Informe de Pruebas Manuales de la Interfaz de Usuario para BugBank (UI).

Dentro del proyecto, se llevaron a cabo pruebas manuales sobre la interfaz de usuario (UI), se crearon y ejecutaron casos de prueba. El enfoque de caja negra permitió validar la funcionalidad de la UI desde la perspectiva del usuario final, centrándose en la entrada y salida de datos sin considerar la lógica interna del sistema.

Se logro identificar fallos evaluando la usabilidad, interacción y comportamiento de la UI en distintos escenarios. Estas pruebas permitieron descubrir defectos relacionados con la experiencia de usuario (UX) y la integridad funcional del sistema.

Las pruebas ejecutadas incluyeron la verificación de flujos críticos, validaciones en campos, controles de navegación y otros elementos interactivos clave, con el objetivo de garantizar un rendimiento adecuado de la UI y detectar cualquier comportamiento inesperado.

Estas pruebas fueron multiplataforma para evaluar el desempeño en cada una de ellas.

Compartimos el link en el cual se encuentran los casos de prueba.

https://docs.google.com/spreadsheets/d/1EYZ55kAx_-yTfh5yvTu3EqjOABivC1fe55L7baRA-Yo/edit?usp=sharing

## Muchas gracias!!!
### Equipo 2

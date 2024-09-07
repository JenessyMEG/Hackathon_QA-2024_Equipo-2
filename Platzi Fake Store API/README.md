# Platzi Fake Store API

## Descripción del Proyecto

Este repositorio contiene las pruebas exhaustivas realizadas para la Platzi Fake Store API, una API que proporciona productos de tienda, usuarios, categorías y autenticación para fines educativos. Se han realizado pruebas automatizadas y manuales para validar la funcionalidad de la API, asegurando que todas las características se comporten como se espera. Se han implementado pruebas automatizadas utilizando Python y unittest para validar las funcionalidades clave de la API, que incluyen productos, filtros de productos, categorías y autenticación de usuarios. Además, se han realizado pruebas manuales en Postman para asegurar la cobertura completa y la identificación de errores.
## Objetivos del Proyecto

1. **Validar el funcionamiento correcto** de los endpoints principales de la API.
2. **Diseñar y automatizar casos de prueba** para asegurar respuestas adecuadas de la API frente a solicitudes (GET, POST, PUT, DELETE).
3. **Reportar defectos** encontrados en las respuestas de la API o en el comportamiento del servidor.

## Endpoints Probados

- **Productos**
  - `GET /products` - Obtener una lista de productos.
  - `GET /products/{id}` - Obtener un producto específico por ID.
  - `POST /products` - Crear un nuevo producto.
  - `PUT /products/{id}` - Actualizar un producto existente.
  - `DELETE /products/{id}` - Eliminar un producto.

- **Filtros de Productos**
  - Filtrar productos por categoría, título y rango de precio.

- **Categorías**
  - `GET /categories` - Obtener todas las categorías.
  - `GET /categories/{id}` - Obtener una categoría específica por ID.
  - `POST /categories` - Crear una nueva categoría.
  - `PUT /categories/{id}` - Actualizar una categoría existente.
  - `DELETE /categories/{id}` - Eliminar una categoría.

- **Usuarios y Autenticación**
  - `POST /auth/login` - Autenticación y obtención de tokens.
  - `GET /users` - Obtener todos los usuarios.
  - `GET /users/{id}` - Obtener un usuario específico por ID.
  - `POST /users` - Crear un nuevo usuario.
  - `PUT /users/{id}` - Actualizar un usuario existente.
  - `POST /users/is-available` - Verificar la disponibilidad de un correo electrónico.

## Herramientas Utilizadas

- **Postman**: Para la ejecución de pruebas manuales y documentación.
- **PyCharm**: Para la automatización de pruebas y gestión del código.
- **Python y unittest**: Para la implementación de pruebas automatizadas.
- **Excel**: Para documentar casos de prueba y reportar defectos.
- **Jira**: Para el seguimiento y documentación de los informes de errores.

## Estructura del Proyecto

El proyecto está organizado en archivos de prueba que corresponden a las diferentes categorías de la API:
Se realizaron pruebas para validar que las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) funcionen correctamente en productos, categorías y usuarios.

- **`test_products.py`**: Pruebas automatizadas para la gestión de productos, incluyendo operaciones CRUD (crear, leer, actualizar y eliminar).
- **`test_filter_products.py`**: Pruebas para validar los filtros disponibles en la API de productos, como filtrado por título, precio y categoría.
- **`test_categories.py`**: Pruebas para la gestión de categorías, incluyendo operaciones CRUD y la verificación de productos asociados a cada categoría.
- **`test_users_auth.py`**: Pruebas para la autenticación de usuarios, incluyendo registro, inicio de sesión y verificación de credenciales.
- **`README`**: Este documento donde se incluye la descripción, objetivos, edpoints utilizados, herramientas, la estructura, prubas automatizadas y pruebas manuales, adjuntando un archivo con los casos de prueba.

## Pruebas Automatizadas

Las pruebas automatizadas se han implementado utilizando el marco de pruebas `unittest` en Python. Cada archivo de prueba contiene casos de prueba que validan diferentes aspectos de la API:

### `test_products.py`

- **Pruebas CRUD de productos**: Verifica la capacidad de crear, leer, actualizar y eliminar productos.
- **Pruebas de integridad de datos**: Asegura que los productos se devuelvan con los campos esperados y los valores correctos.

### `test_filter_products.py`

- **Filtrado por título**: Verifica que los productos se filtren correctamente por título.
- **Filtrado por precio**: Asegura que los productos se filtren correctamente por precio.
- **Filtrado por rango de precios**: Verifica que los productos se filtren correctamente dentro de un rango de precios.
- **Filtrado por categoría**: Asegura que los productos se filtren correctamente por categoría.
- **Filtrado con múltiples parámetros**: Verifica la combinación de múltiples filtros.
- **Filtrado con límite y desplazamiento**: Asegura que los resultados se paginen correctamente.

### `test_categories.py`

- **Obtención de todas las categorías**: Verifica que todas las categorías se obtengan correctamente.
- **Obtención de una categoría por ID**: Asegura que se pueda obtener una categoría específica por su ID.
- **Creación de una categoría**: Verifica la capacidad de crear una nueva categoría.
- **Actualización de una categoría**: Asegura que se pueda actualizar una categoría existente.
- **Eliminación de una categoría**: Verifica la capacidad de eliminar una categoría.
- **Obtención de productos por categoría**: Asegura que los productos se obtengan correctamente para una categoría específica.

### `test_users_auth.py`

- **Registro de usuarios**: Verifica el proceso de registro de nuevos usuarios.
- **Inicio de sesión**: Asegura que los usuarios puedan iniciar sesión correctamente.
- **Verificación de credenciales**: Asegura que las credenciales de los usuarios sean correctas y válidas.

## Pruebas Manuales

Además de las pruebas automatizadas, se han realizado pruebas manuales utilizando Postman para validar los endpoints de la API y detectar posibles errores. Se ha documentado exhaustivamente cada caso de prueba y se ha recopilado un informe de errores en un archivo Excel adjunto.

## Documentación Adicional

Se incluye un archivo de Excel con los casos de prueba detallados y los enlaces al informe de errores encontrado durante las pruebas. Este archivo proporciona una visión completa de los casos de prueba y los problemas detectados.

- [Enlace al archivo Excel de casos de prueba y errores](https://docs.google.com/spreadsheets/d/1EYZ55kAx_-yTfh5yvTu3EqjOABivC1fe55L7baRA-Yo/edit?usp=sharing)

## Cómo Ejecutar las Pruebas

Para ejecutar las pruebas automatizadas, asegúrate de tener `Python`, `unittest` y `requests` instalados en tu entorno.

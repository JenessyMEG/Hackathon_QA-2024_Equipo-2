##
- <a name="_224u9ma7ck5j"></a>Descripción: se realizaron pruebas manuales a través de Postman. Se seleccionó el endpoint de creación de reservas. El objetivo de estas pruebas fue asegurar que la API funcione correctamente y maneje adecuadamente tanto  entradas válidas como  inválidas en los campos.
- Endpoint seleccionado para las pruebas: 
  - Endpoint: /booking
  - Método HTTP: POST
  - Formato de Solicitud: JSON
    - Cuerpo de la solicitud: 

      {

      `    `"firstname": "Sally",

      `    `"lastname": "Brown",

      `    `"totalprice": 111,

      `    `"depositpaid": true,

      `    `"bookingdates": {

      `        `"checkin": "2013-02-23",

      `        `"checkout": "2014-10-23"

      `    `},

      `    `"additionalneeds": "Breakfast"

      }

      ![](Aspose.Words.d8f49c6c-713d-4ca4-9bf4-79fccd933f3a.001.png)
##
- <a name="_vt4f4sz7mo2o"></a>Pruebas realizadas: 
- Positivas 
  - Se crea correctamente una reserva con todos los campos requeridos con datos válidos
  - Validación de ingreso de datos de acuerdo al campo  
- Negativas 
  - Ingreso de datos incorrectos para cada campo 
  - Envió de solicitudes con campos vacíos 
- Reportes de errores: los casos de pruebas permitieron encontrar errores que  fueron documentados en JIRA
- Herramientas utilizadas 
  - POSTMAN 
  - JIRA



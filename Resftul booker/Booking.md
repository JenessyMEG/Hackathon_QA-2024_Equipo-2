
 ![Claro Colores Cocinar Sitio Web Twitter Encabezado](https://github.com/user-attachments/assets/6df3d765-8ae7-45f0-8ca1-4ac6075731ed)

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
- Rendimiento  
  - Se enviaron 100 y 200 solicitudes secuenciales para ver cómo se comportaba la API a través de Postman
  - La API funciona favorablemente bajo una carga continua de solicitudes, todas las solicitudes se crean con un código 200OK (En esta carpeta se ecuentran los resultados exportados desde Postman y videos que muestran la creación de las solicitudes)
- Reportes de errores: los casos de pruebas permitieron encontrar errores que  fueron documentados en JIRA
- Herramientas utilizadas 
  - POSTMAN   
  - JIRA
  - EXCEL (DOCUMENTACIÓN DE CASOS DE PRUEBA)
- Enlaces a: 
  - Casos de prueba: https://docs.google.com/spreadsheets/d/1EYZ55kAx_-yTfh5yvTu3EqjOABivC1fe55L7baRA-Yo/edit?usp=sharing
  - Resultado de la prueba de rendimiento con 100 request: https://github.com/JenessyMEG/Hackathon_QA-2024_Equipo-2/blob/main/Resftul%20booker/Hackathon.postman_test_run.json
  - Resultado de la prueba de rendimiento con 200 request: https://github.com/JenessyMEG/Hackathon_QA-2024_Equipo-2/blob/main/Resftul%20booker/Hackathon.postman_test_run_200



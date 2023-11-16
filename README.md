# DevOps TP
Trabajo práctico para aplicar los conceptos y herramientas aprendidas en el curso de DevOps.

## Obten el API Key de Datadog
Por motivos de seguridad el API Key no se puede commitear al repo, por lo cual está guardado como un **secret en el repo**. El placeholder en los docker-compose es sólo para recordarnos y seguir el mismo patrón de los otros secrets, el mismo no es introducido por github debido a como armamos los github actions (pero se podría).

## Correr la app a nivel local
Para correr la aplicación usando el código local deberás correr el siguiente comando:   
```
docker-compose up -d
```

En cualquier navegador --> http://localhost:3000/employee (muestra todos los empleados de la base de datos)

[
  {
    "id": "0",
    "name": "Josephine Hawkins",
    "phone": "+1 (862) 428-2160"
  },
  {
    "id": "1",
    "name": "Barrett Fulton",
    "phone": "+1 (881) 496-2875"
  },
  {
    "id": "2",
    "name": "Erin Lynch",
    "phone": "+1 (827) 524-3459"
  },
  {
    "id": "3",
    "name": "Valerie Potter",
    "phone": "+1 (965) 586-2319"
  },
  {
    "id": "4",
    "name": "Brandi Douglas",
    "phone": "+1 (817) 422-3504"
  }
]

Otra prueba: http://localhost:3000/employee/0

Muestra el empleado "0", con un mini formato de tabla: 
    Información del Empleado
    ID	Nombre	Telefono
    0	Josephine Hawkins	+1 (862) 428-2160

## Correr la app a nivel prod
Para correr la aplicación usando la imagen desde dockerhub usar:   
```
docker-compose -f docker-compose.prod.yml up -d
```

## Unit test 

PS C:\Users\user_n2\Desktop\devops_tp\devops-tp\src> python -m unittest test_app
...
----------------------------------------------------------------------
Ran 3 tests in 0.007s

OK
# DevOps TP
Trabajo práctico para aplicar los conceptos y herramientas aprendidas en el curso de DevOps

Una vez que te bajas el repo, debes: 

a. buildear la imagen de docker

    a.1) usando el dockerfile 
            docker build -t devopstp . 

    a.2) o usando el docker-compose.yml
            docker compose up -d        // si usas esta opcion ya no tenes que ir por el punto b,
                                        // xq el programa ya queda en ejecución

b. <solo si fuiste por el camino a.1> 
   Despues de buildear la imagen deberias poner a correr el contenedor, asi:  
            docker run -it --publish 7000:3000 devopstp

Para probar el funcionamiento de la app:

En cualquier navegador --> http://localhost:7000/employee (muestra todos los empleados de la base de datos)

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

Otra prueba: http://localhost:7000/employee/0

Muestra el empleado "0", con un mini formato de tabla: 
    Información del Empleado
    ID	Nombre	Telefono
    0	Josephine Hawkins	+1 (862) 428-2160
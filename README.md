# CampusNet – Sistema de Relaciones Universitarias

## Descripción

CampusNet es una aplicación de consola desarrollada en Python que permite administrar una red de usuarios universitarios mediante un **grafo dirigido**.

Los usuarios pueden ser estudiantes, profesores o egresados. Cada usuario representa un vértice y cada relación entre usuarios representa una arista dirigida.

El sistema permite registrar, actualizar y eliminar usuarios y relaciones, realizar recorridos BFS y DFS, detectar ciclos y consultar información sobre la red.

## Objetivo general

Desarrollar un sistema de gestión de relaciones universitarias utilizando grafos dirigidos y programación orientada a objetos en Python, aplicando el patrón de arquitectura Modelo-Vista-Controlador (MVC).

## Tecnologías utilizadas

- Python 3
- Programación orientada a objetos
- Arquitectura MVC
- Grafos dirigidos
- Biblioteca `collections.deque`
- Biblioteca `unittest`
- Visual Studio Code

## Estructura del proyecto

```text
CampusNet/
├── controller/
│   └── campus_controller.py
├── model/
│   ├── vertex.py
│   ├── edge.py
│   └── graph.py
├── view/
│   └── console_view.py
├── tests/
│   └── test_graph.py
├── main.py
└── README.md
```

## Arquitectura MVC

**Modelo:** contiene las clases `Vertex`, `Edge` y `Graph`, encargadas de representar usuarios, relaciones y operaciones sobre el grafo.

**Vista:** `ConsoleView` presenta la información y recibe las entradas del usuario mediante la consola.

**Controlador:** `CampusController` coordina la interacción entre el modelo y la vista.

## Funcionalidades

### Gestión CRUD

- Registrar usuarios.
- Consultar usuarios y relaciones.
- Actualizar información de usuarios.
- Eliminar usuarios y sus relaciones.
- Crear relaciones dirigidas.
- Eliminar relaciones.
- Validar usuarios y relaciones duplicados.

### Algoritmos de grafos

**BFS (Breadth-First Search):** realiza un recorrido en anchura utilizando una cola FIFO.

**DFS (Depth-First Search):** realiza un recorrido en profundidad mediante recursividad y permite detectar aristas de retroceso asociadas a ciclos.

**Alcanzabilidad:** determina si existe un camino dirigido entre dos usuarios.

### Consultas sociales

- Usuarios sin seguidores.
- Usuarios más influyentes según su grado de entrada.
- Usuarios más activos según su grado de salida.

## Datos iniciales

La aplicación carga 12 usuarios y 19 relaciones dirigidas para demostrar su funcionamiento.

## Ejecución

Abrir una terminal en la carpeta principal del proyecto y ejecutar:

```powershell
python main.py
```

## Pruebas unitarias

CampusNet utiliza `unittest` para verificar las operaciones principales del modelo.

Ejecutar:

```powershell
python -m unittest discover -s tests -v
```

Se han ejecutado satisfactoriamente 11 pruebas, incluyendo creación, actualización y eliminación de usuarios, relaciones duplicadas, BFS, DFS, alcanzabilidad y sincronización de aristas.

## Consideraciones

- Los identificadores de usuario se normalizan a mayúsculas.
- Los roles admitidos son `estudiante`, `profesor` y `egresado`.
- Las relaciones son dirigidas.
- El sistema utiliza almacenamiento en memoria; los cambios realizados durante la ejecución no se guardan en una base de datos.

## Estado del proyecto

Implementación funcional con arquitectura MVC, operaciones CRUD, recorridos de grafos, consultas sociales y pruebas unitarias satisfactorias.
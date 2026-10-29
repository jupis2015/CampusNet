

from model.graph import Graph
from view.console_view import ConsoleView


class CampusController:

    def __init__(self):
        # Inicializar el modelo y la vista
        self.grafo = Graph()
        self.vista = ConsoleView()

    def ejecutar(self):

        # ==========================================
        # 1. REGISTRAR USUARIOS
        # ==========================================

        usuarios = [
            ("U01", "Carlos", "estudiante"),
            ("U02", "Maria", "profesor"),
            ("U03", "Pedro", "egresado"),
            ("U04", "Ana", "estudiante"),
            ("U05", "Luis", "profesor"),
            ("U06", "Sofia", "estudiante"),
            ("U07", "Andres", "egresado"),
            ("U08", "Laura", "estudiante"),
            ("U09", "Diego", "profesor"),
            ("U10", "Camila", "estudiante"),
            ("U11", "Jorge", "egresado"),
            ("U12", "Valentina", "estudiante")
        ]

        for id, nombre, rol in usuarios:
            self.grafo.agregar_usuario(id, nombre, rol)

        # ==========================================
        # 2. REGISTRAR RELACIONES DIRIGIDAS
        # ==========================================

        relaciones = [
            ("U01", "U02"),
            ("U01", "U03"),
            ("U01", "U04"),
            ("U01", "U05"),

            ("U02", "U03"),
            ("U02", "U06"),
            ("U02", "U07"),
            ("U02", "U08"),

            ("U03", "U01"),
            ("U03", "U09"),

            ("U04", "U05"),
            ("U05", "U06"),
            ("U06", "U07"),
            ("U07", "U08"),
            ("U08", "U09"),
            ("U09", "U10"),
            ("U10", "U03"),

            ("U11", "U02"),
            ("U12", "U04")
        ]

        for origen, destino in relaciones:
            self.grafo.agregar_relacion(origen, destino)

        # ==========================================
        # 3. MOSTRAR INFORMACION DEL GRAFO
        # ==========================================

        self.vista.mostrar_titulo(
            "CAMPUSNET - RED SOCIAL ACADEMICA"
        )

        self.vista.mostrar_usuarios(
            self.grafo.vertices
        )

        self.vista.mostrar_grafo(
            self.grafo.adyacencia
        )

        # ==========================================
        # 4. MOSTRAR ESTADISTICAS GENERALES
        # ==========================================

        total_usuarios = len(self.grafo.vertices)

        total_relaciones = sum(
            len(destinos)
            for destinos in self.grafo.adyacencia.values()
        )

        self.vista.mostrar_titulo(
            "ESTADISTICAS GENERALES"
        )

        self.vista.mostrar_estadisticas(
            total_usuarios,
            total_relaciones
        )

        # ==========================================
        # 5. RECORRIDOS BFS
        # ==========================================

        self.vista.mostrar_titulo(
            "RECORRIDOS BFS - BUSQUEDA EN ANCHURA"
        )

        usuarios_inicio = ["U01", "U04", "U11"]

        for inicio in usuarios_inicio:

            recorrido = self.grafo.bfs(inicio)

            self.vista.mostrar_bfs(
                inicio,
                recorrido
            )

        # ==========================================
        # 6. RECORRIDO DFS COMPLETO
        # ==========================================

        self.vista.mostrar_titulo(
            "RECORRIDO DFS - BUSQUEDA EN PROFUNDIDAD"
        )

        recorrido_dfs, ciclos = self.grafo.dfs_completo()

        self.vista.mostrar_dfs(
            recorrido_dfs,
            ciclos
        )

        # ==========================================
        # 7. CONSULTAS SOCIALES
        # ==========================================

        self.vista.mostrar_titulo(
            "CONSULTAS SOCIALES"
        )

        sin_seguidores = (
            self.grafo.usuarios_sin_seguidores()
        )

        influyentes, grado_entrada = (
            self.grafo.usuarios_influyentes()
        )

        activos, grado_salida = (
            self.grafo.usuarios_activos()
        )

        self.vista.mostrar_consultas(
            sin_seguidores,
            influyentes,
            grado_entrada,
            activos,
            grado_salida
        )

        # ==========================================
        # 8. VERIFICAR ALCANZABILIDAD
        # ==========================================

        self.vista.mostrar_titulo(
            "CONSULTAS DE ALCANZABILIDAD"
        )

        consultas = [
            ("U01", "U10"),
            ("U01", "U12"),
            ("U11", "U05"),
            ("U12", "U11")
        ]

        for origen, destino in consultas:
            resultado = self.grafo.es_alcanzable(
                origen, destino
            )

            self.vista.mostrar_alcanzabilidad(
                origen, destino, resultado
            )

    def menu_interactivo(self):

        while True:
            self.vista.mostrar_menu()

            opcion = self.vista.solicitar_dato(
                "Seleccione una opcion: "
            )

            if opcion == "1":
                self.vista.mostrar_usuarios(
                    self.grafo.vertices
                )
                self.vista.mostrar_grafo(
                    self.grafo.adyacencia
                )

            elif opcion == "2":
                id = self.vista.solicitar_dato("ID: ")
                nombre = self.vista.solicitar_dato("Nombre: ")
                rol = self.vista.solicitar_dato("Rol: ")

                resultado = self.grafo.agregar_usuario(
                    id, nombre, rol
                )

                self.vista.mostrar_mensaje(
                    "Usuario agregado correctamente."
                    if resultado else
                    "No se pudo agregar el usuario."
                )

            elif opcion == "3":
                id = self.vista.solicitar_dato("ID: ")
                nombre = self.vista.solicitar_dato(
                    "Nuevo nombre: "
                )
                rol = self.vista.solicitar_dato(
                    "Nuevo rol: "
                )

                resultado = self.grafo.actualizar_usuario(
                    id, nombre, rol
                )

                self.vista.mostrar_mensaje(
                    "Usuario actualizado."
                    if resultado else
                    "No se pudo actualizar."
                )

            elif opcion == "4":
                id = self.vista.solicitar_dato(
                    "ID del usuario: "
                )

                resultado = self.grafo.eliminar_usuario(id)

                self.vista.mostrar_mensaje(
                    "Usuario eliminado."
                    if resultado else
                    "Usuario no encontrado."
                )

            elif opcion == "5":
                origen = self.vista.solicitar_dato(
                    "Usuario origen: "
                )
                destino = self.vista.solicitar_dato(
                    "Usuario destino: "
                )

                resultado = self.grafo.agregar_relacion(
                    origen, destino
                )

                self.vista.mostrar_mensaje(
                    "Relacion agregada."
                    if resultado else
                    "No se pudo agregar la relacion."
                )

            elif opcion == "6":
                origen = self.vista.solicitar_dato(
                    "Usuario origen: "
                )
                destino = self.vista.solicitar_dato(
                    "Usuario destino: "
                )

                resultado = self.grafo.eliminar_relacion(
                    origen, destino
                )

                self.vista.mostrar_mensaje(
                    "Relacion eliminada."
                    if resultado else
                    "No se pudo eliminar la relacion."
                )

            elif opcion == "7":
                inicio = self.vista.solicitar_dato(
                    "Usuario inicial: "
                )

                recorrido = self.grafo.bfs(inicio)

                self.vista.mostrar_bfs(inicio, recorrido)

            elif opcion == "8":
                recorrido, ciclos = self.grafo.dfs_completo()

                self.vista.mostrar_dfs(recorrido, ciclos)

            elif opcion == "9":
                sin_seguidores = (
                    self.grafo.usuarios_sin_seguidores()
                )

                influyentes, grado_entrada = (
                    self.grafo.usuarios_influyentes()
                )

                activos, grado_salida = (
                    self.grafo.usuarios_activos()
                )

                self.vista.mostrar_consultas(
                    sin_seguidores,
                    influyentes,
                    grado_entrada,
                    activos,
                    grado_salida
                )

            elif opcion == "0":
                self.vista.mostrar_mensaje(
                    "Gracias por utilizar CampusNet."
                )
                break

            else:
                self.vista.mostrar_mensaje(
                    "Opcion no valida."
                )

            # Mostrar el estado actualizado del grafo
            if opcion in ("2", "3", "4", "5", "6"):
                self.vista.mostrar_usuarios(
                    self.grafo.vertices
                )
                self.vista.mostrar_grafo(
                    self.grafo.adyacencia
                )

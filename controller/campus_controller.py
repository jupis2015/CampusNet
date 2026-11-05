
from model.graph import Graph
from view.console_view import ConsoleView


class CampusController:

    def __init__(self):

        # Modelo
        self.grafo = Graph()

        # Vistas
        self.vista = ConsoleView()

    # ==========================================
    # 1. CARGAR DATOS INICIALES
    # ==========================================

    def cargar_datos(self):

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

        for id, nombre, rol in usuarios:
            self.grafo.agregar_usuario(id, nombre, rol)

        for origen, destino in relaciones:
            self.grafo.agregar_relacion(origen, destino)

    # ==========================================
    # 2. EJECUCION INICIAL
    # ==========================================

    def ejecutar(self):

        self.cargar_datos()

        self.vista.mostrar_titulo(
            "CAMPUSNET - RED UNIVERSITARIA"
        )

        self.vista.mostrar_usuarios(
            self.grafo.vertices
        )

        self.vista.mostrar_grafo(
            self.grafo.adyacencia
        )

        self.vista.mostrar_estadisticas(
            len(self.grafo.vertices),
            len(self.grafo.aristas)
        )

        # Recorridos BFS de ejemplo
        for inicio in ("U01", "U04", "U11"):

            recorrido = self.grafo.bfs(inicio)

            self.vista.mostrar_bfs(
                inicio,
                recorrido
            )

        # DFS completo
        recorrido, ciclos = (
            self.grafo.dfs_completo()
        )

        self.vista.mostrar_dfs(
            recorrido,
            ciclos
        )

        # Consultas sociales
        self.mostrar_consultas_sociales()

        # Consultas de alcanzabilidad
        consultas = [
            ("U01", "U10"),
            ("U01", "U12"),
            ("U11", "U05"),
            ("U12", "U11")
        ]

        for origen, destino in consultas:

            resultado = self.grafo.es_alcanzable(
                origen,
                destino
            )

            self.vista.mostrar_alcanzabilidad(
                origen,
                destino,
                resultado
            )

    # ==========================================
    # 3. CONSULTAS SOCIALES
    # ==========================================

    def mostrar_consultas_sociales(self):

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
    # 4. MOSTRAR USUARIOS Y RELACIONES
    # ==========================================

    def mostrar_red(self):

        self.vista.mostrar_usuarios(
            self.grafo.vertices
        )

        self.vista.mostrar_grafo(
            self.grafo.adyacencia
        )

        self.vista.mostrar_estadisticas(
            len(self.grafo.vertices),
            len(self.grafo.aristas)
        )

    # ==========================================
    # 5. MENU INTERACTIVO
    # ==========================================

    def menu_interactivo(self):

        while True:

            self.vista.mostrar_menu()

            opcion = self.vista.solicitar_dato(
                "Seleccione una opcion: "
            )

            # ----------------------------------
            # OPCION 1: MOSTRAR RED
            # ----------------------------------

            if opcion == "1":

                self.mostrar_red()

            # ----------------------------------
            # OPCION 2: AGREGAR USUARIO
            # ----------------------------------

            elif opcion == "2":

                id = self.vista.solicitar_dato(
                    "ID: "
                )

                nombre = self.vista.solicitar_dato(
                    "Nombre: "
                )

                rol = self.vista.solicitar_dato(
                    "Rol (estudiante/profesor/egresado): "
                )

                resultado = self.grafo.agregar_usuario(
                    id,
                    nombre,
                    rol
                )

                if resultado:
                    self.vista.mostrar_mensaje(
                        "Usuario agregado correctamente."
                    )
                else:
                    self.vista.mostrar_mensaje(
                        "No se pudo agregar el usuario."
                    )

                self.mostrar_red()

            # ----------------------------------
            # OPCION 3: ACTUALIZAR USUARIO
            # ----------------------------------

            elif opcion == "3":

                id = self.vista.solicitar_dato(
                    "ID del usuario: "
                )

                nombre = self.vista.solicitar_dato(
                    "Nuevo nombre: "
                )

                rol = self.vista.solicitar_dato(
                    "Nuevo rol: "
                )

                resultado = self.grafo.actualizar_usuario(
                    id,
                    nombre,
                    rol
                )

                if resultado:
                    self.vista.mostrar_mensaje(
                        "Usuario actualizado correctamente."
                    )
                else:
                    self.vista.mostrar_mensaje(
                        "No se pudo actualizar el usuario."
                    )

                self.mostrar_red()

            # ----------------------------------
            # OPCION 4: ELIMINAR USUARIO
            # ----------------------------------

            elif opcion == "4":

                id = self.vista.solicitar_dato(
                    "ID del usuario: "
                )

                resultado = self.grafo.eliminar_usuario(
                    id
                )

                if resultado:
                    self.vista.mostrar_mensaje(
                        "Usuario eliminado correctamente."
                    )
                else:
                    self.vista.mostrar_mensaje(
                        "El usuario no existe."
                    )

                self.mostrar_red()

            # ----------------------------------
            # OPCION 5: AGREGAR RELACION
            # ----------------------------------

            elif opcion == "5":

                origen = self.vista.solicitar_dato(
                    "Usuario origen: "
                )

                destino = self.vista.solicitar_dato(
                    "Usuario destino: "
                )

                resultado = self.grafo.agregar_relacion(
                    origen,
                    destino
                )

                if resultado:
                    self.vista.mostrar_mensaje(
                        "Relacion agregada correctamente."
                    )
                else:
                    self.vista.mostrar_mensaje(
                        "No se pudo agregar la relacion."
                    )

                self.mostrar_red()

            # ----------------------------------
            # OPCION 6: ELIMINAR RELACION
            # ----------------------------------

            elif opcion == "6":

                origen = self.vista.solicitar_dato(
                    "Usuario origen: "
                )

                destino = self.vista.solicitar_dato(
                    "Usuario destino: "
                )

                resultado = self.grafo.eliminar_relacion(
                    origen,
                    destino
                )

                if resultado:
                    self.vista.mostrar_mensaje(
                        "Relacion eliminada correctamente."
                    )
                else:
                    self.vista.mostrar_mensaje(
                        "La relacion no existe."
                    )

                self.mostrar_red()

            # ----------------------------------
            # OPCION 7: EJECUTAR BFS
            # ----------------------------------

            elif opcion == "7":

                inicio = self.vista.solicitar_dato(
                    "Usuario inicial para BFS: "
                ).upper()

                recorrido = self.grafo.bfs(inicio)

                if recorrido:

                    self.vista.mostrar_bfs(
                        inicio,
                        recorrido
                    )

                else:

                    self.vista.mostrar_mensaje(
                        "El usuario no existe."
                    )

            # ----------------------------------
            # OPCION 8: EJECUTAR DFS
            # ----------------------------------

            elif opcion == "8":

                recorrido, ciclos = (
                    self.grafo.dfs_completo()
                )

                self.vista.mostrar_dfs(
                    recorrido,
                    ciclos
                )

            # ----------------------------------
            # OPCION 9: CONSULTAS SOCIALES
            # ----------------------------------

            elif opcion == "9":

                self.mostrar_consultas_sociales()

            

            # ----------------------------------
            # OPCION 0: SALIR
            # ----------------------------------

            elif opcion == "0":

                self.vista.mostrar_mensaje(
                    "Gracias por utilizar CampusNet."
                )

                break

            # ----------------------------------
            # OPCION NO VALIDA
            # ----------------------------------

            else:

                self.vista.mostrar_mensaje(
                    "Opcion no valida. Intente nuevamente."
                )

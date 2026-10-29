

class ConsoleView:

    def mostrar_titulo(self, titulo):
        print("\n" + "=" * 55)
        print(titulo)
        print("=" * 55)

    def mostrar_usuarios(self, usuarios):
        print("\nUSUARIOS REGISTRADOS:")

        for usuario in usuarios.values():
            print(f"  {usuario}")

    def mostrar_grafo(self, adyacencia):
        print("\nLISTA DE ADYACENCIA:")

        for origen, destinos in adyacencia.items():

            relaciones = (
                ", ".join(destinos)
                if destinos else "Ninguna"
            )

            print(f"  {origen} -> {relaciones}")

    def mostrar_bfs(self, inicio, recorrido):
        print(f"\nBFS desde {inicio}")

        print(
            "Orden de visita:",
            " -> ".join(recorrido)
        )

        print(
            "Vertices alcanzados:",
            len(recorrido)
        )

    def mostrar_dfs(self, recorrido, ciclos):
        print("\nORDEN DE DESCUBRIMIENTO DFS:")
        print(" -> ".join(recorrido))

        print(f"\nTotal de vertices visitados: {len(recorrido)}")

        if ciclos:
            print("\nCICLOS DETECTADOS:")
            for origen, destino in ciclos:
                print(
                    f"Arista de retroceso: "
                    f"{origen} -> {destino}"
                )
        else:
            print("\nNo se detectaron ciclos.")
    
    def mostrar_consultas(
        self,
        sin_seguidores,
        influyentes,
        grado_entrada,
        activos,
        grado_salida
    ):
        print("\nUSUARIOS SIN SEGUIDORES:")
        print(", ".join(sin_seguidores) or "Ninguno")

        print("\nUSUARIOS MAS INFLUYENTES:")
        print(", ".join(influyentes))
        print(f"Seguidores: {grado_entrada}")

        print("\nUSUARIOS MAS ACTIVOS:")
        print(", ".join(activos))
        print(f"Usuarios que siguen: {grado_salida}")

    def mostrar_alcanzabilidad(
        self, origen, destino, resultado
    ):
        if resultado:
            print(
                f"SI existe un camino desde "
                f"{origen} hasta {destino}"
            )
        else:
            print(
                f"NO existe un camino desde "
                f"{origen} hasta {destino}"
            )

    def mostrar_menu(self):
        print("\n" + "=" * 55)
        print("CAMPUSNET - MENU PRINCIPAL")
        print("=" * 55)

        print("1. Mostrar usuarios y relaciones")
        print("2. Agregar usuario")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Agregar relacion")
        print("6. Eliminar relacion")
        print("7. Ejecutar BFS")
        print("8. Ejecutar DFS")
        print("9. Consultas sociales")
        print("0. Salir")

    def solicitar_dato(self, mensaje):
        return input(mensaje).strip()

    def mostrar_mensaje(self, mensaje):
        print(f"\n{mensaje}")

    def mostrar_estadisticas(self, usuarios, relaciones):
        print(f"Total de usuarios: {usuarios}")
        print(f"Total de relaciones: {relaciones}")

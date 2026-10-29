
from collections import deque

from model.vertex import Vertex
from model.edge import Edge


class Graph:

    def __init__(self):
        # Diccionario de usuarios
        self.vertices = {}

        # Lista de adyacencia
        self.adyacencia = {}

        # Objetos que representan relaciones dirigidas
        self.aristas = []

    # ==========================================
    # 1. AGREGAR USUARIO
    # ==========================================

    def agregar_usuario(self, id, nombre, rol):

        id = id.strip().upper()
        nombre = nombre.strip()
        rol = rol.strip().lower()

        if not id or not nombre:
            return False

        if id in self.vertices:
            return False

        if rol not in ("estudiante", "profesor", "egresado"):
            return False

        self.vertices[id] = Vertex(id, nombre, rol)
        self.adyacencia[id] = []

        return True

    # ==========================================
    # 2. AGREGAR RELACION DIRIGIDA
    # ==========================================

    def agregar_relacion(self, origen, destino):

        origen = origen.strip().upper()
        destino = destino.strip().upper()

        if origen not in self.vertices:
            return False

        if destino not in self.vertices:
            return False

        if destino in self.adyacencia[origen]:
            return False

        # Registrar relación en lista de adyacencia
        self.adyacencia[origen].append(destino)

        # Crear el objeto Edge
        self.aristas.append(Edge(origen, destino))

        return True

    # ==========================================
    # 3. RECORRIDO BFS
    # ==========================================

    def bfs(self, inicio):

        inicio = inicio.strip().upper()

        if inicio not in self.vertices:
            return []

        visitados = {inicio}
        cola = deque([inicio])
        recorrido = []

        while cola:

            actual = cola.popleft()
            recorrido.append(actual)

            for vecino in self.adyacencia[actual]:

                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

        return recorrido

    # ==========================================
    # 4. RECORRIDO DFS COMPLETO
    # ==========================================

    def dfs_completo(self):

        visitados = set()
        en_proceso = set()
        recorrido = []
        ciclos = []

        def visitar(actual):

            visitados.add(actual)
            en_proceso.add(actual)
            recorrido.append(actual)

            for vecino in self.adyacencia[actual]:

                if vecino not in visitados:
                    visitar(vecino)

                elif vecino in en_proceso:
                    ciclos.append((actual, vecino))

            en_proceso.remove(actual)

        for usuario in self.vertices:

            if usuario not in visitados:
                visitar(usuario)

        return recorrido, ciclos

    # ==========================================
    # 5. GRADOS DE ENTRADA
    # ==========================================

    def grados_entrada(self):

        grados = {
            id: 0 for id in self.vertices
        }

        for destinos in self.adyacencia.values():

            for destino in destinos:
                grados[destino] += 1

        return grados

    # ==========================================
    # 6. USUARIOS SIN SEGUIDORES
    # ==========================================

    def usuarios_sin_seguidores(self):

        grados = self.grados_entrada()

        return [
            id for id, grado in grados.items()
            if grado == 0
        ]

    # ==========================================
    # 7. USUARIOS MAS INFLUYENTES
    # ==========================================

    def usuarios_influyentes(self):

        grados = self.grados_entrada()

        if not grados:
            return [], 0

        maximo = max(grados.values())

        usuarios = [
            id for id, grado in grados.items()
            if grado == maximo
        ]

        return usuarios, maximo

    # ==========================================
    # 8. USUARIOS MAS ACTIVOS
    # ==========================================

    def usuarios_activos(self):

        if not self.vertices:
            return [], 0

        grados = {
            id: len(destinos)
            for id, destinos in self.adyacencia.items()
        }

        maximo = max(grados.values())

        usuarios = [
            id for id, grado in grados.items()
            if grado == maximo
        ]

        return usuarios, maximo

    # ==========================================
    # 9. VERIFICAR ALCANZABILIDAD
    # ==========================================

    def es_alcanzable(self, origen, destino):

        origen = origen.strip().upper()
        destino = destino.strip().upper()

        if origen not in self.vertices:
            return False

        if destino not in self.vertices:
            return False

        recorrido = self.bfs(origen)

        return destino in recorrido

    # ==========================================
    # 10. ACTUALIZAR USUARIO
    # ==========================================

    def actualizar_usuario(self, id, nombre, rol):

        id = id.strip().upper()
        nombre = nombre.strip()
        rol = rol.strip().lower()

        if id not in self.vertices:
            return False

        if not nombre:
            return False

        if rol not in ("estudiante", "profesor", "egresado"):
            return False

        usuario = self.vertices[id]

        usuario.nombre = nombre
        usuario.rol = rol

        return True

    # ==========================================
    # 11. ELIMINAR USUARIO
    # ==========================================

    def eliminar_usuario(self, id):

        id = id.strip().upper()

        if id not in self.vertices:
            return False

        # Eliminar usuario y relaciones salientes
        del self.adyacencia[id]
        del self.vertices[id]

        # Eliminar relaciones entrantes
        for destinos in self.adyacencia.values():

            if id in destinos:
                destinos.remove(id)

        # Eliminar objetos Edge relacionados
        self.aristas = [
            arista for arista in self.aristas
            if arista.origen != id and arista.destino != id
        ]

        return True

    # ==========================================
    # 12. ELIMINAR RELACION
    # ==========================================

    def eliminar_relacion(self, origen, destino):

        origen = origen.strip().upper()
        destino = destino.strip().upper()

        if origen not in self.vertices:
            return False

        if destino not in self.vertices:
            return False

        if destino not in self.adyacencia[origen]:
            return False

        # Eliminar de la lista de adyacencia
        self.adyacencia[origen].remove(destino)

        # Eliminar el objeto Edge correspondiente
        self.aristas = [
            arista for arista in self.aristas
            if not (
                arista.origen == origen
                and arista.destino == destino
            )
        ]

        return True

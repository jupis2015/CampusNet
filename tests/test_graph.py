
import unittest

from model.graph import Graph


class TestGraph(unittest.TestCase):

    def setUp(self):
        """
        Se ejecuta antes de cada prueba.
        Crea un grafo independiente.
        """
        self.grafo = Graph()

        self.grafo.agregar_usuario(
            "U01", "Carlos", "estudiante"
        )
        self.grafo.agregar_usuario(
            "U02", "Maria", "profesor"
        )
        self.grafo.agregar_usuario(
            "U03", "Pedro", "egresado"
        )
        self.grafo.agregar_usuario(
            "U04", "Ana", "estudiante"
        )

        self.grafo.agregar_relacion("U01", "U02")
        self.grafo.agregar_relacion("U02", "U03")
        self.grafo.agregar_relacion("U03", "U01")

    # ==========================================
    # PRUEBA 1: USUARIO DUPLICADO
    # ==========================================

    def test_usuario_duplicado(self):

        resultado = self.grafo.agregar_usuario(
            "U01", "Otro Carlos", "estudiante"
        )

        self.assertFalse(resultado)
        self.assertEqual(len(self.grafo.vertices), 4)

    # ==========================================
    # PRUEBA 2: NORMALIZACION DE ID
    # ==========================================

    def test_identificadores_minusculas(self):

        resultado = self.grafo.agregar_usuario(
            "u05", "Felipe", "estudiante"
        )

        self.assertTrue(resultado)
        self.assertIn("U05", self.grafo.vertices)

    # ==========================================
    # PRUEBA 3: RELACION DUPLICADA
    # ==========================================

    def test_relacion_duplicada(self):

        resultado = self.grafo.agregar_relacion(
            "U01", "U02"
        )

        self.assertFalse(resultado)

    # ==========================================
    # PRUEBA 4: RECORRIDO BFS
    # ==========================================

    def test_bfs(self):

        recorrido = self.grafo.bfs("U01")

        self.assertEqual(
            recorrido,
            ["U01", "U02", "U03"]
        )

    # ==========================================
    # PRUEBA 5: DFS COMPLETO
    # ==========================================

    def test_dfs(self):

        recorrido, ciclos = (
            self.grafo.dfs_completo()
        )

        self.assertEqual(len(recorrido), 4)
        self.assertEqual(len(set(recorrido)), 4)
        self.assertIn(("U03", "U01"), ciclos)

    # ==========================================
    # PRUEBA 6: USUARIOS SIN SEGUIDORES
    # ==========================================

    def test_sin_seguidores(self):

        resultado = (
            self.grafo.usuarios_sin_seguidores()
        )

        self.assertEqual(resultado, ["U04"])

    # ==========================================
    # PRUEBA 7: ALCANZABILIDAD
    # ==========================================

    def test_alcanzabilidad(self):

        self.assertTrue(
            self.grafo.es_alcanzable("U01", "U03")
        )

        self.assertFalse(
            self.grafo.es_alcanzable("U01", "U04")
        )

    # ==========================================
    # PRUEBA 8: ACTUALIZAR USUARIO
    # ==========================================

    def test_actualizar_usuario(self):

        resultado = self.grafo.actualizar_usuario(
            "u01", "Carlos Gomez", "egresado"
        )

        self.assertTrue(resultado)

        self.assertEqual(
            self.grafo.vertices["U01"].nombre,
            "Carlos Gomez"
        )

    # ==========================================
    # PRUEBA 9: ELIMINAR RELACION
    # ==========================================

    def test_eliminar_relacion(self):

        resultado = self.grafo.eliminar_relacion(
            "u01", "u02"
        )

        self.assertTrue(resultado)

        self.assertNotIn(
            "U02",
            self.grafo.adyacencia["U01"]
        )

    # ==========================================
    # PRUEBA 10: ELIMINAR USUARIO
    # ==========================================

    def test_eliminar_usuario(self):

        resultado = self.grafo.eliminar_usuario(
            "u02"
        )

        self.assertTrue(resultado)

        self.assertNotIn(
            "U02",
            self.grafo.vertices
        )

        self.assertNotIn(
            "U02",
            self.grafo.adyacencia["U01"]
        )

    
    def test_sincronizacion_aristas(self):

        # Inicialmente existen tres relaciones
        self.assertEqual(len(self.grafo.aristas), 3)

        # Agregar una nueva relación
        self.assertTrue(
            self.grafo.agregar_relacion("U01", "U04")
        )

        self.assertEqual(len(self.grafo.aristas), 4)

        # Eliminar una relación
        self.assertTrue(
            self.grafo.eliminar_relacion("U01", "U04")
        )

        self.assertEqual(len(self.grafo.aristas), 3)

        # Eliminar un usuario con relaciones
        self.assertTrue(
            self.grafo.eliminar_usuario("U02")
        )

        # Solo permanece U03 -> U01
        self.assertEqual(len(self.grafo.aristas), 1)

        self.assertEqual(
            str(self.grafo.aristas[0]),
            "U03 -> U01"
        )

if __name__ == "__main__":
    unittest.main()

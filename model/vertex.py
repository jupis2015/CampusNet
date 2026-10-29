
class Vertex:
    def __init__(self, id, nombre, rol):
        self.id = id
        self.nombre = nombre
        self.rol = rol

    def __str__(self):
        return f"{self.id} - {self.nombre} ({self.rol})"

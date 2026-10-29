
class Edge:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino

    def __str__(self):
        return f"{self.origen} -> {self.destino}"

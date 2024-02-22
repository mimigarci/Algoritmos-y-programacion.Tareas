#Objeto Vendedor

class Seller:

    def __init__(self, concesionario, disponibilidad=False):
        
        self.concesionario = concesionario
        self.disponibilidad = disponibilidad

    def show(self):
        return f"""
Concesionario: {self.concesionario}
Disponible: {self.disponibilidad}"""
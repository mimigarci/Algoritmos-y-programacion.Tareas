from Vehicle import Vehicle

#Clase hija: Boat

class Boat(Vehicle):

    def __init__(self, nombre, fabricante, año_lanzamiento, cant_velas):

        Vehicle.__init__(self, nombre, fabricante, año_lanzamiento)
        self.cant_velas = cant_velas

    def __str__(self):
        return f"""
        Nombre: {self.nombre} 
        Fabricante: {self.fabricante} 
        Año de lanzamiento: {self.año_lanzamiento}
        Cantidad de velas: {self.cant_velas}
"""






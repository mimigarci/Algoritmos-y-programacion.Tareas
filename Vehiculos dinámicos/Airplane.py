from Vehicle import Vehicle

#Clase hija: Airplane

class Airplane(Vehicle):

    def __init__(self, nombre, fabricante, año_lanzamiento, cant_alas):

        Vehicle.__init__(self, nombre, fabricante, año_lanzamiento)
        self.cant_alas = cant_alas

    def __str__(self):
        return f"""
        Nombre: {self.nombre} 
        Fabricante: {self.fabricante} 
        Año de lanzamiento: {self.año_lanzamiento}
        Cantidad de alas: {self.cant_alas}
"""


from Vehicle import Vehicle

#Clase hija: Airplane

class Airplane(Vehicle):

    def __init__(self, nombre, fabricante, año_lanzamiento, seller, cant_alas):

        Vehicle.__init__(self, nombre, fabricante, año_lanzamiento, seller)
        self.cant_alas = cant_alas

    def show(self):
        return f"""
        Nombre: {self.nombre} 
        Fabricante: {self.fabricante} 
        Año de lanzamiento: {self.año_lanzamiento}
        Vendedor: {self.seller}
        Cantidad de alas: {self.cant_alas}
"""


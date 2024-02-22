from Vehicle import Vehicle

#Clase hija: Car

class Car(Vehicle):

    def __init__(self, nombre, fabricante, año_lanzamiento, seller, cant_ruedas):

        Vehicle.__init__(self, nombre, fabricante, año_lanzamiento, seller)
        self.cant_ruedas = cant_ruedas
         
    def __str__(self):
        return f"""
        Nombre: {self.nombre} 
        Fabricante: {self.fabricante} 
        Año de lanzamiento: {self.año_lanzamiento}
        Vendedor: {self.seller}
        Cantidad de ruedas: {self.cant_ruedas}
"""






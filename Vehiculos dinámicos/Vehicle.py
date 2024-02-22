from Seller import Seller

#Clase padre: Vehículo.

class Vehicle:

    def __init__(self, nombre:str, fabricante:str, año_lanzamiento:int,  seller):
        
        self.nombre = nombre
        self.fabricante = fabricante
        self.año_lanzamiento = año_lanzamiento
        self.seller = seller

    def show(self):
        return f"""
        Nombre: {self.nombre} 
        Fabricante: {self.fabricante} 
        Año de lanzamiento: {self.año_lanzamiento}
        Vendedor: {self.seller.concesionario}
        Disponibile: {self.seller.disponibilidad}
"""
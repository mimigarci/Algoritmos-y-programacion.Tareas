#17/02/2024
#Tipos de Vehiculo con herencia
#Autor: Michelle García


#Limpiar la terminal.
import os
os.system('cls')


#Clase padre: Vehículo.

class Vehicle:

    def __init__(self, nombre, fabricante, año_lanzamiento):
        
        self.nombre = nombre
        self.fabricante = fabricante
        self.año_lanzamiento = año_lanzamiento

                

#Clases hijas: Carro, Bote, Avión


class Car(Vehicle):

    def __init__(self, nombre, fabricante, año_lanzamiento, cant_ruedas):

        Vehicle.__init__(self, nombre, fabricante, año_lanzamiento)
        self.cant_ruedas = cant_ruedas
         
    def __str__(self):
        return f"""
        Nombre: {self.nombre} 
        Fabricante: {self.fabricante} 
        Año de lanzamiento: {self.año_lanzamiento}
        Cantidad de ruedas: {self.cant_ruedas}
"""



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



#Ejemplos de tipos de vehículos.
        
Model_3 = Car("Model 3", "Tesla", 2023, 4)
Model_S = Car("Model S", "Tesla", 2012, 4)

Boeing_Stearman_Model75 = Airplane("Boeing-Stearman", "Stearman Aircraft/Boeing", 1934, 2)
Grumman_F9F_Panther = Airplane("Grumman F9F Panther", "Grumman", 1947, 2)

Titanic = Boat("Titanic", "Harland and Wolff", 1912, 0)
HMS_Victory = Boat("HMS Victory", "Chatham Dockyard", 1765, 4)


#Llamando las funciones

print (f"""
       
{Car.__str__(Model_3)}
{Car.__str__(Model_S)}

{Boat.__str__(Titanic)}
{Boat.__str__(HMS_Victory)}

{Airplane.__str__(Boeing_Stearman_Model75)}
{Airplane.__str__(Grumman_F9F_Panther)}

""")
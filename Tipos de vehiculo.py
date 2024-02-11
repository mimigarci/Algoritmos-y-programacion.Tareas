#11/02/2024
#Tipos de Vehiculo
#Autor: Michelle García


import os
os.system('cls')

#Tipos de vehículos con sus respectivos atributos.

class Car:

    def __init__(self, nombre, marca, año_lanzamiento):
        
        self.nombre = nombre
        self.marca = marca
        self.año_lanzamiento = año_lanzamiento



class Boat:

    def __init__(self, nombre, fabricante, año_lanzamiento):
        
        self.nombre = nombre
        self.fabricante = fabricante
        self.año_lanzamiento = año_lanzamiento



class Airplane:

    def __init__(self, nombre, fabricante, año_lanzamiento):
        
        self.nombre = nombre
        self.fabricante = fabricante
        self.año_lanzamiento = año_lanzamiento



#Ejemplos de tipos de vehículos.
        
Model_3 = Car("Model 3", "Tesla", 2023)
Model_S = Car("Model S", "Tesla", 2012)

Boeing_Stearman_Model75 = Airplane("Boeing-Stearman", "Stearman Aircraft/Boeing", 1934)
Grumman_F9F_Panther = Airplane("Grumman F9F Panther", "Grumman", 1947)

Titanic = Boat("Titanic", "Harland and Wolff", 1912)
HMS_Victory = Boat("HMS Victory", "Chatham Dockyard", 1765)



#Objetos junto a sus atributos respectivos.

print (f"""
{Model_3.nombre}
{Model_3.marca}
{Model_3.año_lanzamiento}

{Model_S.nombre}
{Model_S.marca}
{Model_S.año_lanzamiento}

{Boeing_Stearman_Model75.nombre}
{Boeing_Stearman_Model75.fabricante}
{Boeing_Stearman_Model75.año_lanzamiento}

{Grumman_F9F_Panther.nombre}
{Grumman_F9F_Panther.fabricante}
{Grumman_F9F_Panther.año_lanzamiento}

{Titanic.nombre}
{Titanic.fabricante}
{Titanic.año_lanzamiento}

{HMS_Victory.nombre}
{HMS_Victory.fabricante}
{HMS_Victory.año_lanzamiento}

""")
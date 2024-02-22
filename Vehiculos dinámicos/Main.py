#17/02/2024
#Tipos de Vehiculo con herencia
#Autor: Michelle García
 

#Limpiar la terminal.
import os
os.system('cls')

#Importar clases

from Airplane import Airplane
from Boat import Boat
from Car import Car
from Program import Program


#Ejemplos de tipos de vehículos.

Model_3 = Car("Model 3", "Tesla", 2023, any, 4)
Model_S = Car("Model S", "Tesla", 2012, any, 4)

Boeing_Stearman_Model75 = Airplane("Boeing-Stearman", "Stearman Aircraft/Boeing", 1934, any, 2)
Grumman_F9F_Panther = Airplane("Grumman F9F Panther", "Grumman", 1947, any, 2)

Titanic = Boat("Titanic", "Harland and Wolff", 1912, any, 0)
HMS_Victory = Boat("HMS Victory", "Chatham Dockyard", 1765, any, 4)


vehiculos = [Model_3, Model_S, Boeing_Stearman_Model75, Grumman_F9F_Panther, Titanic, HMS_Victory]


def main (vehiculos):

    programa = Program()
    programa.vehiculos_existentes(vehiculos)
    programa.menu()

main(vehiculos)
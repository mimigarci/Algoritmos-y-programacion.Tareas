from Seller import Seller
from Vehicle import Vehicle

#Programa

class Program:

    def __init__(self):
        #vehicle_status = (sold, concesionario)
        self.Vehicles = []
        self.disponibles = []


    def vehiculos_existentes(self, vehiculos_list):
        self.vehiculos_list = vehiculos_list
        
        for i in vehiculos_list:
            self.Vehicles.append(i)


    def set_seller(self, nombre_vehiculo):
        self.nombre_vehiculo = nombre_vehiculo

        vender_vehiculos = input ("Nombre del concesionario que venderá el vehículo: ")
        
        p = 0
        for j in self.Vehicles:
            if j.nombre == nombre_vehiculo:

                disponible = True
                vendedor = Seller(vender_vehiculos, disponible)
            
                j.seller = vendedor
                self.disponibles.append(j)

                print (Vehicle.show(j))
                print ("Se ha registrado el vendedor")

                p += 1
            else:
                p += 0
                continue

        if p == 0:
            print ("\nEl vehículo no se encuentra registrado. Ingrese un nombre válido")
        else:
            pass

                
                


    def sell_vehicle (self, nombre_vehiculo):
        self.nombre_vehiculo = nombre_vehiculo

        if len(self.disponibles) > 0:

            for z in self.disponibles:
                if z.nombre == nombre_vehiculo:
                    z.seller.disponibilidad = False
                    print ("El vehículo se ha vendido")
                    self.disponibles.remove(z)
                    
                else:
                    continue
                
        else:
            print ("No se encuentra ningún vehículo disponible\n")


    def vehiculos_disp (self):

        for m in self.Vehicles:

            if m.seller == True:
                self.disponibles.append(m)
            else:
                continue

        if len(self.disponibles) > 0:
            print ("Cantidad de vehiculos disponibles: ", len(self.disponibles))
            for h in self.disponibles:
                print (Vehicle.show(h))
        else:
            print ("No hay vehiculos disponibles\n")
            

    def menu (self):
        while True:

            choice = input("""
Seleccione una opción:

1. Definir el vendedor de un vehículo
2. Ver vehículos disponibles
3. Vender vehículo
4. Salir
                          
        ---> """)
            
            if choice == "1":
                #Funcion para definir el seller de cada vehículo

                nombre_vehiculo = input ("¿Qué vehículo desea vender? ")
                Program.set_seller(self, nombre_vehiculo)
                
            elif choice == "2":
                #Funcion para imprimir los vehículos disponibles

                Program.vehiculos_disp(self)

            elif choice == "3":

                #Funcion para cambiar el valor de disponibilidad dentro de un vehículo
                nombre_vehiculo = input ("¿Qué vehículo desea vender? ")
                Program.sell_vehicle(self, nombre_vehiculo)

            elif choice == "4":
                break
            else:
                print ("Esa opción no se encuentra dentro del menu\n")

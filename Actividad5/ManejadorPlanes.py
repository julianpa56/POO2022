import csv
import os

from PlanAhorro import PlanAhorro

class ManejadorPlanes:

    __listaPlanes=[]

    def menuPrincipal(self):
        op=int(input("1- Cargar archivo \n2- Menu secundario \n OTRA TECLA PARA SALIR -- \nOPCION: "))
        while op==1 or op==2:
            if op==1:
                self.cargarPlanes()
            else:
                self.menuSecundario()
            op=int(input("1- Cargar archivo \n2- Menu secundario \n OTRA TECLA PARA SALIR -- \nOPCION: "))

        # 1
    def cargarPlanes(self):
        archivo= open('planes.csv')
        reader= csv.reader(archivo,delimiter=';')
        for plan in reader:
            nuevoPlan= PlanAhorro(plan[0],plan[1],plan[2],plan[3],plan[4],plan[5])
            print(nuevoPlan)
            self.__listaPlanes.append(nuevoPlan)
        os.system("Pause")
        os.system("cls")
        # 2
    def menuSecundario(self):
        opciones={'1':self.actualizarValores ,'2':self.mostrarSegunValor ,'3':self.montoLicitacion ,'4':self.modificarCantidadCuotas }
        opc=int(input("1- Actualizar valor de vehiculos \n2- Mostrar planes segun valor de cuota \n3- Lista de montos para licitar \n 4- Modificar cantidad de cuotas necesarias \n5- SALIR \n--OPCION: "))
        while opc!=5:
            if opc<5 and opc>0:
                func=opciones.get(str(opc))
                func()
            else: 
                print("OPCION INCORRECTA -------")
            opc=int(input("1- Actualizar valor de vehiculos \n2- Mostrar planes segun valor de cuota \n3- Lista de montos para licitar \n4- Modificar cantidad de cuotas necesarias \n5- SALIR \n--OPCION: "))

        # 2.a
    def actualizarValores(self):
        print("--- ACTUALIZACION DE LOS PRECIOS DE VEHICULOS ---")
        for plan in self.__listaPlanes:
            print("\nPlan: {}".format(plan))
            nuevoValor=int(input("\nIngrese nuevo valor: "))
            plan.setValorVehiculo(nuevoValor)
        os.system("Pause")
        os.system("cls")
        # 2.b
    def mostrarSegunValor(self):
        print("\n--- Buscar planes con cuotas menores a la ingresada ---")
        valor=(int(input("INGRESE VALOR: ")))
        b=0
        for plan in self.__listaPlanes:
            aux=plan.calcularCuota()
            aux=float(aux)
            if aux<valor:
                b=1
                info= plan.getDatosPlan()
                print("\nCODIGO PLAN: {} - MODELO: {} - VERSION: {}".format(info[0],info[1],info[2]))
        if b==0:
            print("No hay ningun plan con cuotas menores al valor ingresado")
        os.system("Pause")
        os.system("cls")
        # 2.c
    def montoLicitacion(self):
        print("\n--- Monto necesario para licitar cada vehiculo ---")
        for plan in self.__listaPlanes:
            print("\n-----------------------------")
            print(plan)
            cuota= int(plan.calcularCuota())
            cuotasNecesarias= int(PlanAhorro.cuotasNecesarias)
            monto= cuota * cuotasNecesarias
            print("Monto para licitar: {}".format(monto))
            print("\n-----------------------------")
        os.system("Pause")
        os.system("cls")
        # 2.d
    def modificarCantidadCuotas(self):
        id=int(input("-- INGRESE CODIGO DEL PLAN: "))
        b= True
        i=0
        while (i<(len(self.__listaPlanes)) and b):
            if self.__listaPlanes[i].getCodigo()==id:
                b=False
            else:
                i+=1
        
        if b:
            print("\n-- NO SE ENCONTRO EL CODIGO INGRESADO")
        else :
            aux=int(input("-- Ingrese nueva cantidad de cuotas necesarias: "))
            PlanAhorro.setCuotasNecesarias(aux)
        os.system("Pause")
        os.system("cls")


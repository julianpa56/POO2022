
import csv
from distutils.log import error
import os

from ViajeroFrecuente import ViajeroFrecuente

class ManejadorViajerosFrecuentes:
    
    def menu(self,listaViajeros:list[ViajeroFrecuente]):
        op= int(input("MENU PRINCIPAL -------------- \n 1 - Cargar Archivo\n 2 - Consultar sobre un viajero \n 3 - Salir \n OPCION: "))
        while (op!=3):
            if op==1:
                self.cargarArchivo(listaViajeros)
            elif op==2:
                self.opcionesViajero(listaViajeros)
            else:
                op=3
            op= int(input("MENU PRINCIPAL -------------- \n 1 - Cargar Archivo\n 2 - Consultar sobre un viajero \n 3 - Salir \n---NUEVA OPCION PRINCIPAL: "))

    def cargarArchivo(self,listaViajeros:list):
        listaViajeros=[]
        archivo = open('ArchivoViajeros.csv')
        reader = csv.reader(archivo,delimiter=',')
        for viajero in reader:
            nuevoViajero= ViajeroFrecuente(viajero[0],viajero[1],viajero[2],viajero[3],viajero[4])
            listaViajeros.append(nuevoViajero)
            # print(listaViajeros[0].getNumViajero())
        print("\n-----Archivo cargado------\n")
        os.system("Pause")
        os.system("cls")

    def opcionesViajero(self,listaViajeros):
        print(listaViajeros[0].getNumViajero())
        idViajero= int(input("Ingrese numero de viajero a buscar: "))
        respuesta=int(self.buscarViajero(listaViajeros,idViajero))
        if(respuesta==-1):
            print("Viajero no encontrado")
        else:
            opciones= {'1': listaViajeros[respuesta].cantidadTotalMillas() , '2': listaViajeros[respuesta].acumularMillas(millas) , '3' : listaViajeros[respuesta].canjearMillas(millas) }
            op=int(input("\n 1 - Consultar cantidad de millas \n 2 - Acumular millas \n 3 - Canjear millas \n 4 - Salir \n OPCION: "))
            
            while (op != 4):
                if op==1:
                    res=opciones.get(op,error)
                    print("\nCantidad de millas acumuladas: "+ res)
                elif op==2:
                    millas= int("\nIngrese millas a acumular: ")
                    res=opciones.get(op,error)
                    print("\nNueva cantidad de millas acumuladas: "+ res)
                elif op==3:
                    millas= int("\nIngrese millas a canjear: ")
                    res=opciones.get(op,error)
                    if res != None:
                        print("\nMillas restantes: "+ res)
                op=int(input("\n 1 - Consultar cantidad de millas \n 2 - Acumular millas \n 3 - Canjear millas \n 4 - Salir \n----- INGRESE NUEVA OPCION: "))
        os.system("Pause")
        os.system("cls")
            
    def buscarViajero(self,listaViajeros,auxId:int):
        i=0
        b= True
        while (i<len(listaViajeros)and(b==True)):
            print(listaViajeros[2])
            aux=listaViajeros[i].getNumViajero
            print("Valor de aux: ",aux)
            if(aux == auxId):
                print(listaViajeros[i])
                b=False
            else:
                i+=1
        if(b==False):
            return i
        else:
            return -1



        
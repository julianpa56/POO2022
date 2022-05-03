
import csv
import os

from ViajeroFrecuente import ViajeroFrecuente


class ManejadorViajerosFrecuentes:

    __listaViajeros: list[ViajeroFrecuente]
    
    def menu(self):
        op= int(input("MENU PRINCIPAL -------------- \n 1 - Cargar Archivo\n 2 - Consultar sobre un viajero \n 3 - Determinar mayor cantidad de millas\n 4- Salir \n OPCION: "))
        while (op!=4):
            if op==1:
                self.cargarArchivo()
            elif op==2:
                self.opcionesViajero()
            elif op==3:
                self.mayorCantidadMillas()
            else:
                op=4
            op= int(input("MENU PRINCIPAL -------------- \n 1 - Cargar Archivo\n 2 - Consultar sobre un viajero \n 3 - Determinar mayor cantidad de millas\n 4- Salir \n---NUEVA OPCION PRINCIPAL: "))

    def cargarArchivo(self):
        self.__listaViajeros=[]
        archivo = open('ArchivoViajeros.csv')
        reader = csv.reader(archivo,delimiter=',')
        for viajero in reader:
            nuevoViajero= ViajeroFrecuente(viajero[0],viajero[1],viajero[2],viajero[3],viajero[4])
            self.__listaViajeros.append(nuevoViajero)
            print(nuevoViajero)
        print("\n-----Archivo cargado------\n")
        os.system("Pause")
        os.system("cls")

    def opcionesViajero(self):
        print(self.__listaViajeros[0].getNumViajero())
        idViajero= int(input("Ingrese numero de viajero a buscar: "))
        respuesta=int(self.buscarViajero(idViajero))
        if(respuesta==-1):
            print("Viajero no encontrado")
        else:
            opciones= {'1': self.__listaViajeros[respuesta].cantidadTotalMillas , '2': self.__listaViajeros[respuesta].acumularMillas , '3' : self.__listaViajeros[respuesta].canjearMillas }
            op=int(input("\n 1 - Consultar cantidad de millas \n 2 - Acumular millas \n 3 - Canjear millas \n 4 - Salir \n OPCION: "))
            
            while (op != 5):
                if op==1:
                    print("\nCantidad de millas acumuladas: ", self.__listaViajeros[respuesta].cantidadTotalMillas())
                elif op==2:
                    millas= int(input("\nIngrese millas a acumular: "))
                    self.__listaViajeros[respuesta]= millas + self.__listaViajeros[respuesta]
                    print("\nNueva cantidad de millas acumuladas: ", self.__listaViajeros[respuesta].cantidadTotalMillas())
                elif op==3:
                    millas= int(input("\nIngrese millas a canjear: "))
                    self.__listaViajeros[respuesta]= millas - self.__listaViajeros[respuesta]
                    print("\nMillas restantes: ", self.__listaViajeros[respuesta].cantidadTotalMillas())
                op=int(input("\n 1 - Consultar cantidad de millas \n 2 - Acumular millas \n 3 - Canjear millas \n 4 - Salir \n----- INGRESE NUEVA OPCION: "))
        os.system("Pause")
        os.system("cls")
            
    def buscarViajero(self,auxId):
        i=0
        b= True
        while ((i<len(self.__listaViajeros)) and (b==True)):
            aux=self.__listaViajeros[i].getNumViajero()
            print("Valor de aux: ",aux)
            print("Valor de auxId: ",auxId)
            auxId= int(auxId)
            aux= int(aux)
            if aux == auxId :
                b=False
            else:
                i+=1
        if(b==False):
            return i
        else:
            return -1

    def mayorCantidadMillas(self):
        i=0
        listaMaximos=[]
        mayorCantidad=0
        while i+1 < len(self.__listaViajeros):
            if (self.__listaViajeros[i]>self.__listaViajeros[i+1]):
                mayorCantidad= self.__listaViajeros[i].cantidadTotalMillas()
            elif (self.__listaViajeros[i+1]>self.__listaViajeros[i]):
                mayorCantidad= self.__listaViajeros[i+1].cantidadTotalMillas()
            i=i+1
        print("\nCantidad de millas maximas acumuladas: ",mayorCantidad)
        for viajero in self.__listaViajeros:
            if (viajero == mayorCantidad):
                listaMaximos.append(viajero)
        print("-- LISTA DE VIAJEROS QUE TIENEN LA MAYOR CANTIDAD DE MILLAS ACUMULADAS --")
        for viajero in listaMaximos:
            print(viajero)
        os.system("Pause")
        os.system("cls")
        
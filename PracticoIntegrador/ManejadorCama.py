import csv
import numpy as np

from Cama import Cama


class ManejadorCama:
    __dimension=0
    __cantidad=0
    __incremento=1
    __arreCamas= None

    def __init__(self,dimension):
        self.__arreCamas= np.empty(dimension,dtype=Cama)

    def leerArchivo(self):
        archivo = open("camas.csv")
        reader= csv.reader(archivo,delimiter=';')
        b=True
        for cama in reader:
            if b==True:
                b=False
            else:
                idCama=int(cama[0])
                nroHabitacion=int(cama[1])
                estado=bool(cama[2])
                nombre=cama[3].split(',')
                diagnostico=cama[4]
                ingreso=cama[5]
                alta=cama[6]
                nuevaCama= Cama(idCama,nroHabitacion,estado,nombre,diagnostico,ingreso,alta)
                self.agregar(nuevaCama)

    def agregar(self,nuevaCama:Cama):
        if self.__dimension == self.__cantidad:
            self.__dimension+= self.__incremento
            self.__arreCamas.resize(self.__dimension)
        self.__arreCamas[self.__cantidad]=nuevaCama
        self.__cantidad+=1

    def buscar(self,apellido,nombre):
        resultado=None
        b=True
        i=0
        idC=0
        aux=[]
        while b and i< self.__cantidad:
            aux= self.__arreCamas[i].getNombre()
            if aux[0]== apellido and aux[1]== nombre:
                b=False
                idC= self.__arreCamas[i].getIdCama()
            else:
                i+=1
        if b== False:
            resultado=idC
            print("Paciente: {:10},{} Cama:{:10} Habitacion: {:10}".format(aux[0],aux[1],idC,self.__arreCamas[idC-1].getHabitacion()))
            print("Diagnostico: {:10} Fecha de internacion: {:10}\nFecha de alta: {:10}".format(self.__arreCamas[idC-1].getDiagnostico(),self.__arreCamas[idC-1].getFechaInternacion(),self.__arreCamas[idC-1].getFechaAlta()))
        return resultado

    def darAlta(self,fecha,indice):
        self.__arreCamas[indice-1].setEstado(False)
        self.__arreCamas[indice-1].setNombre(None)
        self.__arreCamas[indice-1].setFechaAlta(fecha)
        print('La fecha de alta se actualizo con exito!')

    def listarPacientes(self,diag):
        for paciente in self.__arreCamas:
            if paciente.getDiagnostico()==diag and paciente.getEstado()==True:
                print("\nPaciente: {} | Habitacion: {} | Diagnostico: {} | Fecha de Internacion: {}".format(paciente.getNombre(),paciente.getHabitacion(),paciente.getDiagnostico(),paciente.getFechaInternacion()))

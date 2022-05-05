
import os
import sys

from Conjunto import Conjunto

class ManejadorConjunto:

    __conjunto1= Conjunto()
    __conjunto2= Conjunto()

    def menuPrincipal(self):
        op=int(input("--- MENU PRINCIPAL---\n 1 - Cargar conjuntos\n 2- Menu secundario\n -- PARA SALIR OTRA TECLA\n OPCION: "))
        while op==1 or op==2:
            if op==1:
                self.cargarConjuntos()
            else:
                self.menuSecundario()
            op=int(input("--- MENU PRINCIPAL---\n 1 - Cargar conjuntos\n 2- Menu secundario\n -- PARA SALIR OTRA TECLA\n OPCION: "))

    def cargarConjuntos(self):
        sys.stdout.flush()
        print("\n--- Carga del conjunto 1 ---")
        a=[]
        nuevo1=(input("\nIngrese un nuevo elemento o 'a' para terminar: "))
        while (nuevo1!='a'):
            nuevo1=int(nuevo1)
            a.append(nuevo1)
            nuevo1=(input("\nIngrese un nuevo elemento o 'a' para terminar: "))
        self.__conjunto1.agregar(a)
        print(self.__conjunto1.getElementos())

        sys.stdout.flush()
        print("\n\n--- Carga del conjunto 2 ---")
        b=[]
        nuevo2=(input("\nIngrese un nuevo elemento o 'a' para terminar: "))
        while (nuevo2!='a'):
            print(nuevo2)
            nuevo2=int(nuevo2)
            b.append(nuevo2)
            nuevo2=(input("\nIngrese un nuevo elemento o 'a' para terminar: "))
        self.__conjunto2.agregar(b)
        print(self.__conjunto2.getElementos())
        os.system("Pause")
        os.system("cls")

    def menuSecundario(self):
        op={'1':self.sumarConjuntos,'2':self.restarConjuntos,'3':self.compararConjuntos}
        opcion=int(input("1 - Sumar conjuntos\n2 - Restar conjuntos\n3 - Comparar conjuntos\n -- OTRO NUMERO - SALIR\n -- OPCION: "))
        while opcion>0 and opcion<4:
            func=op.get(str(opcion))
            func()
            opcion=int(input("1 - Sumar conjuntos\n2 - Restar conjuntos\n3 - Comparar conjuntos\n -- OTRO NUMERO - SALIR\n -- OPCION: "))

    def sumarConjuntos(self):
        op=int(input("\n1- CONJ 1 + CONJ 2 \n2- CONJ 2 + CONJ 1"))
        if (op==1):
            aux= self.__conjunto1 + self.__conjunto2
            print(aux)
        elif (op==2):
            aux= self.__conjunto2 + self.__conjunto1
            print(aux)
        os.system("Pause")
        os.system("cls")

    def restarConjuntos(self):
        op=int(input("\n1- CONJ 1 - CONJ 2 \n2- CONJ 2 - CONJ 1"))
        if (op==1):
            aux= self.__conjunto1 - self.__conjunto2
            print(aux)
        elif (op==2):
            aux= self.__conjunto2 - self.__conjunto1
            print(aux)
        os.system("Pause")
        os.system("cls")

    def compararConjuntos(self):
        if(self.__conjunto1==self.__conjunto2):
            print("Ambos conjuntos son iguales")
        else:
            print("Los conjuntos son diferentes")
        os.system("Pause")
        os.system("cls")
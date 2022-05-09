

class Medicamento:
    __idCama=0
    __idMedicamento=0
    __nombreComercial=''
    __monodroga=''
    __presentacion=''
    __cantidadAplicada=0
    __precioTotal=0

    def __init__(self,idC,idM,nom,mon,pre,cantA,pres):
        self.__idCama=idC
        self.__idMedicamento=idM
        self.__nombreComercial=nom
        self.__monodroga=mon
        self.__presentacion=pre
        self.__cantidadAplicada=cantA
        self.__precioTotal=pres

    def getIdCama(self):
        return self.__idCama

    def getNombre(self):
        return self.__nombreComercial

    def getMonodroga(self):
        return self.__monodroga

    def getPresentacion(self):
        return self.__presentacion

    def getPrecio(self):
        return self.__precioTotal

    def getCantAplicada(self):
        return self.__cantidadAplicada

    def __str__(self) -> str:
        return ("id Medicamento: {} - Nombre: {}".format(self.__idMedicamento,self.__nombreComercial))
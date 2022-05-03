import os


class ViajeroFrecuente :
    __num_viajero= 0
    __dni= 0
    __nombre= ''
    __apellido= ''
    __millas_acum= 0

    def __init__(self,auxNumViajero,auxDni,auxNom,auxApe,auxMillAcum) -> None:
        self.__num_viajero= int(auxNumViajero)
        self.__dni= int(auxDni)
        self.__nombre= auxNom
        self.__apellido= auxApe
        self.__millas_acum= int(auxMillAcum)

    def cantidadTotalMillas(self) -> int:
        return self.__millas_acum

    def acumularMillas(self,auxNuevasMillas) -> int:
        self.__millas_acum += auxNuevasMillas
        return self.__millas_acum

    def canjearMillas(self,auxMillasACanjear:int):
        if(self.__millas_acum>=auxMillasACanjear):
            self.__millas_acum-=auxMillasACanjear
            return self.__millas_acum
        else:
            print("ERROR EN LA OPERACION!!! El total de millas a canjear es superior al total de millas acumuladas\n")
            return None
    def getNumViajero(self) -> int:
        return self.__num_viajero

    def __str__(self) -> str:
        return ("{}-{}-{}-{}-{}".format(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum))

    def __gt__(self,otroViajero):
        if (self.__millas_acum > otroViajero.cantidadTotalMillas()):
            return True
        else:
            return False

    def __radd__(self,millas:int):
        self.__millas_acum+=millas
        return self

    def __rsub__(self,millas:int):
        if(self.__millas_acum>=millas):
            self.__millas_acum-=millas
            return self
        else:
            print("ERROR EN LA OPERACION!!! El total de millas a canjear es superior al total de millas acumuladas\n")
            os.system("Pause")
            return self

    def __eq__(self,cantidadMillas:int):
        if (self.cantidadTotalMillas()==cantidadMillas):
            return True
        else :
            return False

    def __req__(self,cantidadMillas:int):
        if (self.cantidadTotalMillas()==cantidadMillas):
            return True
        else :
            return False
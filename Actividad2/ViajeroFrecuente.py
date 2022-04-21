

class ViajeroFrecuente :
    __num_viajero: int
    __dni: int
    __nombre: str
    __apellido: str
    __millas_acum: int

    def __init__(self,auxNumViajero: int,auxDni: int,auxNom: str,auxApe: str,auxMillAcum: int) -> None:
        self.__num_viajero= auxNumViajero
        self.__dni= auxDni
        self.__nombre= auxNom
        self.__apellido= auxApe
        self.__millas_acum= auxMillAcum

    def cantidadTotalMillas(self) -> int:
        return self.__millas_acum

    def acumularMillas(self,auxNuevasMillas:int) -> int:
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


class Registro :
    __temperatura=0
    __humedad=0
    __presion_at=0

    def __init__(self,temp,hum,pre) -> None:
        self.__temperatura=int(temp)
        self.__humedad=int(hum)
        self.__presion_at=int(pre)

    def getTemp(self):
        return self.__temperatura

    def getHum(self):
        return self.__humedad

    def getPres(self):
        return self.__presion_at
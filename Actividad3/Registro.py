

class Registro :
    __temperatura=0.0
    __humedad=0.0
    __presion_at=0.0

    def __init__(self,temp,hum,pre):
        self.__temperatura=float(temp)
        self.__humedad=float(hum)
        self.__presion_at=float(pre)

    def getTemp(self):
        return self.__temperatura

    def getHum(self):
        return self.__humedad

    def getPres(self):
        return self.__presion_at
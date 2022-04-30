

class Ventana:
    __titulo=''
    __verticeXSupIzq=0
    __verticeYSupIzq=0
    __verticeXInfDer=500
    __verticeYInfDer=500

    def __init__(self,titulo='defect',xsi=0,ysi=0,xid=500,yid=500):
        if (xsi<xid and ysi<yid):
            self.__titulo= titulo
            self.__verticeXSupIzq=int(xsi)
            self.__verticeYSupIzq=int(ysi)
            self.__verticeXInfDer=int(xid)
            self.__verticeYInfDer=int(yid)
        else:
            print("Las coordenadas son erroneas")

    def mostrar(self):
        return print("Coordenadas superiores: ({},{})\nCoordenadas inferiores: ({},{})".format(self.__verticeXSupIzq,self.__verticeYSupIzq,self.__verticeXInfDer,self.__verticeYInfDer))

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return (self.__verticeYInfDer-self.__verticeYSupIzq)

    def ancho(self):
        return (self.__verticeXInfDer-self.__verticeXSupIzq)

    def moverIzquierda(self,aux):
        self.__verticeXSupIzq+=int(aux)
        self.__verticeXInfDer+=int(aux)

    def moverDerecha(self,aux):
        self.__verticeXSupIzq-=int(aux)
        self.__verticeXInfDer-=int(aux)

    def subir(self,aux=1):
        self.__verticeYSupIzq+=int(aux)
        self.__verticeYInfDer+=int(aux)

    def bajar(self,aux=1):
        self.__verticeYSupIzq-=int(aux)
        self.__verticeYInfDer-=int(aux)
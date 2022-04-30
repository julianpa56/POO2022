

class PlanAhorro:
    __codigoPlan=0
    __modelo=''
    __versionVehiculo=''
    __valorVehiculo=0
    cuotasPlan=60
    cuotasNecesarias=10

    def __init__(self,cod,mod,verV,valV,cp=0,cn=0):
        self.__codigoPlan=int(cod)
        self.__modelo=mod
        self.__versionVehiculo=verV
        self.__valorVehiculo=int(valV)
        if(int(cp)!=0 and int(cn)!=0):
            PlanAhorro.cuotasPlan=int(cp)
            PlanAhorro.cuotasNecesarias=int(cn)

    def __str__(self):
        return ("{}--{}--{}--{}--{}--{}".format(self.__codigoPlan,self.__modelo,self.__versionVehiculo,self.__valorVehiculo,PlanAhorro.cuotasPlan,PlanAhorro.cuotasNecesarias))

    @classmethod
    def getCuotasPlan(cls):
        return cls.cuotasPlan

    @classmethod
    def getCuotasNecesarias(cls):
        return cls.cuotasNecesarias
        
    @classmethod
    def setCuotasNecesarias(cls,aux):
        PlanAhorro.cuotasNecesarias=int(aux)

    def calcularCuota(self):
        a=int(self.__valorVehiculo)/ int(PlanAhorro.getCuotasPlan())
        b=int(self.__valorVehiculo)*0.10
        aux=a+b
        aux=round(aux,2)
        return (aux)

    def setValorVehiculo(self,nuevoValor):
        self.__valorVehiculo= int(nuevoValor)

    def getDatosPlan(self):
        datos=[self.__codigoPlan,self.__modelo,self.__versionVehiculo]
        return datos 
    
    def getCodigo(self):
        return self.__codigoPlan
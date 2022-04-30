

class PlanAhorro:
    __codigoPlan=0
    __modelo=''
    __versionVehiculo=''
    __valorVehiculo=0
    cuotasPlan=60
    cuotasNecesarias=10

    def __init__(self,cod,mod,verV,valV) -> None:
        self.__codigoPlan=int(cod)
        self.__modelo=mod
        self.__versionVehiculo=verV
        self.__valorVehiculo=int(valV)

class Cama:
    __idCama=0
    __habitacion=0
    __estado=True
    __nombrePaciente=[]
    __diagnostico=''
    __fechaInternacion=''
    __fechaAlta=''

    def __init__(self,idC,hab,est,nom,diag,fIng,fAlta):
        self.__idCama=int(idC)
        self.__habitacion=int(hab)
        self.__estado=bool(est)
        self.__nombrePaciente=nom
        self.__diagnostico=diag
        self.__fechaInternacion=fIng
        self.__fechaAlta= fAlta
    
    def getIdCama(self):
        return self.__idCama

    def getHabitacion(self):
        return self.__habitacion
    
    def getEstado(self):
        return self.__estado

    def getNombre(self):
        return self.__nombrePaciente

    def getDiagnostico(self):
        return self.__diagnostico

    def getFechaInternacion(self):
        return self.__fechaInternacion

    def getFechaAlta(self):
        return self.__fechaAlta

    def getHabitacion(self):
        return self.__habitacion

    def setEstado(self,nuevoEstado:bool):
        self.__estado=nuevoEstado

    def setNombre(self,nuevoNombre):
        self.__nombrePaciente=nuevoNombre

    def setFechaAlta(self,fechaAlta):
        self.__fechaAlta= fechaAlta

    def __str__(self) -> str:
        return ("id: {} - nombre: {}".format(self.__idCama,self.__nombrePaciente))

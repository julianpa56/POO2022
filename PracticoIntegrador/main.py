from ManejadorCama import ManejadorCama
from ManejadorMedicamento import ManejadorMedicamento

if __name__=='__main__':
    manejadorCamas= ManejadorCama(3)
    manejadorMedicamentos= ManejadorMedicamento()

    manejadorCamas.leerArchivo()
    manejadorMedicamentos.leerArchivo()

    apellido=input("Ingrese apellido de paciente: ")
    nombre=input("Ingrese nombre de paciente: ")

    idC=manejadorCamas.buscar(apellido,nombre)
    if idC==None:
        print("-- no se encontro a paciente")
    else:
        manejadorMedicamentos.buscarMedicamento(idC)

    diag=input("Ingrese diagnostico a buscar: ")
    manejadorCamas.listarPacientes(diag)
import csv

from Medicamento import Medicamento



class ManejadorMedicamento:
    __listaMedicamentos=[]


    def leerArchivo(self):
        archivo= open('medicamentos.csv')
        reader= csv.reader(archivo,delimiter=';')
        b=True
        for medicamento in reader:
            if b:
                b=False
            else:
                idCama=int(medicamento[0])
                idMedicamento=int(medicamento[1])
                nombreComercial=medicamento[2]
                monodroga=medicamento[3]
                presentacion=medicamento[4]
                cantidadAplicada=int(medicamento[5])
                precioTotal=float(medicamento[6])

                nuevoMedicamento= Medicamento(idCama,idMedicamento,nombreComercial,monodroga,presentacion,cantidadAplicada,precioTotal)
                self.__listaMedicamentos.append(nuevoMedicamento)
                print(nuevoMedicamento)

    def buscarMedicamento(self,idCama):
        print("{:10}{:70}{:50}{:20}".format("Medicamento/monodroga","Presentacion","Cantidad","Precio"))
        total=0.0
        
        for medicamento in self.__listaMedicamentos:
            aux=medicamento.getIdCama()
            aux=int(aux)
            if aux ==idCama:
                total+=medicamento.getPrecio()
                print("{:10}{:70}{:50}{:20}".format((medicamento.getNombre()+'/'+medicamento.getMonodroga()),medicamento.getPresentacion(),medicamento.getCantAplicada(),medicamento.getPrecio()))
        print("Total adeudado: {:40}".format(total))
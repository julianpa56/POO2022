import csv

from Medicamento import Medicamento



class ManejadorMedicamento:
    __listaMedicamentos=[Medicamento]


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

    def buscarMedicamento(self,idCama):
        print("{:10}{:10}{:10}{:10}".format("Medicamento/monodroga","Presentacion","Cantidad","Precio"))
        total=0.0
        
        for medicamento in self.__listaMedicamentos:
            
            if medicamento.getIdCama() ==idCama:
                cantidad=self.__listaMedicamentos.count(medicamento)
                total+=medicamento.getPrecio()*cantidad
                print("{:10}{:10}{:10}{:10}".format((medicamento.getNombre()+'/'+medicamento.getMonodroga()),medicamento.getPresentacion(),cantidad,medicamento.getPrecio()))
            print("Total adeudado: {:40}".format(total))
import csv
import os

from Registro import Registro


class ManejadorRegistro :

    __tabla=[]

    def __init__(self) -> None:
        for i in range(30):
            a=[]
            self.__tabla.append(a)

    def menuPrincipal(self):
        menuP={'1': self.cargaDatos , '2': self.menuSecundario}
        op=(str(input("\n1- CARGAR DATOS \n2- MENU SECUNDARIO \n -- PARA SALIR PRESIONE OTRA TECLA \n---- OPCION: ")))
        while(op=='1' or op=='2'):
            func= menuP.get(op)
            print(func)
            func()
            op=(str(input("\n1- CARGAR DATOS \n2- MENU SECUNDARIO \n -- PARA SALIR PRESIONE OTRA TECLA \n---- OPCION: ")))


    def cargaDatos(self):
        archivo= open("mes.csv",)
        reader= csv.reader(archivo,delimiter=',')
        for reg in reader:
            t=float(reg[2])
            h=float(reg[3])
            p=float(reg[4])
            aux= Registro(t,h,p)
            self.__tabla[int(reg[0])-1].append(aux)
            print(self.__tabla[int(reg[0])-1][int(reg[1])-1])
        
    def menuSecundario(self):
        menuP={'1': self.maxYMin , '2': self.tempPromedio , '3': self.listarDia}
        op=(str(input("\n1- Mostrar para cada variable el día y hora de menor y mayor valor \n2- Indicar la temperatura promedio mensual por cada hora \n3- Indicar la temperatura promedio mensual por cada hora \n -- PARA SALIR PRESIONE OTRA TECLA \n---- OPCION: ")))
        while(op=='1' or op=='2' or op=='3'):
            func= menuP.get(op)
            func()
            op=(str(input("\n1- Mostrar para cada variable el día y hora de menor y mayor valor \n2- Indicar la temperatura promedio mensual por cada hora \n3- Indicar la temperatura promedio mensual por cada hora \n -- PARA SALIR PRESIONE OTRA TECLA \n---- OPCION: ")))

    
    def maxYMin(self):
        auxTempMayor=0.0
        auxTempMenor=100.0
        auxHumMayor=0.0
        auxHumMenor=100.0
        auxPreMayor=0.0
        auxPreMenor=3000.0    
        for dia in range(len(self.__tabla)):
            for hora in range(len(self.__tabla[dia])):
                temp= float(self.__tabla[dia][hora].getTemp())
                hum= float(self.__tabla[dia][hora].getHum())
                pre= float(self.__tabla[dia][hora].getPres())

                if (temp>auxTempMayor):
                    maxTemp=[]
                    maxTemp.append([dia+1,hora+1,temp])
                    auxTempMayor=temp
                elif (temp<auxTempMenor):
                    minTemp=[]
                    minTemp.append([dia+1,hora+1,temp])
                    auxTempMenor=temp

                if (hum>auxHumMayor):
                    maxHum=[]
                    maxHum.append([dia+1,hora+1,hum])
                    auxHumMayor=hum
                elif (hum<auxHumMenor):
                    minHum=[]
                    minHum.append([dia+1,hora+1,hum])
                    auxHumMenor=hum

                if (pre>auxPreMayor):
                    maxPre=[]
                    maxPre.append([dia+1,hora+1,pre])
                    auxPreMayor=pre
                elif (pre<auxPreMenor):
                    minPre=[]
                    minPre.append([dia+1,hora+1,pre])
                    auxPreMenor=pre
                    
        print("\nREGISTROS DE TEMPERATURA -------------------------------------")
        print("\nEl dia {}, hora {} se registro la mayor temperatura que fue de {}°".format(maxTemp[0][0],maxTemp[0][1],maxTemp[0][2]))
        print("\nEl dia {}, hora {} se registro la menor temperatura que fue de {}°".format(minTemp[0][0],minTemp[0][1],minTemp[0][2]))
        print("\n\nREGISTROS DE HUMEDAD -------------------------------------")
        print("\nEl dia {}, hora {} se registro la mayor humedad que fue de {}°".format(maxHum[0][0],maxHum[0][1],maxHum[0][2]))
        print("\nEl dia {}, hora {} se registro la menor humedad que fue de {}°".format(minHum[0][0],minHum[0][1],minHum[0][2]))
        print("\n\nREGISTROS DE PRESION ATMOSFERICA -------------------------------------")
        print("\nEl dia {}, hora {} se registro la mayor presion atmosferica que fue de {}°".format(maxPre[0][0],maxPre[0][1],maxPre[0][2]))
        print("\nEl dia {}, hora {} se registro la menor presion atmosferica que fue de {}°".format(minPre[0][0],minPre[0][1],minPre[0][2]))
        os.system("Pause")
        os.system("cls")

    def tempPromedio(self):
        arrePromedios=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        for i in range(len(arrePromedios)):
            for j in range(len(self.__tabla)):
                reg=self.__tabla[j][i]
                arrePromedios[i]+= float(reg.getTemp())
        i=0
        for i in range(24):
            arrePromedios[i]/=30
            print("\nLa temperatura promedio mensual a las {}hs fue de {}°".format(i,round(arrePromedios[i],2)))
    
    def listarDia(self):
        dia=int(input("\nIngrese dia a listar: "))
        print("\n{:^10}{:^10}{:^10}{:^10}\n\n".format('Hora','Temperatura','Humedad','Presion'))
        for j in range(24):
            print("{:^10}{:^10}{:^10}{:^10}".format(j+1,self.__tabla[dia-1][j].getTemp(),self.__tabla[dia-1][j].getHum(),self.__tabla[dia-1][j].getPres()))

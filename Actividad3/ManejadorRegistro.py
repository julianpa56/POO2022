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
            # print()
            aux= Registro(t,h,p)
            self.__tabla[int(reg[0])-1].append(aux)
        
    def menuSecundario(self):
        menuP={'1': self.maxYMin , '2': self.tempPromedio , '3': self.listarDia}
        op=(str(input("\n1- Mostrar para cada variable el día y hora de menor y mayor valor \n2- Indicar la temperatura promedio mensual por cada hora \n3- Indicar la temperatura promedio mensual por cada hora \n -- PARA SALIR PRESIONE OTRA TECLA \n---- OPCION: ")))
        while(op=='1' or op=='2' or op=='3'):
            func= menuP.get(op)
            func()
            op=(str(input("\n1- Mostrar para cada variable el día y hora de menor y mayor valor \n2- Indicar la temperatura promedio mensual por cada hora \n3- Indicar la temperatura promedio mensual por cada hora \n -- PARA SALIR PRESIONE OTRA TECLA \n---- OPCION: ")))

    
    def maxYMin(self):
        auxTempMayor=0
        auxTempMenor=100
        auxHumMayor=0
        auxHumMenor=100
        auxPreMayor=0
        auxPreMenor=100      
        for dia in range(30):
            for hora in range(24):
                temp= self.__tabla[dia][hora].getTemp()
                hum= self.__tabla[dia][hora].getHum()
                pre= self.__tabla[dia][hora].getPres()

                if (temp>auxTempMayor):
                    maxTemp=[dia,hora,temp]
                    auxTempMayor=temp
                elif (temp<auxTempMenor):
                    minTemp=[dia,hora,temp]
                    auxTempMenor=temp

                if (hum>auxHumMayor):
                    maxHum=[dia,hora,hum]
                    auxHumMayor=hum
                elif (hum<auxHumMenor):
                    minHum=[dia,hora,hum]
                    auxTempMenor=pre

                if (pre>auxPreMayor):
                    maxPre=[dia,hora,pre]
                    auxPreMayor=hum
                elif (pre<auxPreMenor):
                    minPre=[dia,hora,pre]
                    auxPreMenor=pre
                    
        print("\nREGISTROS DE TEMPERATURA -------------------------------------")
        print("\nEl dia {}, hora {} se registro la mayor temperatura que fue de {}°".format(maxTemp[0],maxTemp[1],maxTemp[2]))
        print("\nEl dia {}, hora {} se registro la menor temperatura que fue de {}°".format(minTemp[0],minTemp[1],minTemp[2]))
        print("\n\nREGISTROS DE HUMEDAD -------------------------------------")
        print("\nEl dia {}, hora {} se registro la mayor humedad que fue de {}°".format(maxHum[0],maxHum[1],maxHum[2]))
        print("\nEl dia {}, hora {} se registro la menor humedad que fue de {}°".format(minHum[0],minHum[1],minHum[2]))
        print("\n\nREGISTROS DE PRESION ATMOSFERICA -------------------------------------")
        print("\nEl dia {}, hora {} se registro la mayor presion atmosferica que fue de {}°".format(maxPre[0],maxPre[1],maxPre[2]))
        print("\nEl dia {}, hora {} se registro la menor presion atmosferica que fue de {}°".format(minPre[0],minPre[1],minPre[2]))
        os.system("Pause")
        os.sysyem("cls")

    def tempPromedio(self):
        arrePromedios= list[24]
        for i in range(24):
            for j in range(30):
                arrePromedios[i]+= self.__tabla[j][i].getTemperatura()
        i=0
        for i in range(24):
            arrePromedios[i]/=30
            print("\nLa temperatura promedio mensual a las {}hs fue de {}°".format(i,round(arrePromedios[i],2)))
    
    def listarDia(self,dia):
        print("\n{:^10}{:^10}{:^10}{:^10}\n\n".format('Hora','Temperatura','Humedad','Presion'))
        for j in range(24):
            print("{:^10}{:^10}{:^10}{:^10}".format(j,self.__tabla[dia-1][j].getTemp(),self.__tabla[dia-1][j].getHum(),self.__tabla[dia-1][j].getPres()))

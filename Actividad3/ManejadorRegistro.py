import csv

from Registro import Registro


class ManejadorRegistro :

    __tabla: Registro = [30][24]

    def menuPrincipal(self):
        pass

    def cargaDatos(self):
        archivo= open("Archivo.csv")
        reader= csv.reader(archivo)
        for reg in reader:
            self.__tabla[reg[0]][reg[1]]= Registro(reg[2],reg[3],reg[4])
        
    def menuSecundario(self):
        pass
    
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

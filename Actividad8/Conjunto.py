

from numpy import conj


class Conjunto :
    __conjunto = []

    def agregar(self,nuevosElementos):
        self.__conjunto=nuevosElementos

    def __add__(self,otroConjunto):
        nuevoConjunto=[]
        conjA=self.__conjunto
        conjA.sort()
        conjB= otroConjunto.getElementos()
        conjB.sort()
        longitudA= len(conjA)
        longitudB= len(conjB)
        i=0
        j=0
        while (i<longitudA and j<longitudB):
            if conjA[i]<conjB[j]:
                nuevoConjunto.append(conjA[i])
                i+=1
            elif conjA[i]>conjB[j]:
                nuevoConjunto.append(conjB[j])
                j+=1
            else:
                nuevoConjunto.append(conjA[i])
                i+=1
                j+=1
                
        if i<longitudA: 
            while i<longitudA:
                nuevoConjunto.append(conjA[i])
                i+=1
        elif j<longitudB:
            while j<longitudB:
                nuevoConjunto.append(conjB[j])
                j+=1
        
        return nuevoConjunto

    def __sub__(self,otroConjunto):
        nuevoConjunto=[]
        conjA=self.__conjunto
        conjB=otroConjunto.getElementos()
        c=0
        for a in conjA:
            for b in conjB:
                if a == b:
                    c=1
            if c==0:
                print(a)
                nuevoConjunto.append(a)
            c=0
        return nuevoConjunto

    def __eq__(self,otroConjunto):
        conjA=self.__conjunto
        conjB=otroConjunto.getElementos()
        if (len(conjA)!= len(conjB)):
            return False
        else:
            conjA.sort(reverse=False)
            conjB.sort(reverse=False)
            i=0
            c=True
            while (i<len(conjA) and c):
                if( conjA[i] != conjB[i] ):
                    c=False
                else:
                    i+=1
            return c

    def getElementos(self):
        return self.__conjunto


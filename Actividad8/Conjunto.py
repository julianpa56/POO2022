

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
        b=False
        for a in conjA:
            print(a)
            for b in conjB:
                if a == b:
                    b=True
            if b==False:
                nuevoConjunto.append(a)
            b=False
        return nuevoConjunto

    def __eq__(self,otroConjunto):
        if (len(self.__conjunto.getElementos())!= len(otroConjunto.getElementos())):
            return False
        else:
            a=self.__conjunto
            a.sort(reverse=False)
            b=otroConjunto
            b.sort(reverse=False)
            i=0
            c=True
            while (i<len(a) and c):
                if(a[i]!=b[i]):
                    c=False
                else:
                    i+=1
            return b

    def getElementos(self):
        return self.__conjunto


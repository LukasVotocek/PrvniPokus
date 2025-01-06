#ukol: funkce pro odmocninu
"""cache={}

def odmocnina(n):
    if cache.get(n) is not None:
        print("cache hit")
        return cache.get(n)

    
    if n<0:
        raise Exception("zaporny")
    o=n**(1/2)
    cache[n]=o
    return o

n=int(input("zadej cislo: "))
odmocnina(n)
odmocnina(n)
"""

#spojovaci seznam 
"""
class PrvekSeznamu:
    def __init__(self, cislo, dalsi):
        self.cislo=cislo
        self.dalsi=dalsi


class SpojovySeznam:
    def __init__ (self):
        self._hlava=None

    def is_empty(self):
        return self._hlava is None

    def prepend(self,nove_cislo):
        stary_prvni_prvek=self._hlava
        self._hlava=PrvekSeznamu(nove_cislo,stary_prvni_prvek)

    def get(self,idx):
        if self.is_empty():
            raise Exception("prazdny seznam")
        acc=0
        aktualni=self._hlava
        while acc<idx:
            aktualni=aktualni.dalsi
            acc+=1
        return aktualni
    

    def pop_last(self):
    """


    
    
 

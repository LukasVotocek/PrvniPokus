# telefonni seznam
"""
clovek;
- jmeno
-tel cislo


telseznam;
-kontejner pro clovek 
-operace:
    -najdi_cislo_podle_prefix(prefix)->list(clovek)
    -najdi_clovek_podle_cisla(cislo) ->clovek
"""

"""from dataclasses import dataclass
from sys import prefix


@dataclass
class Clovek:
    jmeno: str
    cislo: int


#class Clovek:
#    def __init__(self,jmeno,cislo):
#       self.jmeno=jmeno
#        self.cislo=cislo

class TelSeznam:
    def __init__(self):
        self.kontejner=[]
        self.mapa={}
        
    def pridej_cloveka(self):
        self.kontejner.append(Clovek)
        self.mapa[Clovek.cislo]=Clovek.jmeno


    def najdi_cislo_podle_prefix(self):
        seznam=[]
        for osoba in self.kontejner:
            if osoba.jmeno[0:len(prefix)]==prefix:
                seznam.append(osoba)
        return seznam

    def najdi_cloveka_podle_cisla(self,cislo):
        return self.mapa.get(cislo)

"""



#nemocnice
"""
nemocnice:
    -kontejner: ma ordinace (pavilony)
ordinace:
    -specializace
    -hlavniho lekare
    -pomocneho lekare
    -pacienty,kteri do ordinace dochazeji
pacient:
    -rodne cislo
    -jmeno
    -pohlavi: zena, ne zena (bool)
    -typ pacienta:hypochondr,normal,rambo
lekar:
    -jmeno
    -specializace 
"""

from dataclasses import dataclass
from enum import Enum

@dataclass
class Pacient:
    rodne_cislo:int
    jmeno:str
    pohlavi:bool
    typ:str
    
class Specializace(Enum):
    KARDIOLOG = 0
    NEUROLOG = 1
    NEFROLOG = 2

class Lekar:
    jmeno:str
    specializace: Specializace



class Nemocnice:
    def __init__(self):
        self.seznam=[]

    def pridej(self):
        self.seznam.append(Ordinace)


class Ordinace:
    def __init__(self, specializace: str, hlavni_lekar: Lekar):
        self.specializace = specializace
        self.hlavni_lekar = hlavni_lekar
        self.pacienti = []

    def pridej_pacienta(self, pacient: Pacient):
        self.pacienti.append(pacient)

lekar1 = Lekar("Karel Vins", Specializace.KARDIOLOG)
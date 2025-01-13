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

lekar1 = Lekar("Karel Vins", Specializace.KARDIOLOG)"""




from enum import Enum
from dataclasses import dataclass
from random import randint, choice, sample, seed

class TypPacienta(Enum):
    HYPOCHONDR = 0
    NORMAL = 1
    RAMBO = 2

@dataclass
class Pacient:
    rodne_cislo: str
    jmeno_prijmeni: str
    vek: int
    typ: TypPacienta
    pohlavi_zena: bool


class Specializace(Enum):
    NEFROLOGIE = 0
    NEUROLOGIE = 1
    KARDIOLOGIE = 2
    CHIRURGIE = 3
    ORL = 4


@dataclass
class Lekar:
    jmeno_prijmeni: str
    specializace: Specializace

@dataclass
class Ordinace:
    specializace: Specializace
    hlavni_lekar: Lekar
    pomocny_lekar: Lekar
    pacienti: list[Pacient]


@dataclass
class Nemocnice:
    ordinace: list[Ordinace]


def generuj_nemocnici(tisk: bool, pocet_ordinaci) -> Nemocnice:
    seed(42)

    # Helper functions
    def generate_pacient(rodne_cislo, jmeno_prijmeni):
        vek = randint(1, 100)
        typ = choice(list(TypPacienta))
        pohlavi_zena = choice([True, False])
        return Pacient(rodne_cislo, jmeno_prijmeni, vek, typ, pohlavi_zena)

    def generate_lekar(jmeno_prijmeni, specializace):
        return Lekar(jmeno_prijmeni, specializace)

    # Generate shared patients
    shared_pacienti = [
        generate_pacient(f"{100000+idx}{idx}", f"Shared Pacient {idx}") for idx in range(5)
    ]

    # Generate ordinace and nemocnice
    ordinace_list = []
    specializace_list = list(Specializace)

    for i in range(pocet_ordinaci):
        specializace = specializace_list[i % len(specializace_list)]
        hlavni_lekar = generate_lekar(f"Hlavni Lekar {i}", specializace)
        pomocny_lekar = generate_lekar(f"Pomocny Lekar {i}", choice(list(Specializace))) if i % 2 == 0 else None

        pacienti = shared_pacienti + [
            generate_pacient(f"{100000+i}{j}", f"Pacient {i}-{j}") for j in range(7)
        ]
        pacienti = sample(pacienti, len(pacienti))  # Shuffle patients

        ordinace_list.append(
            Ordinace(
                specializace=specializace,
                hlavni_lekar=hlavni_lekar,
                pomocny_lekar=pomocny_lekar,
                pacienti=pacienti
            )
        )

    nemocnice = Nemocnice(ordinace=ordinace_list)

    # Output for verification
    if tisk:
        for ord in nemocnice.ordinace:
            print(f"Ordinace: {ord.specializace}")
            print(f"  Hlavni lekar: {ord.hlavni_lekar}")
            if ord.pomocny_lekar:
                print(f"  Pomocny lekar: {ord.pomocny_lekar}")
            print("  Pacienti:")
            for pacient in ord.pacienti:
                print(f"    {pacient}")
            print()
    return nemocnice

nemocnice = generuj_nemocnici(True, 4)

"""
*Pacient*
- rodné číslo
- jméno + příjmení
- věk
- typ: hypochondr, normal, superman
*Lékař*
- jméno + příjmení
- zkušenost: zaučuji se, normal, expert
- obor: kardio, nefro, neuro, orl, interna, radio, gynekologie
*Ordinace*
- název: jakékoliv pojmenování
- kapacita
- seznam pacientů
- hlavní lékař
- pomocný lékař
*Nemocnice*
- seznam ordinací
*Dynamika*
- ordinaci předěláme na normální třídu
- na ordinaci bychom chtěli následující metody:
1. přidej pacienta: signalizuje výjimkou, pokud je ordinace přes kapacitu
2. vrať všechny hypochondry
3. má ordinace volnou kapacitu?: vrací boolean true/false
- nemocnici předěláme na normální třídu
- na nemocnici bychom chtěli následující metody:
1. vrať seznam všech specializací, které nemocnice nabízí
   (procházením ordinací a sběrem jejich specializací)
2. vrať seznam ordinací, které mají ještě volnou kapacitu
3. vrať seznam všech pacientů nemocnice
4. vrať seznam všech expertů v nemocnici
5. umí specializaci?: vrací true/false podle toho zda hlavní nebo pomocný
   lékař některé z ordinací má danou specializaci
"""

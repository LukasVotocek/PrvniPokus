# typové anotace
"""
def add_numbers(a : int, b : int) -> int:
    return a + b

def format_name(first : str, last : str, upper : bool) -> str:
    name = f"{first} {last}"
    if upper:
        return name.upper()
    return name

"""
#print(add_numbers(1,2))
#print(format_name("Lukas", "Votocek", True))

"""def add_numbers(a: int, b: int) -> int:
    return a + b

def format_name(first: str, last: str, upper: bool) -> str:
    name = f"{first} {last}"
    if upper:
        return name.upper()
    return name"""

"""
def suda_cisla(seznam:list[int]) -> list[int]:
    vysledek:list[int]=[]
    
    for cislo in seznam:
        if cislo%2==0:
            vysledek.append(cislo)
    return vysledek

seznam:list[int]=[1,2,3,4,5,6,7,8,9,10,11,12]
vysledek:list[int]=[cislo for cislo in seznam if cislo%2==0]


print(suda_cisla([1,2,3,4,5,6,7,8,9,10,11,12]))
print(vysledek)"""

"""
studenti_tuple = [
    ("Jan Novák", 20, "informatika"),
    ("Marie Svobodová", 22, "matematika"),
    ("Petr Dvořák", 19, "fyzika"),
    ("Lucie Němcová", 21, "ekonomie"),
    ("Tomáš Černý", 23, "informatika"),
    ("Karolína Procházková", 20, "matematika"),
    ("Jakub Kučera", 18, "informatika"),
    ("Tereza Veselá", 22, "fyzika"),
    ("Martin Horák", 21, "ekonomie"),
    ("Veronika Marková", 19, "informatika"),
    ("Filip Pospíšil", 24, "matematika"),
    ("Anna Králová", 20, "fyzika"),
    ("David Beneš", 22, "ekonomie"),
    ("Kristýna Růžičková", 19, "informatika"),
    ("Ondřej Fiala", 21, "matematika"),
    ("Barbora Malinová", 23, "fyzika"),
    ("Michal Sedláček", 20, "ekonomie"),
    ("Nikola Doležalová", 18, "informatika"),
    ("Adam Nguyen", 22, "fyzika"),
    ("Eliška Krejčí", 21, "matematika"),
]

def vyber_studenty(studenti:list[tuple[str,int,str]], min_vek:int) -> list[str]:
    return [student[0] for student in studenti if student[1] >= min_vek]

vybrani_studenti = vyber_studenty(studenti_tuple, 21)
print(vybrani_studenti)
"""




from dataclasses import dataclass
from enum import Enum 
"""
def add_numbers(a: int | float, b: int | float) -> int | float:
    return a + b

def format_name(first: str, last: str, upper: bool) -> str:
    name = f"{first} {last}"
    if upper:
        return name.upper()
    return name

def suda_cisla(seznam: list[int]) -> list[int]:
    vysledek: list[int] = []
    for cislo in seznam:
        if cislo%2 == 0:
            vysledek.append(cislo)
    return vysledek
    
print(suda_cisla([1,5,4,6,3,2]))

seznam=[1,5,4,6,3,2]
print([cislo for cislo in seznam if cislo%2==0])
"""
"""
class StudijniObor(Enum):
    INFORMATIKA = "informatika"
    MATEMATIKA = "matematika"
    FYZIKA = "fyzika"
    EKONOMIE = "ekonomie"

@dataclass
class Student:
    jmeno: str
    vek: int
    obor: StudijniObor



studenti_dataclass = [
    Student("Jan Novák", 20, StudijniObor.INFORMATIKA),
    Student("Marie Svobodová", 22, StudijniObor.MATEMATIKA),
    Student("Petr Dvořák", 19, StudijniObor.FYZIKA),
    Student("Lucie Němcová", 21, StudijniObor.EKONOMIE),
    Student("Tomáš Černý", 23, StudijniObor.INFORMATIKA),
    Student("Karolína Procházková", 20, StudijniObor.MATEMATIKA),
    Student("Jakub Kučera", 18, StudijniObor.INFORMATIKA),
    Student("Tereza Veselá", 22, StudijniObor.FYZIKA),
    Student("Martin Horák", 21, StudijniObor.EKONOMIE),
    Student("Veronika Marková", 19, StudijniObor.INFORMATIKA),
    Student("Filip Pospíšil", 24, StudijniObor.MATEMATIKA),
    Student("Anna Králová", 20, StudijniObor.FYZIKA),
    Student("David Beneš", 22, StudijniObor.EKONOMIE),
    Student("Kristýna Růžičková", 19, StudijniObor.INFORMATIKA),
    Student("Ondřej Fiala", 21, StudijniObor.MATEMATIKA),
    Student("Barbora Malinová", 23, StudijniObor.FYZIKA),
    Student("Michal Sedláček", 20, StudijniObor.EKONOMIE),
    Student("Nikola Doležalová", 18, StudijniObor.INFORMATIKA),
    Student("Adam Nguyen", 22, StudijniObor.FYZIKA),
    Student("Eliška Krejčí", 21, StudijniObor.MATEMATIKA)
]

def vyber_studenty_dataclass(studenti: list[Student], min_vek: int = 10, obor: StudijniObor | None = None) -> list[Student]:
    vybrani = [student for student in studenti if (student.vek >= min_vek) and (obor is None or student.obor == obor)]
    return vybrani

def seznam_studentu_jako_mapa(studenti: list[Student]) -> dict[str, Student]:
    seznamstudentu: dict[str, Student] = {}
    for student in studenti:
        seznamstudentu[student.jmeno] = student
    return seznamstudentu

print(seznam_studentu_jako_mapa(studenti_dataclass))"""


class StudijniObor(Enum):
    INFORMATIKA = "informatika"
    MATEMATIKA = "matematika"
    FYZIKA = "fyzika"
    EKONOMIE = "ekonomie"

@dataclass
class Student:
    jmeno: str
    rodne_cislo: str
    obor: StudijniObor

studenti_pouziti = [
    Student("Jan Novák", "000120/1234", StudijniObor.INFORMATIKA),
    Student("Marie Svobodová", "985622/5678", StudijniObor.MATEMATIKA),
    Student("Petr Dvořák", "010519/9012", StudijniObor.FYZIKA),
    Student("Lucie Němcová", "996221/3456", StudijniObor.EKONOMIE),
    Student("Tomáš Černý", "970823/7890", StudijniObor.INFORMATIKA),
]

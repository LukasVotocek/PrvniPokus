from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any
from enum import Enum
from abc import ABC, abstractmethod
from collections import deque

"""

@dataclass 
class Uzel:
    hodnota: str
    levy: Uzel | None = None
    pravy: Optional[Uzel] = None


#(3+2)*4-8
tri=Uzel("3")
dva=Uzel("2")
plus=Uzel("+",tri,dva)
ctyri=Uzel("4")
krat=Uzel("*", plus, ctyri)
osm=Uzel("8")
minus=Uzel("-",krat,osm)


def tisk(n:Uzel):
    if (n.levy is None):
        print(n.hodnota)
    else: 
        tisk(n.levy)
        print(n.hodnota)
        tisk(n.pravy)

tisk(minus)"""

#fronta, FIFO (first in, first out)
#tiskova fronta


"""
@dataclass
class Uloha:
    file:str
    user:str

class Printer:
    def __init__ (self) ->None:
        self.fronta=deque()
    def enqueue(self,file,user):
        self.fronta.append(Uloha(file,user))    

    def print_next(self):
        print(self.fronta.popleft())

    def print_all(self):
        while self.fronta:
            self.print_next()

printer = Printer()
printer.enqueue("tabulka.xls", "Karel")
printer.enqueue("referat.docx", "Lida")
printer.enqueue("dovolena.jpeg", "Rudolf")

printer.print_all()"""






    
"""
class Op(Enum):
    PLUS = "+"
    MINUS = "-"
    TIMES = "*"
    DIVIDE = "/"
    
    def __str__(self) -> str:
        return self.value


class Uzel(ABC):
    
    @abstractmethod
    def eval(self) -> float:
        pass


class ListUzel:

    def __init__(self, hodnota) -> None:
        self.hodnota = hodnota
    
    def __str__(self) -> str:
        return str(self.hodnota)
    
    def eval(self) -> float:
        return self.hodnota
        

class BinUzel:

    def __init__(self, operace, levy, pravy) -> None:
        self.operace = operace
        self.levy = levy
        self.pravy = pravy

    def __str__(self) -> str:
        return str(self.operace)
    
    def eval(self) -> float:
        l = self.levy.eval()
        p = self.pravy.eval()
        if self.operace == Op.PLUS:
            return l + p
        elif self.operace == Op.MINUS:
            return l - p
        elif self.operace == Op.TIMES:
            return l * p
        elif self.operace == Op.DIVIDE:
            return l / p
        else:
            raise ValueError(f"Neznama operace {self.operace}?")
        
def bfs(koren):
    fronta=deque()
    seznam=[]
    fronta.append(koren)
    while fronta:
        celo=fronta.popleft()
        seznam.append(celo)
        if isinstance(celo,BinUzel):
            fronta.append(celo.levy)
            fronta.append(celo.pravy)
    return seznam



uzel10 = ListUzel(10)
uzel5 = ListUzel(5)

uzel_plus = BinUzel(Op.PLUS, uzel10, uzel5)
lst=bfs(uzel_plus)

for i in lst:
    print (i)

print(uzel_plus.eval())"""



"""class Historie:
    def __init__(self):
        self.zasobnik=deque()

    def open_page(self,url):
        self.zasobnik.append(url)

    def go_back(self):
        self.zasobnik.pop()

"""

class Prohlizeni:
    def __init__(self)->None:
        self.historie:deque=deque()
        self.budoucnost:deque=deque()
        self.aktualni=""

    def open_page(self,url):
        self.historie.append(self.aktualni)
        self.aktualni=url

    def go_back(self):
        self.budoucnost.append(self.aktualni)
        self.aktualni=self.historie.pop()
        print(self.aktualni)

    def go_forward(self):
        self.historie.append(self.aktualni)
        self.aktualni=self.budoucnost.pop()
        print(self.aktualni)

a=Prohlizeni()
a.open_page("wikipedie")
a.open_page("wiki")
a.open_page("google")
a.open_page("arcig")
a.go_back()
a.go_back()
a.go_back()
a.go_forward()
a.go_forward()
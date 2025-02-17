"""from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

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

from collections import deque
class Printer:
    def __init__ (self) ->None:
        self.fronta=deque()
    def enqueue(self,file,user):
        self.fronta.append((file,user))    

    def print_next(self):
        print(self.fronta.popleft())

    def print_all(self):
        while self.fronta:
            self.print_next()

printer = Printer()
printer.enqueue("tabulka.xls", "Karel")
printer.enqueue("referat.docx", "Lida")
printer.enqueue("dovolena.jpeg", "Rudolf")

printer.print_all()
from __future__ import annotations
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

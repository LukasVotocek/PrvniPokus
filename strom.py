from __future__ import annotations
from dataclasses import dataclass

@dataclass 
class Uzel:
    operace: str
    levy: Uzel
    pravy: Uzel


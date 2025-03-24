from typing import List, Tuple
from dataclasses import dataclass
class Graph:
    
    def __init__(self) -> None:
        self.cities : set[str] = set()
    
    def new_edge(self, from_city: str, to_city: str, distance: int) -> None:
        ...

    def najdi_sousedy(self, z_mesta):
        ...

@dataclass
class Cesta:
    mesta: List[str]
    delka: int
    

def vyzkousej_cesty(graph, nazev_startovniho_mesta,dosud_projita_cesta):
    sousedi=graph.najdi_sousedy(nazev_startovniho_mesta)
    for soused,vzdalenost in sousedi:
        if soused in dosud_projita_cesta.mesta:
            continue
        cesta_do_souseda=Cesta(dosud_projita_cesta.mesta+[soused],dosud_projita_cesta.delka+vzdalenost)
        if len(cesta_do_souseda.mesta)==graph.kolik_mest():
            if graph.existuje_cesta(soused,cesta_do_souseda.mesta[0]):
        vyzkousej_cesty(graph,soused,cesta_do_souseda)






def load_europe() -> Graph:
    graph = Graph()
    graph.new_edge("Lisbon", "Madrid", 339)
    graph.new_edge("Naples", "Rome", 134)
    graph.new_edge("Hamburg", "Copenhagen", 180)
    graph.new_edge("Hamburg", "Berlin", 182)
    graph.new_edge("Berlin", "Warsaw", 345)
    graph.new_edge("Amsterdam", "Hamburg", 338)
    graph.new_edge("Amsterdam", "Brussels", 164)
    graph.new_edge("Berlin", "Prague", 219)
    graph.new_edge("Prague", "Warsaw", 479)
    graph.new_edge("Prague", "Vienna", 185)
    graph.new_edge("Munich", "Prague", 174)
    graph.new_edge("Vienna", "Warsaw", 464)
    graph.new_edge("Vienna", "Budapest", 214)
    graph.new_edge("Warsaw", "Budapest", 394)
    graph.new_edge("Budapest", "Belgrade", 319)
    graph.new_edge("Vienna", "Belgrade", 490)
    graph.new_edge("Budapest", "Trieste", 384)
    graph.new_edge("Trieste", "Vienna", 317)
    graph.new_edge("Trieste", "Belgrade", 403)
    graph.new_edge("Munich", "Vienna", 280)
    graph.new_edge("Munich", "Rome", 582)
    graph.new_edge("Genoa", "Trieste", 361)
    graph.new_edge("Genoa", "Rome", 328)
    graph.new_edge("Trieste", "Rome", 442)
    graph.new_edge("Paris", "Genoa", 629)
    graph.new_edge("Genoa", "Bern", 304)
    graph.new_edge("Genoa", "Brussels", 740)
    graph.new_edge("Bern", "Brussels", 497)
    graph.new_edge("Amsterdam", "Bern", 558)
    graph.new_edge("Amsterdam", "Munich", 526)
    graph.new_edge("Bern", "Munich", 311)
    graph.new_edge("Bern", "Trieste", 489)
    graph.new_edge("Bern", "Madrid", 1104)
    graph.new_edge("Madrid", "Genoa", 951)
    graph.new_edge("Madrid", "Paris", 805)
    graph.new_edge("Paris", "Brussels", 225)
    return graph


load_europe()
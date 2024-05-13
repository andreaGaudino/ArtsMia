from dataclasses import dataclass

from model.artObject import ArtObject


@dataclass
class Connessione:
    o1: ArtObject
    o2: ArtObject
    peso: int

    def __str__(self):
        return f"Arco: {self.o1.object_id} - {self.o2.object_id} - peso: {self.peso}"

from Pet import Pet
from Owner import Owner
import vetRecord

class Simulation:
    def __init__(self, vet):
        self.vet = vet

    def run(self):
        lisa = Owner("Lisa", "1 Street St, Burlington VT", 8021234567)
        dracula = Pet("Dracula","Feline","Domestic Shorthair",4)
        lisa.adoptPet(dracula)



from Pet import Pet
from Owner import Owner
from VetRecord import VetRecord

class Simulation:
    def __init__(self, vet):
        self.vet = vet

    def run(self):
        lisa = Owner("Lisa", "1 Street St, Burlington VT", 8021234567)
        dracula = Pet("Dracula","Feline","Domestic Shorthair",4)
        self.vet.addPetRecord(dracula)
        lisa.adoptPet(dracula)
        firstVisit = VetRecord("03/31/2020","04/11/2021","Dr. Dolittle")
        firstVisit.reasonForVisit(dracula.getPetName() + " was looking under the weather.")
        dracula.setVetRecord(firstVisit)
        print("Thank you for visiting today, " + dracula.getPetName() + "!")
        print("Vet Record for: " + lisa.getOwnerName())
        print("Today's Visit: " + firstVisit.getLastVisit())
        print("Scheduled Follow-Up: " + firstVisit.getNextVisit())
        print("Reason for Visit: " + firstVisit.getReason())
        print("--------------------------------------------------------")

        print("The Vet Record is currently as follows: ")
        # self.vet.displayPetRecords() TODO: This does not currently work

        fluffy = Pet("Fluffy","Canine","Pug",2)
        jeff = Pet("Jeff","Feline","Domestic Shorthair", 3)

        lisa.adoptPet(fluffy)
        lisa.adoptPet(jeff)
        print("Lisa is trying to schedule another visit for her one of her cats.")
        print("Lisa owns the following pets: ")
        lisa.getPets()







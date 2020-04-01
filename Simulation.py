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
        lisa.adoptPet(dracula, lisa)
        print("\n" + dracula.getPetName() + " is owned by " + dracula.getOwner().getOwnerName())
        firstVisit = VetRecord("03/31/2020","04/11/2021","Dr. Dolittle")
        firstVisit.reasonForVisit(dracula.getPetName() + " had a routine visit.")
        dracula.setVetRecord(firstVisit)
        thisVisit = VetRecord("04/03/2020","04/11/2020","Dr. Dolittle")
        thisVisit.reasonForVisit(dracula.getPetName() + " was looking a little under the weather.")
        dracula.setVetRecord(thisVisit)
        print("Thank you for visiting today, " + dracula.getPetName() + "!")
        print("Vet Record for: " + lisa.getOwnerName())
        print("Today's Visit: " + thisVisit.getLastVisit())
        print("Scheduled Follow-Up: " + thisVisit.getNextVisit())
        print("Reason for Visit: " + thisVisit.getReason())
        print("--------------------------------------------------------")

        print("The Vet Record is currently as follows: ")
        self.vet.displayPetRecords()

        fluffy = Pet("Fluffy","Canine","Pug",2)
        jeff = Pet("Jeff","Feline","Domestic Shorthair", 3)

        lisa.adoptPet(fluffy, lisa)
        self.vet.addPetRecord(fluffy)
        lisa.adoptPet(jeff, lisa)
        self.vet.addPetRecord(jeff)
        print("Lisa is trying to schedule another visit for her one of her cats.")
        print("Lisa owns the following pets: ")
        lisa.getPets()
        print("\n")

        fluffyVisit = VetRecord("04/01/2020", "04/01/2022", "Professor McGonagall")
        fluffyVisit.reasonForVisit(fluffy.getPetName() + " had a slight limp.")
        fluffy.setVetRecord(fluffyVisit)

        print("Thank you for visiting today, " + fluffy.getPetName() + "!")
        print("Vet Record for: " + lisa.getOwnerName())
        print("Today's Visit: " + fluffyVisit.getLastVisit())
        print("Scheduled Follow-Up: " + fluffyVisit.getNextVisit())
        print("Reason for Visit: " + fluffyVisit.getReason())
        print("--------------------------------------------------------")







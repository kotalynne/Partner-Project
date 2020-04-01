from Pet import Pet
from Owner import Owner
from VetRecord import VetRecord


class Simulation:
    def __init__(self, vet):
        self.vet = vet

    def run(self):
        # display vet record!
        print("Displaying current Pet record \n_________________________________________________")
        lisa = Owner("Lisa", "1 Street St, Burlington VT", 8021234567)
        fifi = Pet("Fifi", "Feline", "Persian", 2, lisa)
        fifi.addVetRecord(VetRecord("1st January 2020", " In 6 months", "Dr.DoLittle", "Threw up food"))
        fifi.addVetRecord(VetRecord("2nd March 2020", " In 1 month", "Dr.DoLittle", "Ate trash"))
        self.vet.addPetRecord(fifi)
        if (len(self.vet.petRecords)) == 0:
            print("There is no pet record to show")
        else:
            self.vet.displayPetRecords()

        print("Took in a kitten up for adoption")
        dracula = Pet("Dracula", "Feline", "Domestic Shorthair", 4)
        self.vet.addPetRecord(dracula)
        dracula.addVetRecord(VetRecord("4th April 2020", "In one month", "Dr.DoLittle", "check-up"))
        print("Found a stray pug  \n \nDisplaying pet records now")
        fluffy = Pet("Fluffy", "Canine", "Pug", 2)
        self.vet.addPetRecord(fluffy)
        fluffy.addVetRecord(VetRecord("4th April 2020", "In one month", "Dr.Nancy", "General check-up"))
        # display vet record!
        if (len(self.vet.petRecords)) == 0:
            print("There is no pet record to show")
        else:
            self.vet.displayPetRecords()

        print("Lisa comes in with her cat Fifi for a visit ")
        if self.vet.findPet("Fifi") == None:
            print("Cannot find pet record. Does not exist in database")
        else:
            self.vet.findPet("Fifi").getVetRecord()

        #setting pet record for today's visit
        fifi.addVetRecord(VetRecord("04th April 2020", " In 6 months", "Dr.DoLittle", "Check-Up"))

        print("\nLisa adopts dracula")
        lisa.adoptPet(dracula, lisa)
        print("Lisa adopts fluffy\n")
        lisa.adoptPet(fluffy, lisa)


        print("Displaying Lisa's pets")
        if len(lisa.pets) == 0:
            print("Lisa has no pets to show")
        else:
            lisa.getPets()


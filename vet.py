class Vet:
    def __init__(self):
        self.petRecords = []

    def displayPetRecords(self):
        print("--------------------------------------------------------")
        for i in range(len(self.petRecords)):
            print(self.printRecord(self.petRecords[i]))

    def addPetRecord(self, Pet):
        Pet.id = len(self.petRecords)
        self.petRecords.append(Pet)

    def findPet(self, petName):
        for i in self.petRecords:
            if self.petRecords[i].petName == petName:
                return self.petRecords[i]
        return None

    def findOwner(self, ownerName):
        for i in range(len(self.petRecords)):
            if self.petRecords[i].Owner.ownerName == ownerName:
                return self.petRecords[i]
        return None

    def displayVetRecord(self, Pet):
        print("Pet Information for: " + Pet.getPetName() + "\nAge: " + str(Pet.getAge()) + "\nDate of Last Visit: " + Pet.VetRecord.getLastVisit() + "\nDate of Next Visit: "
            + Pet.VetRecord.getNextVisit() + "\nVet: " + Pet.VetRecord.getVetName() + "\n--------------------------------------------------------")

    def printRecord(self, Pet):
        print("Pet Information for: " + Pet.getPetName() + "\nAge: " + str(Pet.getAge()) + "\nDate of Last Visit: " + Pet.VetRecord.getLastVisit() + "\nDate of Next Visit: "
            + Pet.VetRecord.getNextVisit() + "\nVet: " + Pet.VetRecord.getVetName() + "\n--------------------------------------------------------")
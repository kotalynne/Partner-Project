class Vet:
    def __init__(self):
        self.petRecords = []

    def displayPetRecords(self):
        for i in self.petRecords:
            print(self.printRecord(self.petRecords[i]))

    def addPetRecord(self, Pet):
        Pet.id = len(self.petRecords)
        self.petRecords.append(Pet)

    def findPet(self, petName):
        for i in self.petRecords:
            if self.petRecords[i].name == petName:
                return self.petRecords[i]
        return None

    def findOwner(self, ownername):
        for i in self.petRecords:
            if self.petRecords[i].Owner.name == ownername:
                return self.petRecords[i]
        return None
    def displayVetRecord(self, Pet):
        print("the pets vet record")

    def printRecord(self, Pet):
        print("the pets info")
class Vet:

    def __init__(self):
        self.petRecords = []

    def displayPetRecords(self):

        for i in range(len(self.petRecords)):
            print(self.petRecords[i].toString())
            print("--------------------------------------------------------")

    def addPetRecord(self, Pet):
        Pet.id = len(self.petRecords)
        self.petRecords.append(Pet)

    def findPet(self, petName):
        for i in range(len(self.petRecords)):
            if self.petRecords[i].petName == petName:
                return self.petRecords[i]
        return None

    def findOwner(self, ownerName):
        tempPetHold = []
        for i in range(len(self.petRecords)):
            if self.petRecords[i].Owner != None:

                if self.petRecords[i].Owner.ownerName == ownerName:
                    tempPetHold.append(self.petRecords[i])
        return tempPetHold

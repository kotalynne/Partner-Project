class Pet:

    # constructor
    def __init__(self, name, species, breed, age, Owner=None):
        self.id = None
        self.petName = name
        self.species = species
        self.breed = breed
        self.age = age
        self.Owner = Owner
        self.VetRecord = []
        if Owner is not None:
            Owner.adoptPet(self, Owner)

    # getters
    def getId(self):
        return self.id

    def getPetName(self):
        return self.petName

    def getSpecies(self):
        return self.species

    def getBreed(self):
        return self.breed

    def getAge(self):
        return self.age

    def getOwner(self):
        return self.Owner

    def getVetRecord(self):
        print("Accessing vet Records for ", self.petName)
        for i in range(len(self.VetRecord)):
            print(self.VetRecord[i].toString())
            print("_______________________________________")
        return self.VetRecord

    # setters

    def addVetRecord(self, VetRecord):
        self.VetRecord.append(VetRecord)

    # to string
    def toString(self):
        if self.Owner is None:
            return "Pet Information for: " + self.getPetName() + "\nID: " + str(self.getId()) + "\nAge: " + str(
                self.getAge()) + "\nOwner: " + str(self.getOwner()) + self.VetRecord[-1].toString()
        return "Pet Information for: " + self.getPetName() + "\nID: " + str(self.getId()) + "\nAge: " + str(
            self.getAge()) + "\nOwner: " + str(self.getOwner().ownerName) + self.VetRecord[-1].toString()

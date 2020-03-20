class Pet:

    # constructor
    def __init__(self, name, species, breed, age):
        self.id = None
        self.petName = name
        self.species = species
        self.breed = breed
        self.age = age
        self.Owner = None
        self.VetRecord = None

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
        return self.VetRecord


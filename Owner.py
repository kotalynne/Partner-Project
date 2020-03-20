class Owner:

    # constructor
    def __init__(self, ownerName, address, phone):
        self.ownerName = ownerName
        self.address = address
        self.pets = []
        self.phone = phone

    # getters
    def getOwnerName(self):
        return self.OwnerName
    def getAddress(self):
        return self.Address
    def getPet(self):
        return self.Pet
    def getPhone(self):
        return self.phone

    # others
    def adoptPet(self, Pet):
        self.pets.append(self, Pet)


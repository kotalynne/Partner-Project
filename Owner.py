class Owner:

    # constructor
    def __init__(self, ownerName, address, phone):
        self.ownerName = ownerName
        self.address = address
        self.pets = []
        self.phone = phone

    # getters
    def getOwnerName(self):
        return self.ownerName

    def getAddress(self):
        return self.address

    def getPhone(self):
        return self.phone

    def getPets(self):
        for i in range(len(self.pets)):
            print(self.pets[i].petName)
        return len(self.pets)

    # others
    def adoptPet(self, Pet, Owner):
        self.pets.append(Pet)
        Pet.Owner = Owner


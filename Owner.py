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
            temp = self.pets[i]
            print(temp.getPetName(), end = ", ")

    # others
    def adoptPet(self, Pet):
        self.pets.append(Pet)


class VetRecord:
    def __init__(self, lastVist, nextVisit, vetName, reason):
        self.lastVisit = lastVist
        self.nextVisit = nextVisit
        self.vetName = vetName
        self.reasonForVisit = reason

    def getNextVisit(self):
        return self.nextVisit

    def getLastVisit(self):
        return self.lastVisit

    def getVetName(self):
        return self.vetName

    def getReason(self):
        return self.reasonForVisit



    def toString(self):
        return "\nLast visit to vet: " + self.getVetName() + ", " + self.getLastVisit() + ", " + self.getReason() +"\nNext visit: " + self.getNextVisit()



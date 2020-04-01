class VetRecord:
    def __init__(self, todayDate, nextVisit, vet):
        self.lastVisit = todayDate
        self.nextVisit = nextVisit
        self.vet = vet

    def getNextVisit(self):
        return self.nextVisit

    def getLastVisit(self):
        return self.lastVisit

    def getVetName(self):
        return self.vet

    def getReason(self):
        return self.reasonForVisit

    def setNextVisit(self, nextVisit):
        self.nextVisit = nextVisit

    def setLastVisit(self, todayDate):
        self.lastVisit = todayDate

    def reasonForVisit(self, reason):
        self.reasonForVisit = reason

    def setVetName(self, vetName):
        self.vet = vetName



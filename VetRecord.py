class VetRecord:
    def __init__(self, todayDate, nextVisit, vet):
        self.lastVisit = todayDate
        self.nextVisit = nextVisit
        self.vet = vet

    def getNextVisit(self):
        return self.nextVisit

    def setNextVisit(self, nextVisit):
        self.nextVisit = nextVisit

    def resonForVisit(self, reason):
        self.reasonForVisit = reason

    def getVetName(self):
        return self.vet

    def setVetName(self, vetName):
        self.vet = vetName



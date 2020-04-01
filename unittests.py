import unittest
from vet import Vet
from Owner import Owner
from Pet import Pet
from VetRecord import VetRecord


class TestVet(unittest.TestCase):

    def setUp(self):
            print("set-up")
            self.vet = Vet()
            self.lisa = Owner("Lisa", "1 Street St, Burlington VT", 8021234567)
            self.sherlock = Owner("Sherlock", "Baker street", 2342342334)
            self.knox = Pet("Knox", "Feline", "Domestic short hair", 2)
            self.fluffy = Pet("Fluffy", "Canine", "Pug", 2)
            self.dracula = Pet("Dracula", "Feline", "Domestic Shorthair", 4)
            self.record1 = VetRecord("4th April 2020", "In one month", "Dr.DoLittle", "check-up")
            self.record2 = VetRecord("2nd January 2020", "In one week", "Dr.Nancy", "Ate trash")

    def tearDown(self):
        print("tear down")

    def test_one(self):
        print("testing the owner class ")
        # check there are no pet records in the vet class
        self.assertEqual(len(self.vet.petRecords), 0)
        #add dracula to record
        self.vet.addPetRecord(self.dracula)
        self.assertEqual(len(self.vet.petRecords),1)
        #check dracula has no owner
        self.assertEqual(self.dracula.getOwner(), None)
        #lisa adopts dracula
        self.lisa.adoptPet(self.dracula, self.lisa)
        self.assertEqual(self.dracula.getOwner(),self.lisa)
        #testing the owner info
        self.assertEqual(self.dracula.getOwner().getOwnerName(), "Lisa")
        self.assertEqual(self.dracula.getOwner().getPhone(), 8021234567)
        self.assertEqual(self.dracula.getOwner().getAddress(), "1 Street St, Burlington VT")
        self.assertEqual(self.lisa.getPets(),1)

        #adopt another pet
        self.lisa.adoptPet(self.knox, self.lisa)
        self.assertEqual(self.lisa.getPets(), 2)

    def test_two(self):
        print("testing the vet class")
        #add two pets to the vet record
        self.vet.addPetRecord(self.dracula)
        self.vet.addPetRecord(self.fluffy)
        self.assertEqual(len(self.vet.petRecords),2)

        # find pet by name
        self.assertEqual(self.vet.findPet("Dracula"),self.dracula)
        self.assertEqual(self.vet.findPet("fifi"),None)

        #testing findowner method
        self.assertEqual(self.vet.findOwner("Lisa"),[])
        self.lisa.adoptPet(self.dracula, self.lisa)
        self.assertEqual(self.vet.findOwner("Lisa"), [self.dracula])

    def test_three(self):
        print("testing the getters of the pet class")
        self.vet.addPetRecord(self.knox)
        self.assertEqual(self.vet.petRecords[0].getPetName(),"Knox")
        self.assertEqual(self.vet.petRecords[0].getAge(), 2)
        self.assertEqual(self.vet.petRecords[0].getId(), 0)
        self.assertEqual(self.vet.petRecords[0].getSpecies(), "Feline")
        self.assertEqual(self.vet.petRecords[0].getBreed(),"Domestic short hair")

    def test_four(self):
        print("testing vet Record class")
        self.vet.addPetRecord(self.fluffy)
        self.fluffy.addVetRecord(self.record1)
        self.assertEqual(self.fluffy.getVetRecord(),[self.record1])








if __name__ == "__main__":
    unittest.main()

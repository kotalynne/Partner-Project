from vet import Vet
from Simulation import Simulation

def main():
    initialize = Vet()

    sim = Simulation(initialize)
    sim.run()

main()
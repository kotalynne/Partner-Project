import vet
import Simulation

def main():
    initialize = vet.Vet()

    visit = Simulation.Simulation(initialize)
    visit.run()

main()
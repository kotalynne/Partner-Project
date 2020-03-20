import vet
import simulation

def main():
    initialize = vet.Vet().get()

    visit = simulation.Simulation(initialize)
    visit.run()

main()
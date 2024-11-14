from game.knight import Knight
class Population:
    def __init__(self, population_size):
        self.population_size = population_size
        self.generation = 1
        self.knights = [knight() for _ in range(self.population_size)]

    def check_population(self):
          for knight in self.knights:
              knight.check_moves()

if __name__ == "__main__":
    population_size = 10  # Define the size of the population
    population1 = Population(population_size)
    population1.check_population()
    for knight in population1.knights:
        print(f"Knight final position: {knight.position}")
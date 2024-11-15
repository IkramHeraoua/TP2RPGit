import random
class Chromosome:
  def __init__(self, genes=None):
      self.genes = [random.randint(1, 8) for _ in range(63)] if genes is None else genes

  def __str__(self):
      return str(self.genes)

  def __iter__(self):
      return iter(self.genes)

  # Ajoutez cette méthode
  def __len__(self):
      return len(self.genes)

  def crossover(self , partner):
      point = random.randint(0, len(self.genes) - 1)
      child1_genes = self.genes[:point] + partner.genes[point:]
      child2_genes = partner.genes[:point] + self.genes[point:]
      return Chromosome(child1_genes), Chromosome(child2_genes)

  def mutation(self, mutation_rate=0.05):
      for i in range(len(self.genes)):
          if random.random() < mutation_rate:
              current_value = self.genes[i]
              new_value = random.randint(1, 8)
              while new_value == current_value:
                  new_value = random.randint(1, 8)
              self.genes[i] = new_value
import random

class Chromosome:
    def __init__(self, genes=None):
        if genes is None:
            # Générer 63 mouvements aléatoires (1-8)
            self.genes = [random.randint(1, 8) for _ in range(63)]
        else:
            self.genes = genes

    def __str__(self):
        return str(self.genes)

    def __iter__(self):
        return iter(self.genes)

    def crossover(self , partner):
        point = random.randint(0, len(self.genes) - 1)
        child1_genes = self.genes[:point] + partner.genes[point:]
        child2_genes = partner.genes[:point] + self.genes[point:]
        return Chromosome(child1_genes), Chromosome(child2_genes)

    def mutation(self):
        # Choisir un gène aléatoire à muter
        index_to_mutate = random.randint(0, len(self.genes) - 1)
        print(f"Index choisi pour mutation: {index_to_mutate}")

        # Assigner une nouvelle valeur aléatoire au gène, différente de l'actuelle
        current_value = self.genes[index_to_mutate]
        new_value = current_value
        while new_value == current_value:
            new_value = random.randint(0, 7)

        self.genes[index_to_mutate] = new_value
        print(f"Valeur avant mutation: {current_value}, Valeur après mutation: {new_value}")


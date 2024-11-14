from genetic.chromosome import Chromosome
import random
class Knight:
    def __init__(self, chrome=None):
        self.position = [0, 0]
        self.chromosome = chrome if chrome is not None else Chromosome()
        self.path = [self.position]
        self.fitness = 0

        self.moves = {
            1: [1, -2],  # up-right
            2: [2, -1],  # right-up
            3: [2, 1],  # right-down
            4: [1, 2],  # down-right
            5: [-1, 2],  # down-left
            6: [-2, 1],  # left-down
            7: [-2, -1],  # left-up
            8: [-1, -2]  # up-left
        }

    def move_forward(self, direction):
        x, y = self.position
        if direction in self.moves:
            dx, dy = self.moves[direction]
            new_position = [x + dx, y + dy]
            self.position = new_position
            self.path.append(new_position)
            #print("path", self.path)
            return new_position
        else:
            raise ValueError("Invalid direction. Must be an integer between 1 and 8.")

    def move_backward(self):
        if len(self.path) > 1:
            self.path.pop()
            self.position = self.path[-1]
        else:
            raise ValueError("Cannot move backward from the initial position.")

    def is_valid_move(self, position):
        x, y = position
        if not (0 <= x < 8 and 0 <= y < 8):
            return False
        if position in self.path[:-1]:
            return False
        return True

    def check_moves(self):
        for i, move in enumerate(self.chromosome):
            initial_position = self.position
            next_position = self.move_forward(move)
            if not self.is_valid_move(next_position):
                self.move_backward()  # Annuler le mouvement
                cycle_direction = random.choice(['forward', 'backward'])
                if cycle_direction == 'forward':
                    for new_move in range(move + 1, move + 9):  # Cycler vers l'avant
                        adjusted_move = (new_move - 1) % 8 + 1
                        next_position = self.move_forward(adjusted_move)
                        if self.is_valid_move(next_position):

                            move = adjusted_move  # Remplacer dans le chromosome

                            self.position = next_position  # Mettre à jour la position ici
                            break
                        else:
                            self.move_backward()
                else:
                    for new_move in range(move - 1, move - 9, -1):  # Cycler vers l'arrière
                        adjusted_move = (new_move - 1) % 8 + 1
                        next_position = self.move_forward(adjusted_move)
                        if self.is_valid_move(next_position):
                            move = adjusted_move  # Remplacer dans le chromosome
                            self.position = next_position  # Mettre à jour la position ici
                            break
                        else:
                            self.move_backward()

            # Si aucun mouvement valide n'a été trouvé, on garde l'ancien mouvement
            if not self.is_valid_move(next_position):
                self.move_forward(move)


def evaluate_fitness():
    pass

if __name__ == "__main__":
    knight1 = Knight()
    print("Chromosome après vérification:", knight1.chromosome)
    knight1.check_moves()
    print("Chromosome après vérification:", knight1.chromosome)
    print("Chemin emprunté:", knight1.path)



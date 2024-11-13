
class knight:
    def __init__(self, chromosome=None):
        self.position = [0, 0]
        #self.chromosome = chromosome if chromosome is not None else chromosome()
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
            new_position = (x + dx, y + dy)
            self.position = new_position
            self.path.append(new_position)
            return new_position
        else:
            raise ValueError("Invalid direction. Must be an integer between 1 and 8.")

    def move_backward(self):
        if len(self.path) > 1:
            self.path.pop()
            self.position = self.path[-1]
        else:
            raise ValueError("Cannot move backward from the initial position.")


def check_moves():
    pass

def evaluate_fitness():
    pass


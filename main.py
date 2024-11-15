import pygame
import random
import sys
from genetic.population import Population
from visualisation.visualize import Visualize
from game.knight import Knight

def main():
    pygame.init()
    population_size = 50
    population = Population(population_size)
    while True:
        population.check_population()
        maxFit, bestSolution = population.evaluate()
        print(f"Génération {population.generation} - Meilleure aptitude: {maxFit}")
        if maxFit == 64:
            print(f"Solution trouvée en {population.generation} générations")
            break
        population.create_new_generation()


    screen = pygame.display.set_mode((720, 720))
    pygame.display.set_caption("Knight's Tour")
    font = pygame.font.Font(None, 36)
    try:
        knight_image = pygame.image.load("assets/knight.png")
        knight_image = pygame.transform.scale(knight_image, (80, 80))  # Resize the knight image if needed
    except pygame.error as e:
        print(f"Error loading the knight image: {e}")
        sys.exit()

    # Initialize the Visualize class
    visualizer = Visualize()
    knight_obj = Knight(bestSolution.chromosome)  # Replace with your implementation
    knight_obj.check_moves()  # Ensure moves are correct
    knight_obj.evaluate_fitness()

    running = True
    index = 0
    clock = pygame.time.Clock()
    light_assets = ["assets/board_green_light.png", "assets/board_brown_light.png"]
    dark_assets = ["assets/board_green_dark.png", "assets/board_brown_dark.png"]
    number_color = [(0, 0, 0), (255, 255, 255)]
    i = random.randint(0, 1)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if index < len(knight_obj.path):
            visualizer.draw_board(screen, font, knight_image, knight_obj.path[index], index + 1,light_assets[i],dark_assets[i],number_color[i])
            index += 1
            pygame.display.flip()
            clock.tick(2)  # Control the display speed
        else:
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
  main()
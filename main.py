import pygame
import sys
from genetic.chromosome import Chromosome
from visualisation.visualize import Visualize
from game.knight import Knight

def main():
  pygame.init()

  # Créer l'écran et charger l'image du cavalier
  screen = pygame.display.set_mode((480, 480))
  pygame.display.set_caption("Knight's Tour")
  font = pygame.font.Font(None, 36)
  try:
      knight_image = pygame.image.load("assets/cavalier.png")  
      knight_image = pygame.transform.scale(knight_image, (50, 50))  # Redimensionner l'image si nécessaire
  except pygame.error as e:
      print(f"Erreur lors du chargement de l'image: {e}")
      sys.exit()
  # Initialiser la classe Visualize
  visualizer = Visualize()
  knight_obj = Knight()

  running = True
  while running:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False

      visualizer.draw_board(screen, font, knight_image, knight_obj.position)

      pygame.display.flip()


  pygame.quit()
  sys.exit()

if __name__ == "__main__":
  main()
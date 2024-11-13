
import pygame
import sys

# Interface graphique avec Pygame
def draw_solution(screen, font):
    # Taille de la fenêtre et des cases
    BOARD_SIZE = 400
    MARGIN = 40  # Marge autour du plateau pour les numéros de ligne/colonne
    CELL_SIZE = BOARD_SIZE // 8
    BORDER_COLOR = (0, 50 , 0)  # Couleur des bordures


    # Couleurs
    WHITE = (230, 230, 220)
    GREEN = (0, 50 , 0)
    TEXT_COLOR = (0, 0, 0)  # Bleu pour le texte


    screen.fill(WHITE)

    # Dessiner l'échiquier
    for i in range(8):
        for j in range(8):
            rect = pygame.Rect(MARGIN + i * CELL_SIZE, MARGIN + j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, WHITE, rect)
            else:
                pygame.draw.rect(screen, GREEN, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


    # Ajouter les numéros de ligne (à gauche et à droite, en dehors du plateau)
    for i in range(8):
        text_surface = font.render(str(i + 1), True, TEXT_COLOR)
        screen.blit(text_surface, (MARGIN // 3, MARGIN + i * CELL_SIZE + CELL_SIZE // 3))  # À gauche
        screen.blit(text_surface, (MARGIN + 8 * CELL_SIZE + 5, MARGIN + i * CELL_SIZE + CELL_SIZE // 3))  # À droite

    # Ajouter les lettres des colonnes (en haut et en bas, en dehors du plateau)
    for j in range(8):
        text_surface = font.render(str(j + 1), True, TEXT_COLOR)
        screen.blit(text_surface, (MARGIN + j * CELL_SIZE + CELL_SIZE // 3, MARGIN // 5))  # En haut
        screen.blit(text_surface, (MARGIN + j * CELL_SIZE + CELL_SIZE // 3, MARGIN + 8 * CELL_SIZE + 5))  # En bas

def main():
    pygame.init()
    BOARD_SIZE = 400
    MARGIN = 40  # Espace pour afficher les numéros de ligne/colonne
    WINDOW_SIZE = BOARD_SIZE + 2 * MARGIN  # Taille totale de la fenêtre
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Chess Board")

    # Charger la police pour afficher le texte
    font = pygame.font.SysFont(None, 24)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_solution(screen, font)

        # Met à jour l'affichage
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()



# Test the Knight class
knight = knight()
# Test moving forward
try:
  print("Initial Position:", knight.position)
  print("Move Forward (direction 1):", knight.move_forward(1))
  print("Move Forward (direction 2):", knight.move_forward(2))
  print("Current Position:", knight.position)
  print("Path:", knight.path)
except ValueError as e:
  print(e)

# Test moving backward
try:
  knight.move_backward()
  print("After Moving Backward, Position:", knight.position)
  print("Path:", knight.path)
except ValueError as e:
  print(e)

# Test invalid move
try:
  knight.move_forward(9)  # Invalid direction
except ValueError as e:
  print("Error:", e)

# Test moving backward from initial position
try:
  knight.move_backward()
  knight.move_backward()  # This should raise an error
except ValueError as e:
  print("Error:", e)

def main():
    pygame.init()
    BOARD_SIZE = 400
    MARGIN = 40  # Espace pour afficher les numéros de ligne/colonne
    WINDOW_SIZE = BOARD_SIZE + 2 * MARGIN  # Taille totale de la fenêtre
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Chess Board")

    # Charger la police pour afficher le texte
    font = pygame.font.SysFont(None, 24)

    # Charger l'image du cavalier (assurez-vous que l'image est dans le même répertoire ou donnez le chemin complet)
    knight_image = pygame.image.load("C:/Users/user/PycharmProjects/TP2RPGit/assets/cavalier.png")  # Remplacez "knight.png" par votre chemin d'image
    CELL_SIZE = BOARD_SIZE // 8
    knight_image = pygame.transform.scale(knight_image, (CELL_SIZE, CELL_SIZE))  # Redimensionner à la taille d'une case

    # Position du cavalier (0, 0) correspond à la case 1,1 (en haut à gauche)
    knight_pos = (0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_solution(screen, font, knight_image, knight_pos)

        # Met à jour l'affichage
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

import pygame
import sys


class Visualize:

    def __init__(self, board_size=400, margin=40):
        self.BOARD_SIZE = board_size
        self.MARGIN = margin
        self.CELL_SIZE = self.BOARD_SIZE // 8
        self.BORDER_COLOR = (0, 70, 0)  # Couleur des bordures
        self.BEIGE = (245, 245, 220)  # Beige pour les cases claires
        self.DARK_BOTTLE_GREEN = (0, 70, 0)  # Vert bouteille pour les cases sombres
        self.TEXT_COLOR = (0, 70, 0)  # Bleu pour le texte

    def draw_board(self, screen, font, knight_image, position):
        screen.fill((255, 255, 255))  # Remplir l'écran avec une couleur de fond
        screen.blit(knight_image, position)  # Dessiner l'image du cavalier à la position donnée

        screen.fill(self.BEIGE)

        # Dessiner l'échiquier avec des bordures fines
        for i in range(8):
            for j in range(8):
                rect = pygame.Rect(self.MARGIN + i * self.CELL_SIZE, self.MARGIN + j * self.CELL_SIZE, self.CELL_SIZE,
                                   self.CELL_SIZE)
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, self.BEIGE, rect)
                else:
                    pygame.draw.rect(screen, self.DARK_BOTTLE_GREEN, rect)

                # Dessiner des bordures fines autour de chaque case
                pygame.draw.rect(screen, self.BORDER_COLOR, rect, 1)

        # Ajouter les numéros de ligne (à gauche et à droite, en dehors du plateau)
        for i in range(8):
            text_surface = font.render(str(i + 1), True, self.TEXT_COLOR)
            screen.blit(text_surface,
                        (self.MARGIN // 3, self.MARGIN + i * self.CELL_SIZE + self.CELL_SIZE // 3))  # À gauche
            screen.blit(text_surface, (
            self.MARGIN + 8 * self.CELL_SIZE + 5, self.MARGIN + i * self.CELL_SIZE + self.CELL_SIZE // 3))  # À droite

        # Ajouter les lettres des colonnes (en haut et en bas, en dehors du plateau)
        for j in range(8):
            text_surface = font.render(str(j + 1), True, self.TEXT_COLOR)
            screen.blit(text_surface,
                        (self.MARGIN + j * self.CELL_SIZE + self.CELL_SIZE // 3, self.MARGIN // 5))  # En haut
            screen.blit(text_surface, (
            self.MARGIN + j * self.CELL_SIZE + self.CELL_SIZE // 3, self.MARGIN + 8 * self.CELL_SIZE + 5))  # En bas

        # Placer l'image du cavalier à la position donnée (knight_pos)
        knight_x, knight_y = position
        knight_rect = pygame.Rect(self.MARGIN + knight_x * self.CELL_SIZE,
                                  self.MARGIN + knight_y * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
        screen.blit(knight_image, knight_rect)
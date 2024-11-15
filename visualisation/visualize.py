import pygame
import random
class Visualize:
    def __init__(self):
        self.square_size = 90  # Taille d'une case
        self.visited_squares = [[None for _ in range(8)] for _ in range(8)]  # Track visited squares

    def draw_board(self, screen, font, knight_image, knight_position, move_number,light_assets,dark_assets,color):
        # Load and scale the images to the size of the squares

        light_square_image_im = pygame.image.load(light_assets)
        dark_square_image_im = pygame.image.load(dark_assets)
        light_square_image = pygame.transform.scale(light_square_image_im, (self.square_size, self.square_size))
        dark_square_image = pygame.transform.scale(dark_square_image_im, (self.square_size, self.square_size))

        # Update the visited squares
        x, y = knight_position
        self.visited_squares[x][y] = move_number

        # Draw the board and numbers
        for row in range(8):
            for col in range(8):
                image = light_square_image if (row + col) % 2 == 0 else dark_square_image
                screen.blit(image, (col * self.square_size, row * self.square_size))
                if self.visited_squares[row][col] is not None:
                    number_text = font.render(str(self.visited_squares[row][col]), True, color)
                    screen.blit(number_text, (col * self.square_size + 20, row * self.square_size + 15))

        # Draw the knight
        screen.blit(knight_image, (y * self.square_size + 5, x * self.square_size + 5))
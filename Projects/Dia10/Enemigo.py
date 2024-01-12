import pygame


class Enemigo:
    # enemigo_x_cambio = 0.3
    # enemigo_y_cambio = 50

    def __init__(self, image, x, y):
        self.forma = pygame.image.load(image)
        self.enemigo_x = x
        self.enemigo_y = y

    def enemigo(self, pantalla):
        pantalla.blit(self.forma, (self.enemigo_x, self.enemigo_y))

    def setPosition_x(self, modPosition_x):
        self.enemigo_x += modPosition_x

    def setPosition_y(self, position_y):
        self.enemigo_y += position_y


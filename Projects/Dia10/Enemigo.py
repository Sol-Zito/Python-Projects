import pygame


class Enemigo:

    def __init__(self, image, x, y):
        self.forma = pygame.image.load(image)
        self.posicion_x = x
        self.posicion_y = y


    def enemigo(self, pantalla):
        pantalla.blit(self.forma, (self.posicion_x, self.posicion_y))

    def setPosition_x(self, modPosition_x):
        self.posicion_x += modPosition_x

    def setPosition_y(self, modPosition_y):
        self.posicion_y += modPosition_y


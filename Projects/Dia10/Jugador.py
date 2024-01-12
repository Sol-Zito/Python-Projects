import pygame


class Jugador():

    def __init__(self, image, x, y):
        self.cohete = pygame.image.load(image)
        self.jugador_x = x
        self.jugador_y = y

    def setPosition(self, modPosition):
        # MODIFICAR UBICACION JUGADOR
        self.jugador_x += modPosition
        # MANTENER DENTRO DE PANTALLA
        if self.jugador_x <= 0:
            jugador_x = 0
        elif self.jugador_x >= 736:
            jugador_x = 736

    def jugador(self, pantalla):
        pantalla.blit(self.cohete, (self.jugador_x, self.jugador_y))

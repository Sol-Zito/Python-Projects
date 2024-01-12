import pygame


class Jugador:

    def __init__(self, image, x, y):
        self.cohete = pygame.image.load(image)
        self.posicion_x = x
        self.posicion_y = y

    def setPosition(self, mod_position):
        # MODIFICAR UBICACION JUGADOR
        self.posicion_x += mod_position
        # MANTENER DENTRO DE PANTALLA
        if self.posicion_x <= 0:
            self.posicion_x = 0
        elif self.posicion_x >= 736:
            self.posicion_x = 736

    def jugador(self, pantalla):
        pantalla.blit(self.cohete, (self.posicion_x, self.posicion_y))

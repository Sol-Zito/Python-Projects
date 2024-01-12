import pygame


class Bala:
    isVisible = False
    posicion_x = 0
    posicion_y = 500
    bala_x_cambio = 0
    bala_y_cambio = 1

    def __init__(self, image):
        self.bala_img = pygame.image.load(image)

    def disparo(self, pantalla):
        self.isVisible = True
        pantalla.blit(self.bala_img, (self.posicion_x + 16, self.posicion_y + 10))

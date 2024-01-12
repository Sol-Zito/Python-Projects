import math
import random

from Bala import *
from Jugador import *
from Enemigo import *
import pygame

# INICIAR GAME
pygame.init()

# CREAR PANTALLA
pantalla = pygame.display.set_mode((800, 600))


# TITULO E ICONO
pygame.display.set_caption('Invasion Espacial')
icono = pygame.image.load("Photos/ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Photos/Fondo.jpg")

# JUGADOR VARIABLES
nave = Jugador("Photos/cohete.png", 368, 500)
jugador_x_cambio = 0


# ENEMIGO VARIABLES
nave_enemiga = Enemigo("Photos/enemigo.png", random.randint(0, 736), random.randint(50, 200))
enemigo_x_cambio = 0.3
enemigo_y_cambio = 50


# BALA VARIABLES
# bala_img = pygame.image.load("Photos/bala.png")
# bala_x = 0
# bala_y = 500
# bala_x_cambio = 0
# bala_y_cambio = 1
# isVisible = False
#
# def disparo(x, y):
#     global isVisible
#     isVisible = True
#     pantalla.blit(bala_img, (x + 16, y + 10))
bala = Bala("Photos/bala.png")


# DETECTAR COLISIONES
def hay_colision(x1, x2, y1, y2):
    x_cuadrado = math.pow(x1 - x2, 2)
    y_cuadrado = math.pow(y1 - y2, 2)
    distancia = math.sqrt(x_cuadrado + y_cuadrado)
    if distancia < 27:
        return True
    else:
        return False

# LOOP DEL GAME
se_ejecuta = True
puntaje = 0

while se_ejecuta:
    # PANTALLA
    pantalla.blit(fondo, (0, 0))
    # ITERAR EVENTOS
    for event in pygame.event.get():
        # SIRVE PARA CERRAR EL PROGRAMA
        if event.type == pygame.QUIT:
            se_ejecuta = False

        # PRESIONAR FLECHAS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jugador_x_cambio = -0.2
            if event.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.2
            if event.key == pygame.K_SPACE:
                if not bala.isVisible:
                    bala.bala_x = nave.jugador_x
                    bala.disparo(pantalla)

        # SOLTAR FLECHAS
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador_x_cambio = 0


    # MODIFICAR UBICACION JUGADOR
    nave.setPosition(jugador_x_cambio)

    # MODIFICAR UBICACION ENEMIGO
    nave_enemiga.setPosition_x(enemigo_x_cambio)

    # MANTENER DENTRO DE PANTALLA
    if nave_enemiga.enemigo_x <= 0:
        enemigo_x_cambio = 0.2
        nave_enemiga.enemigo_y += enemigo_y_cambio
    elif nave_enemiga.enemigo_x >= 734:
        enemigo_x_cambio = -0.2
        nave_enemiga.enemigo_y += enemigo_y_cambio


    # MANTENER DENTRO DE PANTALLA
    if bala.bala_y <= -64:
        bala.bala_y = 500
        bala.isVisible = False
    if bala.isVisible:
        bala.disparo(pantalla)
        bala.bala_y -= bala.bala_y_cambio

    # Colision
    colision = hay_colision(nave_enemiga.enemigo_x, bala.bala_x, nave_enemiga.enemigo_y, bala.bala_y)
    if colision:
        bala.bala_y = 500
        bala.isVisible = False
        puntaje += 1
        print(f"Puntaje: {puntaje}")
        nave_enemiga.setPosition_x(random.randint(50, 600))
        nave_enemiga.setPosition_y(random.randint(50, 200))

    nave.jugador(pantalla)
    nave_enemiga.enemigo(pantalla)

    # ACTUALIZAR
    pygame.display.update()


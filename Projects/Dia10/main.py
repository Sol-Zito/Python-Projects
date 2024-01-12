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
# nave_enemiga = Enemigo("Photos/enemigo.png", random.randint(5, 736), random.randint(50, 200))
enemigo_x_cambio = 0.3
enemigo_y_cambio = 50

lista_enemigos = []

for i in range(4):
    i = Enemigo("Photos/enemigo.png", random.randint(5, 736), random.randint(50, 200))
    lista_enemigos.append(i)


# BALA VARIABLES
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
                    bala.posicion_x = nave.posicion_x
                    bala.disparo(pantalla)

        # SOLTAR FLECHAS
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador_x_cambio = 0


    # MODIFICAR UBICACION JUGADOR
    nave.setPosition(jugador_x_cambio)


    for e in lista_enemigos:
        # MODIFICAR UBICACION ENEMIGO
        e.setPosition_x(enemigo_x_cambio)

        # MANTENER ENEMIGO DENTRO DE PANTALLA
        if e.posicion_x <= 0:
            enemigo_x_cambio = 0.2
            e.posicion_y += enemigo_y_cambio
        elif e.posicion_x >= 736:
            enemigo_x_cambio = -0.2
            e.posicion_y += enemigo_y_cambio

        # Colision
        colision = hay_colision(e.posicion_x, bala.posicion_x, e.posicion_y, bala.posicion_y)
        if colision:
            bala.posicion_y = 500
            bala.isVisible = False
            puntaje += 1
            print(f"Puntaje: {puntaje}")
            e.setPosition_x(random.randint(0, 700))
            e.setPosition_y(random.randint(50, 500))
            print(f"Nave enemiga: x: {e.posicion_x}, y: {e.posicion_y}")

        e.enemigo(pantalla)


    # MANTENER DENTRO DE PANTALLA
    if bala.posicion_y <= -64:
        bala.posicion_y = 500
        bala.isVisible = False
    if bala.isVisible:
        bala.disparo(pantalla)
        bala.posicion_y -= bala.bala_y_cambio

    nave.jugador(pantalla)


    # ACTUALIZAR
    pygame.display.update()


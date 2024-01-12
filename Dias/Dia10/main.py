import random

import pygame

# INICIAR GAME
pygame.init()

# CREAR PANTALLA
pantalla = pygame.display.set_mode((800, 600))


# TITULO E ICONO
pygame.display.set_caption('Invasion Espacial')
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Fondo.jpg")

# JUGADOR VARIABLES
cohete = pygame.image.load("cohete.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# JUGADOR FUNCTIONS
def jugador(x, y):
    pantalla.blit(cohete, (x, y))


# ENEMIGO VARIABLES
enemigo_img = pygame.image.load("enemigo.png")
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
enemigo_x_cambio = 0.3
enemigo_y_cambio = 50

# ENEMIGO FUNCTIONS
def enemigo():
    pantalla.blit(enemigo_img, (enemigo_x, enemigo_y))

# BALA VARIABLES
bala_img = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
isVisible = False

def disparo(x, y):
    global isVisible
    isVisible = True
    pantalla.blit(bala_img, (x + 16, y + 10))

# LOOP DEL GAME
se_ejecuta = True

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
                disparo(jugador_x, bala_y)

        # SOLTAR FLECHAS
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador_x_cambio = 0


    # MODIFICAR UBICACION JUGADOR
    jugador_x += jugador_x_cambio
    # MANTENER DENTRO DE PANTALLA
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # MODIFICAR UBICACION ENEMIGO
    enemigo_x += enemigo_x_cambio
    # MANTENER DENTRO DE PANTALLA
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.2
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio = -0.2
        enemigo_y += enemigo_y_cambio


    # MANTENER DENTRO DE PANTALLA
    if isVisible:
        disparo(jugador_x, bala_y)
        bala_y -= bala_y_cambio


    jugador(jugador_x, jugador_y)
    enemigo()

    # ACTUALIZAR
    pygame.display.update()


import math
import random
import pygame
from pygame import mixer
from Bala import *
from Jugador import *
from Enemigo import *


# INICIAR GAME
pygame.init()

# CREAR PANTALLA
pantalla = pygame.display.set_mode((800, 600))

# TITULO E ICONO
pygame.display.set_caption('Invasion Espacial')
icono = pygame.image.load("Photos/ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Photos/Fondo.jpg")

# AGREGAR MUSICA
mixer.music.load("Music/MusicaFondo.mp3")
mixer.music.set_volume(0.4)
mixer.music.play(-1)

# JUGADOR VARIABLES
nave = Jugador("Photos/cohete.png", 368, 500)
jugador_x_cambio = 0

# ENEMIGO VARIABLES
lista_enemigos = []

for i in range(8):
    i = Enemigo("Photos/enemigo.png", random.randint(0, 736), random.randint(50, 200), 0.5, 50)
    lista_enemigos.append(i)

# BALA VARIABLES
balas = []
img_bala = pygame.image.load("Photos/bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False


# DETECTAR COLISIONES
def hay_colision(x1, x2, y1, y2):
    x_cuadrado = math.pow(x1 - x2, 2)
    y_cuadrado = math.pow(y1 - y2, 2)
    distancia = math.sqrt(x_cuadrado + y_cuadrado)
    if distancia < 27:
        return True
    else:
        return False


# PUNTAJE
puntaje = 0
fuente = pygame.font.Font('Fonts/Consider.otf', 32)
texto_x = 10
texto_y = 10


# MOSTRAR PUNTAJE
def mostar_puntaje():
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (10, 10))


# TEXTO FINAL DEL JUEGO
txt_final = pygame.font.Font('Fonts/Consider.otf', 50)


def texto_final():
    texto_final = txt_final.render("Juego terminado", True, (255, 255, 255))
    print("Juego terminado")
    pantalla.blit(texto_final, (60, 200))


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

            # Disparar balance
            if event.key == pygame.K_SPACE:
                sonido_disparo = mixer.Sound('Music/disparo.mp3')
                sonido_disparo.play()

                nueva_bala = {
                        "x": nave.posicion_x,
                        "y": nave.posicion_y,
                        "velocidad": -5
                }
                balas.append(nueva_bala)

        # SOLTAR FLECHAS
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # MODIFICAR UBICACION JUGADOR
    nave.setPosition(jugador_x_cambio)



    for e in lista_enemigos:
        # FIN DEL JUEGO
        dead = hay_colision(e.posicion_x, nave.posicion_x, e.posicion_y, nave.posicion_y)
        if dead:
            texto_final()
            lista_enemigos.clear()
            balas.clear()
            break

        # MODIFICAR UBICACION ENEMIGO
        e.setPosition_x(e.posicion_x_cambio)

        # MANTENER ENEMIGO DENTRO DE PANTALLA
        if e.posicion_x <= 0:
            e.posicion_x_cambio = 0.3
            e.posicion_y += e.posicion_y_cambio
        elif e.posicion_x >= 706:
            e.posicion_x_cambio = -0.3
            e.posicion_y += e.posicion_y_cambio

        # Colision
        for bala in balas:
            shot = hay_colision(e.posicion_x, bala['x'], e.posicion_y, bala['y'])
            if shot:
                sonido_colision = mixer.Sound("Music/Golpe.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                print(f"Puntaje: {puntaje}")
                e.setPosition_x(random.randint(0, 706))
                e.setPosition_y(random.randint(50, 200))
                break

        e.enemigo(pantalla)

    # Movimiento bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)

    nave.jugador(pantalla)

    mostar_puntaje()

    # ACTUALIZAR
    pygame.display.update()

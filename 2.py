import pygame
from random import randint

pygame.init()

TAMANIO_PANTALLA = [1200, 900]
TAMANIO_PANTALLA_2 = [600, 450]

pantalla = pygame.display.set_mode(TAMANIO_PANTALLA)
corriendo = True
COLOR_FONDO_ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
COLOR_TEXTO_BOTON = (randint(0, 255), randint(0, 255), randint(0, 255))

fuente = pygame.font.SysFont("arial", 100, True, True)
texto_pantalla = fuente.render("Pantalla Principal", True, COLOR_TEXTO_BOTON)
texto_pantalla_puntajes = fuente.render("Pantalla Puntajes", True, COLOR_TEXTO_BOTON)
# texto_pantalla = pygame.transform.scale_by(texto_pantalla, 0.5) # Con pantalla mas chica, reescalamos la superficie.
ubicacion_texto_x = (pantalla.get_width() / 2) - (texto_pantalla.get_width() / 2)
ubicacion_texto_y = (pantalla.get_height() * 0.05)

ubicacion_texto_puntaje_x = (pantalla.get_width() / 2) - (texto_pantalla_puntajes.get_width() / 2)
ubicacion_texto_puntaje_y = (pantalla.get_height() * 0.05)

# Ocupe 20% del ancho, 10% del alto y ubicado en el 2/3 del alto y centrado.
ancho_boton = pantalla.get_width() * 0.2
alto_boton = pantalla.get_height() * 0.1
x_boton = (pantalla.get_width() / 2) - (ancho_boton / 2)
y_boton = pantalla.get_height() * 0.66
rect_boton_jugar = pygame.Rect(x_boton, y_boton, ancho_boton, alto_boton)

# Texto del boton:
texto_jugar = fuente.render("Jugar", True, COLOR_FONDO_ALEATORIO)
texto_jugar = pygame.transform.scale(texto_jugar, (ancho_boton-5, alto_boton-5))
rect_texto_jugar = texto_jugar.get_rect()
rect_texto_jugar.x = rect_boton_jugar.x
rect_texto_jugar.y = rect_boton_jugar.y

bandera_pantalla = "Principal"

while corriendo == True:

    if bandera_pantalla == "Principal":
        # Bucle Eventos de la pantalla Principal
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_boton_jugar.collidepoint(evento.pos) == True:
                    bandera_pantalla = "Puntajes"

        pantalla.fill(COLOR_FONDO_ALEATORIO)
        pantalla.blit(texto_pantalla, (ubicacion_texto_x, ubicacion_texto_y))
        pygame.draw.rect(pantalla, COLOR_TEXTO_BOTON, rect_boton_jugar, border_radius=15)
        pantalla.blit(texto_jugar, rect_texto_jugar)


    elif bandera_pantalla == "Puntajes":
        # Bucle de eventos de la pantalla puntajes.
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
        
        pantalla.fill(COLOR_FONDO_ALEATORIO)
        pantalla.blit(texto_pantalla_puntajes, (ubicacion_texto_x, ubicacion_texto_y))

    pygame.display.flip()
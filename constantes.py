import pygame

from random import randint

pygame.init()

ANCHO = 800
ALTO = 600
TAMANIO_PANTALLA = [ANCHO, ALTO]
CANTIDAD_FILAS = 8
CANTIDAD_COLUMNAS = 8

pantalla = pygame.display.set_mode(TAMANIO_PANTALLA)

COLOR_FONDO = (45, 52, 54)
COLOR_BOTON = (99, 110, 114)
COLOR_TEXTO = (236, 240, 241)
COLOR_TEMPORIZADOR = (231, 76, 60)
COLOR_PUNTAJE = (46, 204, 113)

# COLORES
lista_color = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0), (150, 0, 120), (0, 200, 225)]

# FFUENTES
fuente_grande = pygame.font.SysFont("arial", 60, True)
fuente_mediana = pygame.font.SysFont("arial", 45)
fuente_pequena = pygame.font.SysFont("arial", 35)

# VARIABLES
temporizador = 60
puntaje = 0


# TEXTOS
texto_temporizador = fuente_mediana.render(f"Tiempo: {temporizador}", True, COLOR_TEMPORIZADOR)
texto_puntaje = fuente_mediana.render(f"Puntaje: {puntaje}", True, COLOR_PUNTAJE)

# RECTANGULO CENTRADO A LA IZQUIERDA
ancho_contenedor = int(pantalla.get_width() * 0.55)
alto_contenedor = int(pantalla.get_height() * 0.85)
x_contenedor = int(pantalla.get_width() * 0.05)
y_contenedor = int((pantalla.get_height() - alto_contenedor) / 2)
rect_contenedor = pygame.Rect(x_contenedor, y_contenedor, ancho_contenedor, alto_contenedor)

# PANEL DERECHO
x_panel = x_contenedor + ancho_contenedor + 40
ancho_panel = pantalla.get_width() - x_panel - 40

# POSICIONES DEL PANEL LAT
y_temporizador = 200
y_puntaje = 300

# Botones
ancho_boton = ancho_panel * 0.8
alto_boton = 70
x_boton = x_panel + (ancho_panel - ancho_boton) / 2

# BOTON REINICIAR
y_boton_reiniciar = ALTO * 0.8
rect_boton_reiniciar = pygame.Rect(x_boton, y_boton_reiniciar, ancho_boton, alto_boton)
texto_reiniciar = fuente_pequena.render("Reiniciar", True, COLOR_FONDO)
texto_reiniciar = pygame.transform.scale(texto_reiniciar, (int(ancho_boton * 0.9), int(alto_boton * 0.6)))

# BOTON VOLVER
y_boton_volver = ALTO * 0.6
rect_boton_volver = pygame.Rect(x_boton, y_boton_volver, ancho_boton, alto_boton)
texto_volver = fuente_pequena.render("Volver", True, COLOR_FONDO)
texto_volver = pygame.transform.scale(texto_volver, (int(ancho_boton * 0.9), int(alto_boton * 0.6)))
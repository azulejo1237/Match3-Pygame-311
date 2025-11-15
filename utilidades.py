import pygame
from constantes import *

pygame.init()
# Ventana
ventana_juego = pygame.display.set_mode(tamaño_pantalla)
pygame.display.set_caption("Candy Crush si fuera bueno")

# FUENTES
fuente_grande = pygame.font.SysFont("arial", 60, True)
fuente_mediana = pygame.font.SysFont("arial", 45)
fuente_pequena = pygame.font.SysFont("arial", 35)
fuente_menu_principal = pygame.font.SysFont("arial", 32)

# COLORES
lista_color = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0), (150, 0, 120), (0, 200, 225)]




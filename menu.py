import pygame
from contantes import *

pygame.init()

# Creo la ventana del juego
ventana_menu_principa = pygame.display.set_mode(tamaño_pantalla)
# Titulo de la ventana
pygame.display.set_caption("Candy Crush si fuera bueno")
# Carga la imagen
fondo_menu_principal_img = pygame.image.load("assets/imagenes/tuki.jpg")
# Redimensiona la imagen
fondo_menu_principal_img = pygame.transform.scale(fondo_menu_principal_img, tamaño_pantalla)

# Crea el boton jugar
boton_jugar = pygame.Rect(0, 0, 200, 60)
boton_jugar.center = (ANCHO // 2, ALTO // 2 -200)

boton_puntajes = pygame.Rect(0, 0, 200, 60)
boton_puntajes.center = (ANCHO // 2, ALTO // 2 -100)

boton_resolucion = pygame.Rect(0, 0, 200, 60)
boton_resolucion.center = (ANCHO // 2, ALTO // 2)

boton_salir_main = pygame.Rect(0, 0, 200, 60)
boton_salir_main.center = (ANCHO // 2, ALTO // 2 +100 )

# Fuente del texto
fuente_menu_principal = pygame.font.SysFont("arial", 32)
# Convierte el texto a una imagen
texto_jugar_boton = fuente_menu_principal.render("Jugar", True, COLOR_TEXTO_BOTON)
texto_jugar_rect = texto_jugar_boton.get_rect()

texto_puntajes_boton = fuente_menu_principal.render("Puntajes", True, COLOR_TEXTO_BOTON)
texto_puntajes_rect = texto_puntajes_boton.get_rect()

texto_resolucion_boton = fuente_menu_principal.render("Resolucion", True, COLOR_TEXTO_BOTON)
texto_resolucion_rect = texto_resolucion_boton.get_rect()

texto_salir_main_boton = fuente_menu_principal.render("salir", True, COLOR_TEXTO_BOTON)
texto_salir_main_rect = texto_salir_main_boton.get_rect()

# centro la imagen/texto al boton
texto_jugar_rect.center = boton_jugar.center
texto_puntajes_rect.center = boton_puntajes.center
texto_resolucion_rect.center = boton_resolucion.center
texto_salir_main_rect.center = boton_salir_main.center

# Musica del menu
pygame.mixer.init()
pygame.mixer.music.load("assets/sonidos/musica_menu.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

# Sonido del boton al salir
sonido_click = pygame.mixer.Sound("assets/sonidos/bumper.mp3")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_salir_main.collidepoint(evento.pos):
                sonido_click.play()
                pygame.time.delay(700)
                pygame.quit()
                quit()
        
    # Dibuja la imagen de fondo
    ventana_menu_principa.blit(fondo_menu_principal_img, (0,0))
    
    # Dibuja el boton
    pygame.draw.rect(ventana_menu_principa, Color_BOTON, boton_jugar, border_radius = 10)
    pygame.draw.rect(ventana_menu_principa, Color_BOTON, boton_puntajes, border_radius = 10)
    pygame.draw.rect(ventana_menu_principa, Color_BOTON, boton_resolucion, border_radius = 10)
    pygame.draw.rect(ventana_menu_principa, Color_BOTON, boton_salir_main, border_radius = 10)
    
    # Dibuja el texto del boton
    ventana_menu_principa.blit(texto_jugar_boton, texto_jugar_rect)
    ventana_menu_principa.blit(texto_puntajes_boton, texto_puntajes_rect)
    ventana_menu_principa.blit(texto_resolucion_boton, texto_resolucion_rect)
    ventana_menu_principa.blit(texto_salir_main_boton, texto_salir_main_rect)

    # Actualiza la pantalla
    pygame.display.flip()
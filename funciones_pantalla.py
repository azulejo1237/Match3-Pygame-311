import pygame
from funciones import *
from constantes import * 

# NO USO GLOBALES
ultima_celda = (-1, -1)

# CREACION MATRIZ
matriz = inicializar_matriz(CANTIDAD_FILAS, CANTIDAD_COLUMNAS)
cargar_matriz_aleatoria(matriz, lista_color)
generar_matriz_validada(matriz, lista_color)
crear_botones_matriz(matriz, rect_contenedor)

# BOTONES
y_boton_volver = 380
y_boton_reiniciar = 450
ancho_boton = int(ancho_panel * 0.8)
alto_boton = int(pantalla.get_height() * 0.07)

x_boton = x_panel + (ancho_panel - ancho_boton) // 2

# BOTON REINICIAR
centro_reiniciar = (
    x_boton + ancho_boton // 2,
    y_boton_reiniciar + alto_boton // 2
)
boton_reiniciar = crear_boton(
    "Reiniciar",
    centro_reiniciar,
    fuente_pequena,
    ancho=ancho_boton,
    alto=alto_boton,
    color=COLOR_BOTON,
    color_texto=COLOR_TEXTO
)

# BOTON VOLVER
centro_volver = (
    x_boton + ancho_boton // 2,
    y_boton_volver + alto_boton // 2
)
boton_volver = crear_boton(
    "Volver",
    centro_volver,
    fuente_pequena,
    ancho=ancho_boton,
    alto=alto_boton,
    color=COLOR_BOTON,
    color_texto=COLOR_TEXTO
)

def menu_interacciones():
    global ultima_celda

    corriendo = True
    pantalla_actual = "juego"
    celda_seleccionada = None

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

            if pantalla_actual == "juego" and evento.type == pygame.MOUSEBUTTONDOWN:

                # BOTONES
                if boton_clickeado(evento, boton_reiniciar):
                    print("Boton Reiniciar presionado")

                if boton_clickeado(evento, boton_volver):
                    print("Boton Volver presionado")
                    corriendo = False

                # CLICK MATRIZ
                celda = obtener_celda_click(matriz, evento.pos[0], evento.pos[1])

                if celda is not None:

                    # si no hay celda guardada -> guardo esta
                    if ultima_celda == (-1, -1):
                        ultima_celda = celda

                    # si ya habia -> swap
                    else:
                        swapear_celdas(matriz, ultima_celda, celda)
                        ultima_celda = (-1, -1)
                        celda_seleccionada = None

                    celda_seleccionada = celda
                    print("Celda seleccionada:", celda)

        # DIBUJAR PANTALLA
        if pantalla_actual == "juego":
            pantalla_juego(celda_seleccionada)

def pantalla_juego(celda_seleccionada):
    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, (30, 30, 30), rect_contenedor)

    # MATRIZ
    dibujar_matriz(matriz, pantalla, celda_seleccionada)

    # TEMPORIZADOR
    rect_texto_temporizador = texto_temporizador.get_rect()
    rect_texto_temporizador.centerx = x_panel + ancho_panel / 2
    rect_texto_temporizador.y = y_temporizador
    pantalla.blit(texto_temporizador, rect_texto_temporizador)

    # PUNTAJE
    rect_texto_puntaje = texto_puntaje.get_rect()
    rect_texto_puntaje.centerx = x_panel + ancho_panel / 2
    rect_texto_puntaje.y = y_puntaje
    pantalla.blit(texto_puntaje, rect_texto_puntaje)

    # BOTONES
    dibujar_boton(pantalla, boton_reiniciar)
    dibujar_boton(pantalla, boton_volver)

    pygame.display.flip()

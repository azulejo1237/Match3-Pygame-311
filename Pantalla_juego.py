import pygame
from constantes import *
from random import randint
from utilidades import *

pygame.init()

CANTIDAD_FILAS = 8
CANTIDAD_COLUMNAS = 8

corriendo = True

# VARIABLES
temporizador = 60
puntaje = 0


# TEXTOS
texto_temporizador = fuente_mediana.render(f"Tiempo: {temporizador}", True, COLOR_TEMPORIZADOR)
texto_puntaje = fuente_mediana.render(f"Puntaje: {puntaje}", True, COLOR_PUNTAJE)

# RECTANGULO CENTRADO A LA IZQUIERDA
ancho_contenedor = int(ventana_juego.get_width() * 0.55)
alto_contenedor = int(ventana_juego.get_height() * 0.85)
x_contenedor = int(ventana_juego.get_width() * 0.05)
y_contenedor = int((ventana_juego.get_height() - alto_contenedor) / 2)
rect_contenedor = pygame.Rect(x_contenedor, y_contenedor, ancho_contenedor, alto_contenedor)




# PANEL DERECHO
x_panel = x_contenedor + ancho_contenedor + 40
ancho_panel = ventana_juego.get_width() - x_panel - 40

# POSICIONES DEL PANEL LAT
y_temporizador = 200
y_puntaje = 300

# Botones
ancho_boton = int(ancho_panel * 0.8)
alto_boton = int(ventana_juego.get_height() * 0.07)
x_boton = x_panel + (ancho_panel - ancho_boton) // 2

# BOTON REINICIAR
y_boton_reiniciar = 450
rect_boton_reiniciar = pygame.Rect(x_boton, y_boton_reiniciar, ancho_boton, alto_boton)
texto_reiniciar = fuente_pequena.render("Reiniciar", True, COLOR_FONDO)
rect_texto_reiniciar = texto_reiniciar.get_rect(center=rect_boton_reiniciar.center)
# BOTON VOLVER
y_boton_volver = 550
rect_boton_volver = pygame.Rect(x_boton, y_boton_volver, ancho_boton, alto_boton)
texto_volver = fuente_pequena.render("Volver", True, COLOR_FONDO)
rect_texto_volver = texto_volver.get_rect(center=rect_boton_volver.center)

# INICIALIZAR MATRIZ
def inicializar_matriz(cant_filas: int, cant_columnas: int, valor_inicial: any = None) -> list[list]:
    matriz = []
    for _ in range(cant_filas):
        fila = []
        for _ in range(cant_columnas):
            fila.append(valor_inicial)
        matriz.append(fila)
    return matriz
def cargar_matriz_aleatoria(matriz: list[list], lista_color: list[tuple]) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = {"color": lista_color[randint(0, 5)]}




def crear_botones_matriz(matriz: list[list], rect_cont: pygame.Rect) -> None:
    ancho_celda = int(rect_cont.width * 0.96 / len(matriz[0]))
    alto_celda = int(rect_cont.height * 0.96 / len(matriz))
    margen_x = int(rect_cont.width * 0.02) + rect_cont.x
    margen_y = int(rect_cont.height * 0.02) + rect_cont.y
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            un_rectangulo = pygame.Rect(
                (j * ancho_celda) + margen_x,
                (i * alto_celda) + margen_y,
                ancho_celda,
                alto_celda
            )
            matriz[i][j].update({"rect": un_rectangulo})

def dibujar_matriz(matriz: list[list], pantalla: pygame.Surface, celda_seleccionada:tuple ) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if celda_seleccionada == (i, j):
                dibujar_rectangulo_con_borde(
                    pantalla,
                    matriz[i][j]["color"],
                    matriz[i][j]["rect"],
                    color_borde=(255, 255, 0),
                    grosor_borde=5
                )
            else:
                pygame.draw.rect(pantalla, matriz[i][j]["color"], matriz[i][j]["rect"])
            pygame.draw.rect(pantalla, COLOR_FONDO, matriz[i][j]["rect"], 2)
# CREACION MATRIZ
matriz = inicializar_matriz(CANTIDAD_FILAS, CANTIDAD_COLUMNAS)
cargar_matriz_aleatoria(matriz, lista_color)
crear_botones_matriz(matriz, rect_contenedor)

# DIBUJAR RECTANGULO SELECCIONADO

def dibujar_rectangulo_con_borde(pantalla: pygame.Surface, color: tuple, rect: pygame.Rect, color_borde: tuple = (255, 255, 0), grosor_borde: int = 5) -> None:
    
    pygame.draw.rect(pantalla, color, rect)
    pygame.draw.rect(pantalla, color_borde, rect, grosor_borde)


celda_seleccionada = None

# BUCLE PRINCIPAL
def juego_pantalla(ventana_juego, celda_seleccionada, tiempo_restante, tiempo_inicio):

    # ARRANCAR EL RELOJ AL ENTRAR 
    if tiempo_inicio == -1:
        tiempo_inicio = pygame.time.get_ticks()

    # calcular tiempo
    tiempo_actual = pygame.time.get_ticks()
    segundos_pasados = (tiempo_actual - tiempo_inicio) // 1000
    tiempo_restante = max(60 - segundos_pasados, 0)

    # actualizar texto
    texto_temporizador = fuente_mediana.render(f"Tiempo: {tiempo_restante}", True, COLOR_TEMPORIZADOR)

    #  EVENTOS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return "Salir", celda_seleccionada, tiempo_restante, tiempo_inicio

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if rect_boton_volver.collidepoint(evento.pos):
                return "Volver", celda_seleccionada, tiempo_restante, tiempo_inicio

            if rect_boton_reiniciar.collidepoint(evento.pos):
                tiempo_inicio = pygame.time.get_ticks()
                tiempo_restante = 60

            # clic en celdas
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if matriz[i][j]["rect"].collidepoint(evento.pos):
                        celda_seleccionada = (i, j)

    #  DIBUJO 
    ventana_juego.fill(COLOR_FONDO)

    pygame.draw.rect(ventana_juego, (30, 30, 30), rect_contenedor)
    dibujar_matriz(matriz, ventana_juego, celda_seleccionada)

    # tiempo
    rect_texto_temporizador = texto_temporizador.get_rect()
    rect_texto_temporizador.centerx = x_panel + ancho_panel / 2
    rect_texto_temporizador.y = y_temporizador
    ventana_juego.blit(texto_temporizador, rect_texto_temporizador)

    # puntaje
    rect_texto_puntaje = texto_puntaje.get_rect()
    rect_texto_puntaje.centerx = x_panel + ancho_panel / 2
    rect_texto_puntaje.y = y_puntaje
    ventana_juego.blit(texto_puntaje, rect_texto_puntaje)

    # botones
    pygame.draw.rect(ventana_juego, COLOR_BOTON, rect_boton_reiniciar)
    ventana_juego.blit(texto_reiniciar, rect_texto_reiniciar)

    pygame.draw.rect(ventana_juego, COLOR_BOTON, rect_boton_volver)
    ventana_juego.blit(texto_volver, rect_texto_volver)

    return "Juego", celda_seleccionada, tiempo_restante, tiempo_inicio

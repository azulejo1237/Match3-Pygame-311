import pygame

from random import randint

from constantes import *


# INICIALIZAR MATRIZ
def inicializar_matriz(cant_filas: int, cant_columnas: int, valor_inicial: any = None) -> list[list]:
    matriz = []
    for _ in range(cant_filas):
        fila = []
        for _ in range(cant_columnas):
            fila.append(valor_inicial)
        matriz.append(fila)
    return matriz


# CARGAR MATRIZ
def cargar_matriz_aleatoria(matriz: list[list], lista_color: list[tuple]) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = {"color": lista_color[randint(0, 5)]}

# SE CREAN LAS DIMENSIONES DE LOS BOTONES DE LA MATRIZ

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

# SE LE ASIGNA EL COLOR A CADA ELEMENTO DE LA MATRIZ

def dibujar_matriz(matriz: list[list], pantalla: pygame.Surface, celda_selec:tuple ) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if celda_selec == (i, j):
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


# DIBUJAR RECTANGULO SELECCIONADO

def dibujar_rectangulo_con_borde(pantalla: pygame.Surface, color: tuple, rect: pygame.Rect, color_borde: tuple = (255, 255, 0), grosor_borde: int = 5) -> None:
    
    pygame.draw.rect(pantalla, color, rect)
    pygame.draw.rect(pantalla, color_borde, rect, grosor_borde)



def validar_combinaciones(matriz:list[list]):
    coincidencias = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):

            # horizontal
            if j + 2 < len(matriz[i]):
                c1 = matriz[i][j]["color"]
                c2 = matriz[i][j+1]["color"]
                c3 = matriz[i][j+2]["color"]
                if c1 == c2 == c3:
                    coincidencias += 1


            # vertical
            if i + 2 < len(matriz):
                c1 = matriz[i][j]["color"]
                c2 = matriz[i+1][j]["color"]
                c3 = matriz[i+2][j]["color"]
                if c1 == c2 == c3:
                    coincidencias += 1
    return coincidencias

def generar_matriz_validada(matriz):
    coincidencias = validar_combinaciones(matriz)
    while coincidencias >= 1:
        cargar_matriz_aleatoria(matriz, lista_color)
        coincidencias = validar_combinaciones(matriz)
    return coincidencias
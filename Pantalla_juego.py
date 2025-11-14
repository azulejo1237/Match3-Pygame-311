import pygame
from random import randint

pygame.init()

TAMANIO_PANTALLA = [1200, 900]
CANTIDAD_FILAS = 8
CANTIDAD_COLUMNAS = 8

pantalla = pygame.display.set_mode(TAMANIO_PANTALLA)
corriendo = True

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
y_boton_reiniciar = 450
rect_boton_reiniciar = pygame.Rect(x_boton, y_boton_reiniciar, ancho_boton, alto_boton)
texto_reiniciar = fuente_pequena.render("Reiniciar", True, COLOR_FONDO)
texto_reiniciar = pygame.transform.scale(texto_reiniciar, (int(ancho_boton * 0.9), int(alto_boton * 0.6)))

# BOTON VOLVER
y_boton_volver = 550
rect_boton_volver = pygame.Rect(x_boton, y_boton_volver, ancho_boton, alto_boton)
texto_volver = fuente_pequena.render("Volver", True, COLOR_FONDO)
texto_volver = pygame.transform.scale(texto_volver, (int(ancho_boton * 0.9), int(alto_boton * 0.6)))

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

def dibujar_matriz(matriz: list[list], pantalla: pygame.Surface) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            pygame.draw.rect(pantalla, matriz[i][j]["color"], matriz[i][j]["rect"])
            pygame.draw.rect(pantalla, COLOR_FONDO, matriz[i][j]["rect"], 2)

# CREACION MATRIZ
matriz = inicializar_matriz(CANTIDAD_FILAS, CANTIDAD_COLUMNAS)
cargar_matriz_aleatoria(matriz, lista_color)
crear_botones_matriz(matriz, rect_contenedor)

# BUCLE PRINCIPAL
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rect_boton_reiniciar.collidepoint(evento.pos):
                print("Botón Reiniciar presionado")
            if rect_boton_volver.collidepoint(evento.pos):
                print("Botón Volver presionado")
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if matriz[i][j]["rect"].collidepoint(evento.pos):
                        print(f"Click en celda [{i}][{j}]")
    
    
    pantalla.fill(COLOR_FONDO)
    



    pygame.draw.rect(pantalla, (30, 30, 30), rect_contenedor)
    
    dibujar_matriz(matriz, pantalla)

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
    
    # BOTON REINICIAR
    pygame.draw.rect(pantalla, COLOR_BOTON, rect_boton_reiniciar)
    rect_texto_reiniciar = texto_reiniciar.get_rect()
    rect_texto_reiniciar.center = rect_boton_reiniciar.center
    pantalla.blit(texto_reiniciar, rect_texto_reiniciar)
    
    # BOTON VOLVER
    pygame.draw.rect(pantalla, COLOR_BOTON, rect_boton_volver)
    rect_texto_volver = texto_volver.get_rect()
    rect_texto_volver.center = rect_boton_volver.center
    pantalla.blit(texto_volver, rect_texto_volver)
    
    pygame.display.flip()

pygame.quit()
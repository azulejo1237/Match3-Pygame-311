import pygame

from funciones import *

pygame.init()

# CREACION MATRIZ
matriz = inicializar_matriz(CANTIDAD_FILAS, CANTIDAD_COLUMNAS)  
cargar_matriz_aleatoria(matriz, lista_color)
generar_matriz_validada(matriz)
crear_botones_matriz(matriz, rect_contenedor)



celda_seleccionada = None 

corriendo = True

# BUCLE PRINCIPAL
while corriendo:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rect_boton_reiniciar.collidepoint(evento.pos):
                print("Boton Reiniciar presionado")
            if rect_boton_volver.collidepoint(evento.pos):
                print("Boton Volver presionado")
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if matriz[i][j]["rect"].collidepoint(evento.pos):
                        celda_seleccionada = (i, j)
                        print(f"Click en celda [{i}][{j}]")
    
    
    pantalla.fill(COLOR_FONDO)
    

    pygame.draw.rect(pantalla, (30, 30, 30), rect_contenedor)
    
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
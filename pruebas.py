from funciones import *

matriz = inicializar_matriz(CANTIDAD_FILAS, CANTIDAD_COLUMNAS)
cargar_matriz_aleatoria(matriz, lista_color)

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

coincidencias = validar_combinaciones(matriz)
print(coincidencias)
def generar_matriz_validada(matriz, coincidencias):
    while coincidencias >= 1:
        cargar_matriz_aleatoria(matriz, lista_color)
        coincidencias = validar_combinaciones(matriz)
    return coincidencias

coincidencias = generar_matriz_validada(matriz, coincidencias)
print(coincidencias)

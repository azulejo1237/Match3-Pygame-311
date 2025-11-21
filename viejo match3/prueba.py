import random

def generar_tablero_match3_lista(filas, columnas, num_valores):
    """
    Genera un tablero de juego (matriz) sin 3 o más valores iguales consecutivos
    en horizontal o vertical, utilizando listas de Python.
    """
    # Crear una matriz de ceros (vacia) representada como una lista de listas
    tablero = [[0] * columnas for _ in range(filas)]
    
    # Valores posibles para las gemas (p. ej., números del 1 al 6)
    valores_posibles = list(range(1, num_valores + 1))  

    for f in range(filas):
        for c in range(columnas):
            # Obtener una lista de posibles valores para la celda actual
            posibles = list(valores_posibles)
            
            # --- Regla de Validación ---
            
            # 1. Validación Horizontal (Vecinos a la izquierda)
            if c >= 2:
                # Comprobar si los dos valores inmediatamente a la izquierda son iguales
                valor_izq1 = tablero[f][c - 1]
                valor_izq2 = tablero[f][c - 2]
                
                if valor_izq1 == valor_izq2:
                    # Si el valor que causa la combinación de 3 está en la lista de posibles,
                    # lo eliminamos.
                    if valor_izq1 in posibles:
                        posibles.remove(valor_izq1)

            # 2. Validación Vertical (Vecinos de arriba)
            if f >= 2:
                # Comprobar si los dos valores inmediatamente de arriba son iguales
                valor_arr1 = tablero[f - 1][c]
                valor_arr2 = tablero[f - 2][c]
                
                if valor_arr1 == valor_arr2:
                    # Si el valor que causa la combinación de 3 está en la lista de posibles,
                    # lo eliminamos.
                    if valor_arr1 in posibles:
                        posibles.remove(valor_arr1)

            # Si la lista de 'posibles' no está vacía, elegimos uno al azar.
            # En este contexto, con 6 valores distintos, es casi seguro que siempre habrá opciones.
            if posibles:
                tablero[f][c] = random.choice(posibles)
            else:
                # Esta parte es solo un respaldo, si la lista se vacía, forzamos la elección de 
                # un valor que romperá la racha, si es que existen 3 seguidos.
                tablero[f][c] = random.choice(valores_posibles) # Esto podría causar un match, pero es el plan B
                

    return tablero

# --- Configuración y Ejecución ---
filas = 8
columnas = 8
num_valores = 10

tablero_inicial = generar_tablero_match3_lista(filas, columnas, num_valores)

print(f"🎲 Tablero Inicial de {filas}x{columnas} con {num_valores} valores, sin 3 consecutivos:")

# Función simple para imprimir la lista de listas de forma legible
for fila in tablero_inicial:
    print(fila)
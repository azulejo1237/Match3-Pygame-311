from main import *

corriendo = True
bandera_pantalla = {
    "pantalla": "Principal",
    "celda": None,
    "tiempo_restante": 60,
    "tiempo_inicio": -1  
}

from main import *

corriendo = True
bandera_pantalla = {
    "pantalla": "Principal",
    "celda": None,
    "tiempo_restante": 60,   #el tiempo del reloj 
    "tiempo_inicio": -1      # para ir descontando
}

while corriendo:

    if bandera_pantalla["pantalla"] == "Principal":
        bandera_pantalla = menu_interacciones(bandera_pantalla)
        bandera_pantalla["tiempo_restante"] = 60
        bandera_pantalla["tiempo_inicio"] = -1

    elif bandera_pantalla["pantalla"] == "Juego":
        nueva_pantalla, nueva_celda, tiempo_restante, tiempo_inicio = juego_pantalla(
            ventana_juego,
            bandera_pantalla["celda"],
            bandera_pantalla["tiempo_restante"],
            bandera_pantalla["tiempo_inicio"]
        )

        if nueva_pantalla == "Volver":
            bandera_pantalla["pantalla"] = "Principal"
        else:
            bandera_pantalla["celda"] = nueva_celda
            bandera_pantalla["tiempo_restante"] = tiempo_restante
            bandera_pantalla["tiempo_inicio"] = tiempo_inicio

    elif bandera_pantalla["pantalla"] == "Salir":
        corriendo = False

    pygame.display.flip()



from main import *

corriendo = True
bandera_pantalla = "Principal"

while corriendo:
    bandera_pantalla = menu_interacciones(bandera_pantalla)

    if bandera_pantalla == "Salir":
        corriendo = False

import random

#aqui van la variables globales
pantalla = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
jugador = "X"
triqui = 0
contador = 0

# Función para mostrar un menú
def menu():
    """
    Función que muestra un menú y permite a los jugadores realizar movimientos en el juego del triqui.
    """
    opc = -1
    while opc != 0:
        opc = int(input("Digite 1 para ingresar, 0 para salir"))
        global triqui
        global contador
        if opc == 1:
            while triqui == 0:
                mostrar_pantalla()
                if jugador == "X":
                    opc1 = input("Ingrese del 1 al 9 la posición que desea en el triqui: ")
                    opc1 = int(opc1) - 1
                else:
                    print("Turno de la máquina (O)")
                    opc1 = movimiento_maquina()
                if movimiento(opc1):
                    ganadors = ganador()
                    contador += 1
                    if ganadors is not None:
                        mostrar_pantalla()
                        print(imprimir_color("verde", f"¡El ganador es {ganadors}, fin del juego!"))
                        opc = 0
                        contador = 0
                        break
                    if ganadors is None and contador == 9:
                        mostrar_pantalla()
                        print(imprimir_color("rojo", "¡Empate (ningún ganador), fin del juego"))
                        opc = 0
                        contador = 0
                        break

# Función para mostrar tablero
def mostrar_pantalla():
    """
    Función que muestra el estado actual del tablero en el juego del triqui.
    """
    for i in range(3):
        print(" ".join(pantalla[i * 3:(i + 1) * 3]))


# Función para validar movimiento
def movimiento(opc1):
    """
    Función que valida y realiza un movimiento en el juego del triqui, cambiando el jugador actual.
    @param opc1: Entero, la posición en el tablero donde se desea realizar el movimiento.
    @return: True si el movimiento es válido, False si no es válido.
    """
    global pantalla
    global jugador

    if pantalla[opc1] == "-":
        pantalla[opc1] = jugador
        jugador = "O" if jugador == "X" else "X"
        return True
    else:
        return False
    
# Función para que la máquina (jugador "O") realice un movimiento aleatorio
def movimiento_maquina():
    """
    Función que permite a la máquina (jugador "O") realizar un movimiento aleatorio en el juego del triqui.
    @return: Entero, la posición en el tablero donde se realiza el movimiento.
    """
    opciones_disponibles = [i for i in range(9) if pantalla[i] == "-"]
    movimiento_maquina = random.choice(opciones_disponibles)
    return movimiento_maquina

# Validación del ganador
def ganador():
    """
    Función que valida por fila, columna y diagonal el respectivo ganador en el juego del triqui.
    @return: El jugador ganador ("X" o "O") o None si no hay ganador.
    """
    global pantalla

    # Ganador por fila
    for i in range(3):
        if pantalla[i * 3] == pantalla[i * 3 + 1] == pantalla[i * 3 + 2] != "-":
            return pantalla[i * 3]

    # Ganador por columna
    for i in range(3):
        if pantalla[i * 3] == pantalla[i + 3] == pantalla[i + 6] != "-":
            return pantalla[i]

    # Ganador por diagonal o con un dato igual
    if pantalla[0] == pantalla[4] == pantalla[8] != "-":
        return pantalla[0]

    if pantalla[2] == pantalla[4] == pantalla[6] != "-":
        return pantalla[2]

# Función que imprime color
def imprimir_color(color, mensaje):
    """
    Función que imprime un mensaje del usuario en el color especificado.
    @param: color (str)    Color del texto ("rojo" o "verde").
    @param: mensaje (str)  Mensaje del usuario.
    """
    if color == "rojo":
        print("\x1b[1;31m" + mensaje)
    elif color == "verde":
        print("\x1b[1;32m" + mensaje)
    else:
        print("Color no válido. Utilizando color predeterminado.")
        print(mensaje)
    print("\x1b[0m")



# Ejecución y llamado de funciones
menu()
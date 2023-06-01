def dibujar_tablero(tablero):
    """Dibuja el tablero actual"""
    for fila in tablero:
        print("|".join(fila))
    print()

def verificar_victoria(tablero):
    """Verifica si hay un ganador"""
    # Verificar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != " ":
            return fila[0]
    # Verificar columnas
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != " ":
            return tablero[0][i]
    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
        return tablero[0][2]
    # No hay ganador
    return None

def jugar():
    """Función principal del juego"""
    # Crear el tablero vacío
    tablero = [[" ", " ", " "] for _ in range(3)]
    jugador = "X"
    # Loop del juego
    while True:
        dibujar_tablero(tablero)
        # Pedir al jugador que ingrese su movimiento
        fila = int(input("Fila (1-3): "))
        columna = int(input("Columna (1-3): "))
        # Verificar que la casilla esté vacía
        if tablero[fila-1][columna-1] == " ":
            tablero[fila-1][columna-1] = jugador
            # Verificar si hay un ganador
            ganador = verificar_victoria(tablero)
            if ganador:
                print(f"¡El jugador {ganador} ha ganado!")
                dibujar_tablero(tablero)
                break
            # Cambiar de jugador
            jugador = "O" if jugador == "X" else "X"
        else:
            print("¡La casilla ya está ocupada!")
    print("Fin del juego")

# Iniciar el juego
jugar()

def contar_movimientos_validos(teclado, posicion_inicial, movimientos_restantes):
    if movimientos_restantes == 0:
        return 1
    
    movimientos_validos = 0

    for movimiento in teclado[posicion_inicial]:
        movimientos_validos += contar_movimientos_validos(teclado, movimiento, movimientos_restantes - 1)

    return movimientos_validos

# Declarar el teclado como un array de listas
teclado = [
    [4, 6],   # Posiciones a las que puede moverse desde 0
    [6, 8],   # Posiciones a las que puede moverse desde 1
    [7, 9],   # Posiciones a las que puede moverse desde 2
    [4, 8],   # Posiciones a las que puede moverse desde 3
    [0, 3, 9],# Posiciones a las que puede moverse desde 4
    [],       # El 5 no tiene movimientos válidos
    [0, 1, 7],# Posiciones a las que puede moverse desde 6
    [2, 6],   # Posiciones a las que puede moverse desde 7
    [1, 3],   # Posiciones a las que puede moverse desde 8
    [2, 4]    # Posiciones a las que puede moverse desde 9
]

# Solicitar al usuario el número de movimientos deseados hasta que ingrese "FIN"
while True:
    entrada = input("Ingrese el número de movimientos deseados o escriba 'FIN' para salir: ")
    
    if entrada.upper() == "FIN":
        break  # Salir del bucle si el usuario ingresa "FIN"
    
    try:
        n = int(entrada)
        total_movimientos_validos = 0

        for posicion_inicial in range(len(teclado)):
            total_movimientos_validos += contar_movimientos_validos(teclado, posicion_inicial, n)

        print(f"Total de movimientos válidos para {n} movimientos desde todas las posiciones: {total_movimientos_validos}")
    except ValueError:
        print("Entrada no válida. Ingrese un número o 'FIN' para salir.")


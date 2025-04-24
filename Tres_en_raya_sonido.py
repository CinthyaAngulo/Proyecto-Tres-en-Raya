import winsound  

Player_1 = ""  
Player_2 = ""  

print("¡Bienvenidos! Para comenzar, deberás elegir un token: X o O")  
Token = True  

while Token:  
    Player_1 = input("Jugador 01, elige un token (X u O): ").strip().lower()  
    if Player_1 not in ["x", "o"]:  
        print("Error: Debes ingresar 'X' u 'O'")  
    else:  
        Player_1 = Player_1.upper()  
        Player_2 = "O" if Player_1 == "X" else "X"  
        Token = False  

print(f"PLAYER 1, tu token es {Player_1}")  
print(f"PLAYER 2, tu token es {Player_2}")  
print("¡INICIO DEL JUEGO!")  

puntuacion_1 = 0  
puntuacion_2 = 0  

base = []  
fila = []  
for i in range(1, 10):  
    fila.append(i)  
    if i % 3 == 0:  
        base.append(fila)  
        fila = []  

def mostrar_tablero(tablero):  
    for fila in tablero:  
        print('-' * 13)  
        for j in fila:  
            print(f"| {j} ", end="")  
        print("|")  
    print('-' * 13)  

def sonido_token(jugador):
    if jugador == "X":
        winsound.Beep(600, 150)  # X suena a 600 Hz
    elif jugador == "O":
        winsound.Beep(800, 150)  # O suena a 800 Hz

def jugada(tablero, posicion, jugador):  
    posicion -= 1  
    fila = posicion // 3  
    columna = posicion % 3  
    ocupado = tablero[fila][columna] in ('X', 'O')  
    if ocupado:  
        return False  
    else:  
        tablero[fila][columna] = jugador  
        sonido_token(jugador)
        return True  

def verificar_ganador(tablero):  
    for fila in tablero:  
        if fila[0] == fila[1] == fila[2] and fila[0] in ('X', 'O'):  
            return fila[0]  
    for col in range(3):  
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] in ('X', 'O'):  
            return tablero[0][col]  
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] in ('X', 'O'):  
        return tablero[0][0]  
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] in ('X', 'O'):  
        return tablero[0][2]  
    return None  

while True:  
    tablero = [row[:] for row in base]  
    jugador = (Player_1, Player_2)  
    contador = 0  

    while True:  
        mostrar_tablero(tablero)  
        print("Juega", jugador[contador % 2], end="")  

        while True:  
            try:  
                posicion = int(input(", Ingrese Posición (1-9): "))  
                if 1 <= posicion <= 9:  
                    break  
                else:  
                    print("Posición no válida. Ingrese un número entre 1 y 9.")  
            except ValueError:  
                print("Entrada no válida. Por favor, ingrese un número.")  

        if jugada(tablero, posicion, jugador[contador % 2]):  
            contador += 1  
            ganador = verificar_ganador(tablero)  
            if ganador:  
                mostrar_tablero(tablero)  
                print(f"¡El jugador {ganador} ha ganado!")  
                if ganador == Player_1:  
                    puntuacion_1 += 1  
                elif ganador == Player_2:  
                    puntuacion_2 += 1  
                print(f"Puntuación actual: PLAYER 1 ({Player_1}): {puntuacion_1}, PLAYER 2 ({Player_2}): {puntuacion_2}")  
                break  
            elif contador == 9:  
                mostrar_tablero(tablero)  
                print("¡Empate! No hay más jugadas posibles.")  
                break  
        else:  
            print("La posición ya está ocupada. Intente de nuevo.")  

    respuesta = input("¿Quieres jugar otra partida? (s/n): ").strip().lower()  
    if respuesta != "s":  
        print("Gracias por jugar. ¡Hasta luego!")  
        print(f"Puntuación final: PLAYER 1 ({Player_1}): {puntuacion_1}, PLAYER 2 ({Player_2}): {puntuacion_2}")  
        break  


import sys
import time
from data_loader import cargar_set_datos_naval


def batalla_naval_greedy(d_filas, d_columnas, barcos):
    n = len(d_filas)
    m = len(d_columnas)
    tablero = [[0] * m for _ in range(n)]
    barcos.sort(reverse=True)

    for barco in barcos:
        ubicado = False

        while not ubicado:
            max_d_fil = max((d, i) for i, d in enumerate(d_filas))
            max_d_col = max((d, j) for j, d in enumerate(d_columnas))
            
            # El barco es mas grande que la demanda
            if max_d_fil[0] < barco and max_d_col[0] < barco:
                break

            if max_d_fil[0] >= max_d_col[0]:
                # Intenta ubicar por fila
                i_fil = max_d_fil[1]
                for i_col in range(m):
                    #if intentar_ubicar_barco(tablero, m, n, barco, i_fil, i_col, True):
                    if intentar_ubicar_barco(tablero, barco, i_fil, i_col, True, d_filas, d_columnas):
                        ubicar_barco(tablero, barco, i_fil, i_col, d_filas, d_columnas, True)
                        ubicado = True
                        break
            else:
                # Intenta ubicar por columna
                i_col = max_d_col[1]
                for i_fil in range(n):
                    #if intentar_ubicar_barco(tablero, m, n, barco, i_fil, i_col, False):
                    if intentar_ubicar_barco(tablero, barco, i_fil, i_col, False, d_filas, d_columnas):
                        ubicar_barco(tablero, barco, i_fil, i_col, d_filas, d_columnas, False)
                        ubicado = True
                        break

            # No se puede ubicar al barco
            if not ubicado:
                break

    return d_filas, d_columnas, tablero

def intentar_ubicar_barco(tablero, barcos, i_fil, i_col, horizontal, d_filas, d_columnas):
    n, m = len(tablero), len(tablero[0])

    # Verificar que el barco no salga del tablero
    if (horizontal and i_col + barcos > m) or (not horizontal and i_fil + barcos > n):
        return False

    # Verificar que no se violen las demandas de fila y columna
    if horizontal:
        if d_filas[i_fil] < barcos:
            return False
        for i in range(barcos):
            if d_columnas[i_col + i] < 1:
                return False
    else:  # Es vertical
        if d_columnas[i_col] < barcos:
            return False
        for i in range(barcos):
            if d_filas[i_fil + i] < 1:
                return False

    # Verificar que no haya barcos adyacentes o superpuestos
    for i in range(barcos):
        fil, col = (i_fil, i_col + i) if horizontal else (i_fil + i, i_col)

        # Revisa que el casillero no esté ocupado por otro barco
        if tablero[fil][col] != 0:
            return False
        
        # Revisa adyacencias (por fila, columna y diagonales)
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            adj_fil, adj_col = fil + dx, col + dy
            if 0 <= adj_fil < n and 0 <= adj_col < m and tablero[adj_fil][adj_col] != 0:
                return False

    # Verificar extremos del barco
    if horizontal:
        # Solo revisar extremos (izquierda y derecha) una vez
        if (i_col > 0 and tablero[i_fil][i_col - 1] != 0) or (i_col + barcos < m and tablero[i_fil][i_col + barcos] != 0):
            return False
    else:  # Es vertical
        # Solo revisar extremos (arriba y abajo) una vez
        if (i_fil > 0 and tablero[i_fil - 1][i_col] != 0) or (i_fil + barcos < n and tablero[i_fil + barcos][i_col] != 0):
            return False

    return True


# Ubica al barco en el tablero, de forma horizontal o vertical.
def ubicar_barco(tablero, barcos, i_fil, i_col, d_filas, d_columnas, horizontal):
    if horizontal:
        for i in range(barcos):
            tablero[i_fil][i_col + i] = 1
            d_columnas[i_col + i] -= 1
        d_filas[i_fil] -= barcos
    else:
        for i in range(barcos):
            tablero[i_fil + i][i_col] = 1
            d_filas[i_fil + i] -= 1
        d_columnas[i_col] -= barcos

# Quita al barco del tablero.
def quitar_barco(tablero, barcos, i_fil, i_col, d_filas, d_columnas, horizontal):
    if horizontal:
        for i in range(barcos):
            tablero[i_fil][i_col + i] = 0
            d_columnas[i_col + i] += 1
        d_filas[i_fil] += barcos
    else:
        for i in range(barcos):
            tablero[i_fil + i][i_col] = 0
            d_filas[i_fil + i] += 1
        d_columnas[i_col] += barcos
     

def imprimir_juego_naval(tablero):
    filas = len(tablero)
    columnas = len(tablero[0]) if filas > 0 else 0

    for i in range(filas):
        # Imprimir los valores de cada celda en la fila
        fila = "  ".join("-" if tablero[i][j] == 0 else str(tablero[i][j]) for j in range(columnas))
        print(fila)
    

if __name__ == "__main__":    
    if len(sys.argv) > 1:
        nombre_archivo = sys.argv[1]
    else:
        nombre_archivo = input("Ingrese el nombre del archivo contenedor de datos: ")

    demanda_filas, demanda_columnas, barcos = cargar_set_datos_naval(nombre_archivo)
    tiempo_inicio = time.time()
    d_filas, d_columnas, tablero_final = batalla_naval_greedy(demanda_filas.copy(), demanda_columnas.copy(), barcos)
    tiempo_final = time.time()

    # demanda cumplida es la suma * 2 de los 1s en el tablero
    demanda_cumplida = sum(sum(fila) for fila in tablero_final) * 2
    demanda_total = sum(demanda_filas) + sum(demanda_columnas)
    imprimir_juego_naval(tablero_final)
    print(f"Demanda cumplida: {demanda_cumplida}")
    print(f"Demanda incumplida: {demanda_total - demanda_cumplida}")
    print(f"Demanda total: {demanda_total}")
    print(f"Tiempo de ejecución: {tiempo_final - tiempo_inicio} segundos")

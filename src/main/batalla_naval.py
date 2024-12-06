import sys, time
from data_loader import cargar_set_datos_naval

D_INCUMPLIDA = 1
TABLERO = 0

def batalla_naval(d_filas, d_columnas, barcos):
    n = len(d_filas)
    m = len(d_columnas)
    tablero = [[0] * m for _ in range(n)]
    barcos.sort(reverse=True)
    solucion = [tablero, float("inf")]
    batalla_naval_bt(tablero, barcos, d_filas, d_columnas, solucion)

    demanda_total = sum(d_filas) + sum(d_columnas)
    demanda_cumplida = demanda_total - solucion[D_INCUMPLIDA]

    return demanda_cumplida, demanda_total, solucion[TABLERO]

def batalla_naval_bt(
    tablero, barcos, d_filas, d_columnas, solucion_parcial
):

    d_incumplida = sum(d_filas) + sum(d_columnas)
    
    if d_incumplida < solucion_parcial[D_INCUMPLIDA]:
        solucion_parcial[TABLERO] = [list(fila) for fila in tablero]
        solucion_parcial[D_INCUMPLIDA] = d_incumplida

    # Caso base
    if not barcos:
        return
    # Poda si solución parcial es peor que la demanda incumplida maxima
    if solucion_parcial[D_INCUMPLIDA] <= d_incumplida - sum(
        barco * 2 for barco in barcos
    ): return

    # Sin barco
    batalla_naval_bt(
        tablero, barcos[1:], d_filas, d_columnas, solucion_parcial
    )

    # Con barco
    for i in range(len(tablero)):
        if d_filas[i] > 0:  # Hay demanda en la fila?
            for j in range(len(tablero[0])):
                if d_columnas[j] > 0:  # Hay demanda en la columna?
                    # Pruebo con barco horizontal y vertical
                    procesar_barco(
                        tablero,
                        barcos,
                        i,
                        j,
                        d_filas,
                        d_columnas,
                        solucion_parcial,
                        True,
                    )
                    procesar_barco(
                        tablero,
                        barcos,
                        i,
                        j,
                        d_filas,
                        d_columnas,
                        solucion_parcial,
                        False,
                    )
    

def procesar_barco(
    tablero,
    barcos,
    i,
    j,
    d_filas,
    d_columnas,
    solucion_parcial,
    horizontal,
):
    if intentar_ubicar_barco(
        tablero, barcos[0], i, j, horizontal, d_filas, d_columnas
    ):
        ubicar_barco(
            tablero, barcos[0], i, j, d_filas, d_columnas, horizontal
        )
        batalla_naval_bt(
            tablero, barcos[1:], d_filas, d_columnas, solucion_parcial
        )
        quitar_barco(
            tablero, barcos[0], i, j, d_filas, d_columnas, horizontal
        )


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
    demanda_cumplida, demanda_total, tablero_final = batalla_naval(demanda_filas.copy(), demanda_columnas.copy(), barcos)
    tiempo_final = time.time()

    imprimir_juego_naval(tablero_final)
    print(f"Demanda cumplida: {demanda_cumplida}")
    print(f"Demanda incumplida: {demanda_total - demanda_cumplida}")
    print(f"Demanda total: {demanda_total}")
    print(f"Tiempo de ejecución: {tiempo_final - tiempo_inicio} segundos")

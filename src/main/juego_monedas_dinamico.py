from collections import deque
import time
from data_loader import cargar_set_datos
import os


def juego_monedas_dinamico(coins):
    n = len(coins)

    opt = [[-1] * n for _ in range(n)]


    for largo_subarreglo in range(1, n + 1):
        for i in range(n - largo_subarreglo + 1):
            j = i + largo_subarreglo - 1  

            # Caso base: una sola moneda.
            if i == j:
                opt[i][j] = coins[i]
            # Caso base: dos monedas
            elif i + 1 == j:
                opt[i][j] = max(coins[i], coins[j])
            else:
                # Sophia elige la moneda de la izquierda. Sophia tiene dos opciones luego entre i+1;j y 
                # i;j-1. Mateo elige la moneda de mayor valor entre i+1 y j o i y j-1.
                sophia_izq_mateo_izq = coins[i] + opt[i+2][j] if coins[i+1] >= coins[j] and i+2 <= j else 0
                sophia_izq_mateo_der = coins[i] + opt[i+1][j-1] if coins[i+1] < coins[j] and i+1 <= j-1 else 0
                opcion_izq = max(sophia_izq_mateo_izq, sophia_izq_mateo_der)
                
                # Sophia elige la moneda de la derecha. Sophia tiene dos opciones luego entre i;j-2 y
                # i+1;j-1. Mateo elige la moneda de mayor valor entre i+1 y j o i y j-1.
                sophia_der_mateo_izq = coins[j] + opt[i][j-2] if coins[i] < coins[j-1] and i <= j-2 else 0
                sophia_der_mateo_der = coins[j] + opt[i+1][j-1] if coins[i] >= coins[j-1] and i+1 <= j-1 else 0
                opcion_der = max(sophia_der_mateo_izq, sophia_der_mateo_der)
                
                opt[i][j] = max(opcion_izq, opcion_der)

    puntaje_sophia = opt[0][n-1]
    puntaje_mateo = sum(coins) - puntaje_sophia

    return puntaje_sophia, puntaje_mateo, reconstruccion(coins, opt)


def reconstruccion(coins, opt):
    elecciones = []
    j = len(coins) - 1
    i = 0

    while i <= j:
        # Obtengo la mejor opcion del lado derecho, la comparo con la mejor opcion. 
        # Si no es la misma, avanzo por la otra opcion.
        sophia_der_mateo_izq = coins[j] + opt[i][j-2] if coins[i] < coins[j-1] and i <= j-2 else 0
        sophia_der_mateo_der = coins[j] + opt[i+1][j-1] if coins[i] >= coins[j-1] and i+1 <= j-1 else 0
        opcion_der = max(sophia_der_mateo_izq, sophia_der_mateo_der)
        
        if opt[i][j] == opcion_der:
            # Se eligió la moneda del lado derecho
            elecciones.append(f"Sophia debe agarrar la ultima ({coins[j]})")
            j -= 1
        else:
            # Se eligió la moneda del lado izquierdo
            elecciones.append(f"Sophia debe agarrar la primera ({coins[i]})")
            i += 1
        
        if i <= j: 
            if coins[i] >= coins[j]:
                elecciones.append(f"Mateo agarra la primera ({coins[i]})")
                i += 1
            else:
                elecciones.append(f"Mateo agarra la ultima ({coins[j]})")
                j -= 1

    return "; ".join(elecciones)




if __name__ == "__main__":

    start_time = time.time()

    dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../segunda-parte-set-datos/20.txt'))
    monedas = cargar_set_datos(dir)

    ganancia_sophia, ganancia_mateo, choices = juego_monedas_dinamico(monedas)

    print("Recuento:")
    print(f"Ganancia Sophia: {ganancia_sophia}")
    print(f"Ganancia Mateo: {ganancia_mateo}")


    print(choices)

    end_time = time.time()
    execution_time = end_time - start_time
    # print(f"Tiempo de ejecución: {execution_time:.6f} segundos")

import sys
import os
from collections import deque

from data_loader import cargar_set_datos

def obtener_mayor_moneda(monedas):
    if monedas[0] > monedas[-1]:
        return monedas.popleft(), "Primera moneda para Sophia"
    else:
        return monedas.pop(), "Ultima moneda para Sophia"

def obtener_menor_moneda(monedas):
    if monedas[0] >= monedas[-1]:
        return monedas.pop(), "Ultima moneda para Mateo"
    else:
        return monedas.popleft(), "Primera moneda para Mateo"

def juego_monedas(monedas):
    solucion = []
    suma_sophia = 0
    suma_mateo = 0
    turno_sophia = True

    monedas = deque(monedas)

    append_solucion = solucion.append  # Local variable for faster access

    append_solucion = solucion.append  # Local variable for faster access
    while monedas:
        if turno_sophia:
            valor_moneda, resultado = obtener_mayor_moneda(monedas)
            suma_sophia += valor_moneda
            append_solucion(resultado)
        else:
            valor_moneda, resultado = obtener_menor_moneda(monedas)
            suma_mateo += valor_moneda
            append_solucion(resultado)
        turno_sophia = not turno_sophia

    return solucion, suma_sophia, suma_mateo

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Debe ingresar la direccion de un archivo de texto")

    dir = sys.argv[1]
    print(dir)
    # Descomentar si no toma los argumentos bien para testear
    # dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../primera-parte-set-datos/25.txt'))
    monedas = cargar_set_datos(dir)
    print("Monedas iniciales")
    print(monedas)

    solucion, suma_sofia, _ = juego_monedas(monedas)

    print(solucion)
    print("Ganancia de Sophia: ", suma_sofia)


    

import sys
from collections import deque
from data_loader import cargar_set_datos


path_datos = "../../primera-parte-set-datos/"

def obtener_mayor_moneda(monedas):
    if monedas[0] > monedas[-1]:
        return monedas.popleft(), "Primera moneda para Sophia"
    else:
        return monedas.pop(), "Última moneda para Sophia"

def obtener_menor_moneda(monedas):
    if monedas[0] >= monedas[-1]:
        return monedas.pop(), "Última moneda para Mateo"
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

    return "; ".join(solucion), suma_sophia, suma_mateo

if __name__ == "__main__":
    nombre_archivo = ""
    
    if len(sys.argv) > 1:
        nombre_archivo = sys.argv[1]
    else:
        nombre_archivo = input("Ingrese el nombre del archivo contenedor de datos: ")

    monedas = cargar_set_datos(nombre_archivo)
    solucion, suma_sofia, suma_mateo = juego_monedas(monedas)

    total_monedas = sum(monedas)

    print(solucion)
    print("Ganancia de Sophia: ", suma_sofia)
    
    assert (
            suma_sofia + suma_mateo == total_monedas
    ),f"la suma de puntajes ({suma_sofia + suma_mateo}) no coincide con el total de las monedas ({total_monedas})."

    assert (
            suma_sofia >= suma_mateo
    ),f"Pierde Sophia con un valor acumulado de: ({suma_sofia}) y el valor acumulado de Mateo ({suma_mateo}) )."
    



    

import sys
import os
import collections

def leer_archivo(dir):
    monedas = []
    try:
        with open(dir, 'r') as archivo:
            lineas = archivo.readlines()
            if len(lineas) >= 2:
            # Seleccionar la segunda línea y quitar el salto de línea al final
                segunda_linea = lineas[1].strip()
                valores = segunda_linea.split(';')
                monedas = [int(num) for num in valores]
        return monedas
    except FileNotFoundError:
        print(f"El archivo {dir} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def juega_sofia(monedas):

    solucion = []
    suma_sofia = 0
    turno = 1

    while monedas:
        if turno % 2 != 0:
            if monedas[0] > monedas[-1]:
                suma_sofia += monedas.pop(0)
                solucion.append("Primera moneda para Sophia")
            else:
                suma_sofia += monedas.pop()
                solucion.append("Ultima moneda para Sophia")
            turno += 1
            continue
        if monedas[0] >= monedas[-1]:
            monedas.pop()
            solucion.append("Ultima moneda para Mateo")
        else:
            monedas.pop(0)
            solucion.append("Primera moneda para Mateo")
        turno += 1

    return solucion, suma_sofia

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Debe ingresar la direccion de un archivo de texto")

    dir = sys.argv[1]
    print(dir)
    # Descomentar si no toma los argumentos bien para testear
    # dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../primera-parte-set-datos/25.txt'))
    monedas = leer_archivo(dir)
    print("Monedas iniciales")
    print(monedas)

    solucion, suma_sofia = juega_sofia(monedas)

    print(solucion)
    print("Ganancia de Sophia: ", suma_sofia)


    

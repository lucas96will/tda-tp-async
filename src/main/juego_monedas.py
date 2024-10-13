import sys

def leer_archivo(dir):
    monedas = []
    try:
        with open(dir, 'r') as archivo:
             for linea in archivo:
                linea = linea.strip()
                # Saltar líneas que comienzan con #
                if linea.startswith('#') or not linea:
                    continue
                # Procesar solo la primera línea válida (que no sea comentario)
                valores = linea.split(';')
                monedas = [int(num) for num in valores]
                break  # Romper el bucle después de la primera línea válida
        return monedas
    except FileNotFoundError:
        print(f"El archivo {dir} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def obtener_mayor_moneda(monedas):
    valor_moneda = 0
    resultado = ""
    if monedas[0] > monedas[-1]:
        valor_moneda = monedas.pop(0)
        resultado = "Primera moneda para Sophia"
    else:
        valor_moneda = monedas.pop()
        resultado = "Ultima moneda para Sophia"
    return valor_moneda, resultado

def obtener_menor_moneda(monedas):
    valor_moneda = 0
    resultado = ""
    if monedas[0] >= monedas[-1]:
        monedas.pop()
        resultado = "Ultima moneda para Mateo"
    else:
        monedas.pop(0)
        resultado = "Primera moneda para Mateo"
    return valor_moneda, resultado

def juego_monedas(monedas):
    solucion = []
    suma_sofia = 0
    turno_sophia = True

    while monedas:
        if turno_sophia:
            valor_moneda, resultado = obtener_mayor_moneda(monedas)
            suma_sofia += valor_moneda
            solucion.append(resultado)
            turno_sophia = not turno_sophia
            continue
        _, resultado = obtener_menor_moneda(monedas)
        solucion.append(resultado)
        turno_sophia = not turno_sophia


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

    solucion, suma_sofia = juego_monedas(monedas)

    print(solucion)
    print("Ganancia de Sophia: ", suma_sofia)


    

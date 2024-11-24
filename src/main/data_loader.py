def cargar_set_datos(dir):
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
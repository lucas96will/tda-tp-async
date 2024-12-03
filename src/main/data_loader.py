def cargar_set_datos(dir):
    monedas = []
    try:
        with open(dir, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                # Saltar líneas que comienzan con #
                if linea.startswith("#") or not linea:
                    continue
                # Procesar solo la primera línea válida (que no sea comentario)
                valores = linea.split(";")
                monedas = [int(num) for num in valores]
                break  # Romper el bucle después de la primera línea válida
        return monedas
    except FileNotFoundError:
        print(f"El archivo {dir} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def cargar_set_datos_naval(dir):
    try:
        with open(dir, "r") as archivo:
            lineas = [
                linea.strip() for linea in archivo if not linea.strip().startswith("#")
            ]

            contenido = "\n".join(lineas)
            secciones = contenido.split("\n\n")

            demanda_filas = [int(x) for x in secciones[0].strip().split("\n")]
            demanda_columnas = [int(x) for x in secciones[1].strip().split("\n")]
            barcos = [int(x) for x in secciones[2].strip().split("\n")]

            filas = len(demanda_filas)
            columnas = len(demanda_columnas)
            return demanda_filas, demanda_columnas, barcos
    except FileNotFoundError:
        print(f"El archivo {dir} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

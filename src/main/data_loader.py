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

def cargar_set_datos_naval(dir):
    try:
        with open(dir, 'r') as archivo:
            # Leer todas las líneas del archivo, eliminando comentarios
            lineas = [linea.strip() for linea in archivo if not linea.strip().startswith("#")]
            
            # Unir las líneas en un solo texto y dividirlo en secciones por líneas en blanco
            contenido = "\n".join(lineas)
            secciones = contenido.split("\n\n")
            
            # Leer las demandas de las filas
            demanda_filas = [int(x) for x in secciones[0].strip().split("\n")]
            
            # Leer las demandas de las columnas
            demanda_columnas = [int(x) for x in secciones[1].strip().split("\n")]
            
            # Leer los largos de los barcos
            barcos = [int(x) for x in secciones[2].strip().split("\n")]
            
            # Crear el tablero con ceros basado en las dimensiones de las demandas
            filas = len(demanda_filas)
            columnas = len(demanda_columnas)
            tablero = [[0] * columnas for _ in range(filas)]
            
            return tablero, demanda_filas, demanda_columnas, barcos
    except FileNotFoundError:
        print(f"El archivo {dir} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
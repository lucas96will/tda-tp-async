import sys
from data_loader import cargar_set_datos_naval


def imprimir_juego_naval(tablero, demanda_filas, demanda_columnas):
    filas = len(tablero)
    columnas = len(tablero[0]) if filas > 0 else 0

    # Imprimir el tablero con las demandas de las filas al final
    for i in range(filas):
        fila = "  ".join("-" for _ in range(columnas))  # Cada celda representada por "-"
        print(f"{fila}  {demanda_filas[i]}")           # Añadir la demanda de la fila al final
    
    # Imprimir las demandas de las columnas en una fila final
    demandas_columnas = "  ".join(str(demanda) for demanda in demanda_columnas)
    print(demandas_columnas)


if __name__ == "__main__":
    nombre_archivo = ""
    
    if len(sys.argv) > 1:
        nombre_archivo = sys.argv[1]
    else:
        nombre_archivo = input("Ingrese el nombre del archivo contenedor de datos: ")

    tablero, demanda_filas, demanda_columnas, barcos = cargar_set_datos_naval(nombre_archivo)
    
    imprimir_juego_naval(tablero, demanda_filas, demanda_columnas)
    
import os
import time
from data_loader import cargar_set_datos_naval
from batalla_naval import batalla_naval
from batalla_naval_greedy import batalla_naval_greedy

def medir_tiempos_tercera_parte_bt(func, archivo_salida):
    # Directorio de los archivos de datos
    dir_datos = "tercera-parte-set-datos"

    # Obtener todos los archivos en el directorio
    archivos = [f for f in os.listdir(dir_datos) if os.path.isfile(os.path.join(dir_datos, f)) and f not in ["Resultados_Esperados_Tablero.txt", "Resultados_Esperados.txt"]]
    with open(archivo_salida, "w") as salida:
        for archivo in archivos:
            # Cargar los datos del archivo
            path_archivo = os.path.join(dir_datos, archivo)
            demanda_filas, demanda_columnas, barcos = cargar_set_datos_naval(path_archivo)

            # Medir el tiempo de ejecución de batalla_naval
            tiempo_inicio = time.perf_counter()
            demanda_cumplida, _, _ = func(demanda_filas.copy(), demanda_columnas.copy(), barcos)
            tiempo_final = time.perf_counter()
            duracion = tiempo_final - tiempo_inicio
            # Escribir los resultados en el archivo de salida
            salida.write(f"Archivo: {archivo}\n")
            salida.write(f"Duración: {duracion:.6f} segundos\n")
            salida.write(f"Demanda cumplida: {demanda_cumplida}\n\n")


def medir_tiempos_tercera_parte_greedy(func, archivo_salida):
    # Directorio de los archivos de datos
    dir_datos = "tercera-parte-set-datos"

    # Obtener todos los archivos en el directorio
    archivos = [f for f in os.listdir(dir_datos) if os.path.isfile(os.path.join(dir_datos, f)) and f not in ["Resultados_Esperados_Tablero.txt", "Resultados_Esperados.txt"]]
    with open(archivo_salida, "w") as salida:
        for archivo in archivos:
            # Cargar los datos del archivo
            path_archivo = os.path.join(dir_datos, archivo)
            demanda_filas, demanda_columnas, barcos = cargar_set_datos_naval(path_archivo)

            # Medir el tiempo de ejecución de batalla_naval
            tiempo_inicio = time.perf_counter()
            _, _, tablero_final = func(demanda_filas.copy(), demanda_columnas.copy(), barcos)
            tiempo_final = time.perf_counter()
            duracion = tiempo_final - tiempo_inicio
            demanda_cumplida = sum(sum(fila) for fila in tablero_final) * 2

            # Escribir los resultados en el archivo de salida
            salida.write(f"Archivo: {archivo}\n")
            salida.write(f"Duración: {duracion:.6f} segundos\n")
            salida.write(f"Demanda cumplida: {demanda_cumplida}\n\n")


if __name__ == "__main__":
    medir_tiempos_tercera_parte_greedy(batalla_naval_greedy, "mediciones_tercera_parte_greedy.txt")
    medir_tiempos_tercera_parte_bt(batalla_naval, "mediciones_tercera_parte.txt")


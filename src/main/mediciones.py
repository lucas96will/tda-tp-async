# Imports necesarios para el notebook
from random import seed
import time

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp
from util import time_algorithm

# Imports de los algoritmos a medir
from juego_monedas import juego_monedas
from juego_monedas_dinamico import juego_monedas_dinamico


def get_random_array(size: int):
    return np.random.randint(1, 100.000, size).tolist()

def mediciones_primera_parte_greedy():
    # Siempre seteamos la seed de aleatoridad para que los # resultados sean reproducibles
    seed(12345)
    np.random.seed(12345)
    sns.set_theme()

    # La variable x van a ser los valores del eje x de los gráficos en todo el notebook
    # Tamaño mínimo=100, tamaño máximo=100.000 , cantidad de puntos=20
    x = np.linspace(100, 100_000, 50).astype(int)

    results_greedy = time_algorithm(juego_monedas, x, lambda s: [get_random_array(s)])

    f_n = lambda x, c1, c2: c1 * x + c2
    f_n2 = lambda x, c1, c2: c1 * x**2 + c2

    c_iter, _ = sp.optimize.curve_fit(f_n, x, [results_greedy[n] for n in x])
    c_n2, _ = sp.optimize.curve_fit(f_n2, x, [results_greedy[n] for n in x])

    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, [results_greedy[n] for n in x], label="Medición")
    ax.plot(x, [f_n(n, c_iter[0], c_iter[1]) for n in x], 'g--', label="Ajuste $n$")
    ax.plot(x, [f_n2(n, c_n2[0], c_n2[1]) for n in x], 'y--', label="Ajuste $n^2$")
    ax.set_title('Tiempo de ejecución de algoritmo greedy')
    ax.set_xlabel('Tamaño del array')
    ax.set_ylabel('Tiempo de ejecución (s)')
    ax.legend()
    None

    plt.show()
    fig.savefig('greedy_complejidad.png')


    errors_n2 = [np.abs(f_n2(n, c_n2[0], c_n2[1]) - results_greedy[n]) for n in x]
    errors_n = [np.abs(f_n(n, c_iter[0], c_iter[1]) - results_greedy[n]) for n in x]

    print(f"Error cuadrático total para n^2: {np.sum(np.power(errors_n2, 2))}")
    print(f"Error cuadrático total para n: {np.sum(np.power(errors_n, 2))}")

    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, errors_n2, 'g-',  label="Ajuste $n^2$")
    ax.plot(x, errors_n, 'y-', label="Ajuste $n$")
    ax.set_title('Error de ajuste')
    ax.set_xlabel('Tamaño del array')
    ax.set_ylabel('Error absoluto (s)')
    ax.legend()
    None

    plt.show()
    fig.savefig('greedy_complejidad_error.png')

def mediciones_segunda_parte_dinamico():
    # Siempre seteamos la seed de aleatoridad para que los # resultados sean reproducibles
    seed(12345)
    np.random.seed(12345)
    sns.set_theme()

    # La variable x van a ser los valores del eje x de los gráficos en todo el notebook
    # Tamaño mínimo=100, tamaño máximo=100.000 , cantidad de puntos=20
    x = np.linspace(100, 2000, 20).astype(int)

    results = time_algorithm(juego_monedas_dinamico, x, lambda s: [get_random_array(s)])

    f_n = lambda x, c1, c2: c1 * x + c2
    f_n2 = lambda x, c1, c2: c1 * x**2 + c2
    f_nlogn = lambda x, c1, c2: c1 * x * np.log(x) + c2 

    c_iter, _ = sp.optimize.curve_fit(f_n, x, [results[n] for n in x])
    c_n2, _ = sp.optimize.curve_fit(f_n2, x, [results[n] for n in x])
    c_nlogn, _ = sp.optimize.curve_fit(f_nlogn, x, [results[n] for n in x])

    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, [results[n] for n in x], label="Medición")
    ax.plot(x, [f_n(n, c_iter[0], c_iter[1]) for n in x], 'g--', label="Ajuste $n$")
    ax.plot(x, [f_n2(n, c_n2[0], c_n2[1]) for n in x], 'y--', label="Ajuste $n^2$")
    ax.plot(x, [f_nlogn(n, c_nlogn[0], c_nlogn[1]) for n in x], 'r--', label=r"Ajuste $n \log(n)$")
    ax.set_title('Tiempo de ejecución de algoritmo dinamico')
    ax.set_xlabel('Tamaño del array')
    ax.set_ylabel('Tiempo de ejecución (s)')
    ax.legend()
    None

    plt.show()
    fig.savefig('dinamico_complejidad.png')

    errors_n2 = [np.abs(f_n2(n, c_n2[0], c_n2[1]) - results[n]) for n in x]
    errors_n = [np.abs(f_n(n, c_iter[0], c_iter[1]) - results[n]) for n in x]
    errors_nlogn = [np.abs(f_nlogn(n, c_nlogn[0], c_nlogn[1]) - results[n]) for n in x]


    print(f"Error cuadrático total para n^2: {np.sum(np.power(errors_n2, 2))}")
    print(f"Error cuadrático total para n: {np.sum(np.power(errors_n, 2))}")
    print(f"Error cuadrático total para nlogn: {np.sum(np.power(errors_nlogn, 2))}")

    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, errors_n2, 'g-',  label="Ajuste $n^2$")
    ax.plot(x, errors_n, 'y-', label="Ajuste $n$")
    ax.plot(x, errors_nlogn, 'r-', label=r"Ajuste $n \log(n)$")
    ax.set_title('Error de ajuste')
    ax.set_xlabel('Tamaño del array')
    ax.set_ylabel('Error absoluto (s)')
    ax.legend()
    None

    plt.show()
    fig.savefig('dinamico_complejidad_error.png')

if __name__ == "__main__":
    start_time = time.time()
    # mediciones_primera_parte_greedy()
    mediciones_segunda_parte_dinamico()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")


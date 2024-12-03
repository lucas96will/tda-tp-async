import unittest
import os
import sys

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the main directory
main_dir = os.path.abspath(os.path.join(current_dir, "../main"))
# Add the main directory to the system path
sys.path.insert(0, main_dir)

from batalla_naval import batalla_naval

class TestBatallaNaval(unittest.TestCase):

    def test_small_board_few_ships(self):
        tablero = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        demanda_filas = [1, 1, 1]
        demanda_columnas = [1, 1, 1]
        barcos = [1, 1, 1]

        demanda_cumplida, demanda_total, tablero_final = batalla_naval(tablero, demanda_filas, demanda_columnas, barcos)

        self.assertEqual(demanda_cumplida, 4)
        self.assertEqual(demanda_total, 6)

    def test_large_board_more_ships(self):
        tablero = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        demanda_filas = [2, 2, 2, 2, 2]
        demanda_columnas = [2, 2, 2, 2, 2]
        barcos = [2, 2, 2, 2, 2]

        demanda_cumplida, demanda_total, tablero_final = batalla_naval(tablero, demanda_filas, demanda_columnas, barcos)
        self.assertEqual(demanda_cumplida, 16)
        self.assertEqual(demanda_total, 20)

    def test_no_ships(self):
        tablero = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        demanda_filas = [1, 1, 1]
        demanda_columnas = [1, 1, 1]
        barcos = []

        demanda_cumplida, demanda_total, tablero_final = batalla_naval(tablero, demanda_filas, demanda_columnas, barcos)

        self.assertEqual(demanda_cumplida, 0)
        self.assertEqual(demanda_total, 6)

    def test_no_demands(self):
        tablero = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        demanda_filas = [0, 0, 0]
        demanda_columnas = [0, 0, 0]
        barcos = [1, 1, 1]

        demanda_cumplida, demanda_total, tablero_final = batalla_naval(tablero, demanda_filas, demanda_columnas, barcos)

        self.assertEqual(demanda_cumplida, 0)
        self.assertEqual(demanda_total, 0)

    def test_too_big_ships_no_demand(self):
        tablero = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        demanda_filas = [3, 3, 3]
        demanda_columnas = [3, 3, 3]
        barcos = [4, 4, 4]

        demanda_cumplida, demanda_total, tablero_final = batalla_naval(tablero, demanda_filas, demanda_columnas, barcos)

        self.assertEqual(demanda_cumplida, 0)
        self.assertEqual(demanda_total, 18)

    def test_ship_correct_but_not_enough_space_with_demand(self):
        tablero = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        demanda_filas = [1, 1, 1]
        demanda_columnas = [1, 1, 1]
        barcos = [3]

        demanda_cumplida, demanda_total, tablero_final = batalla_naval(tablero, demanda_filas, demanda_columnas, barcos)

        self.assertEqual(demanda_cumplida, 0)
        self.assertEqual(demanda_total, 6)


if __name__ == "__main__":
    unittest.main()
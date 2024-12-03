import random
import unittest
import os
import sys


# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the main directory
main_dir = os.path.abspath(os.path.join(current_dir, "../main"))
# Add the main directory to the system path
sys.path.insert(0, main_dir)

from juego_monedas_dinamico import juego_monedas_dinamico


class TestJuegoMonedaDinamico(unittest.TestCase):

    def test_con_8_elementos(self):
        monedas = [8, 10, 4, 5, 7, 4, 3, 9]

        ganancia_esperada = 29
        ganancia_sophia, ganancia_mateo, choices = juego_monedas_dinamico(monedas)
        print("Recuento:")
        print(f"Ganancia Sophia: {ganancia_sophia}")
        print(f"Ganancia Mateo: {ganancia_mateo}")
        print(choices)
        self.assertEqual(ganancia_sophia, ganancia_esperada)


if __name__ == "__main__":
    unittest.main()

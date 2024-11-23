import random
import unittest
import os
import sys


# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the main directory
main_dir = os.path.abspath(os.path.join(current_dir, '../main'))
# Add the main directory to the system path
sys.path.insert(0, main_dir)

from juego_monedas import juego_monedas

class TestJuegoMonedas(unittest.TestCase):
    
    def test_ejemplo_5(self):
        acciones_esperadas = [
            "Primera moneda para Sophia", 
            "Ultima moneda para Mateo", 
            "Ultima moneda para Sophia", # Si las dos son iguales, agarra la ultima
            "Ultima moneda para Mateo", 
            "Ultima moneda para Sophia", # Si solo hay una, agarra la ultima
        ]

        ganancia_esperada = 50+50+50
        
        monedas = [50, 50, 15, 50, 25]

        acciones_obtenidas, ganancia, _ = juego_monedas(monedas)      

        self.assertEqual(acciones_obtenidas, acciones_esperadas)
        self.assertEqual(ganancia, ganancia_esperada)

    def test_siempre_gana_sophia(self):
        random.seed(12345)
        monedas = [random.randint(1, 1000) for _ in range(50)]
        num_sorts = 100  # Número de ordenamientos aleatorios a realizar

        for _ in range(num_sorts):
            random.shuffle(monedas)
            _, suma_sophia, suma_mateo = juego_monedas(monedas)
            self.assertGreaterEqual(suma_sophia, suma_mateo, f"Fallo, suma Mateo mayor a Sophia con monedas: {monedas}")


if __name__ == "__main__":
    unittest.main()
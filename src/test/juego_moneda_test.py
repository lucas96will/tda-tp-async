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
        print(acciones_esperadas)

        ganancia_esperada = 50+50+50
        
        monedas = [50, 50, 15, 50, 25]

        acciones_obtenidas, ganancia = juego_monedas(monedas)      
        print(acciones_obtenidas)

        self.assertEqual(acciones_obtenidas, acciones_esperadas)
        self.assertEqual(ganancia, ganancia_esperada)


if __name__ == "__main__":
    unittest.main()
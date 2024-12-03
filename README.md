# tda-tp-async

## Integrantes

Nombre Apellido, Padron

Lucas Ricardo Williams, 103018

Gaston Proz, 105868

## Requisitos

- Python 3.x

## Instrucciones para ejecutar el programa

1. Clona este repositorio:
   ```bash
   git clone https://github.com/lucas96will/tda-tp-async.git
   cd tda-tp-async
   ```
2. Crea un archivo de texto con los valores de las monedas, alternativamente puedes usar los que se encuentran en primera-parte-set-datos. Tiene que seguir el formato del siguiente ejemplo:
   ```valores_monedas.txt
   72;165;794;892;880;341;882;570;679;725;979;375;459;603;112;436;587;699;681;83
   ```
3. Ejecutar el programa

   ```bash
   El path utilizado toma el root de donde lo ejecutas.

   python src/main/juego_moneda.py "PATH_AL_ARCHIVO"

   Ejecutandolo desde TDA-TP-ASYNC

   Ejemplo primera parte
   python src/main/juego_moneda.py primera-parte-set-datos/25.txt

   Ejemplo segunda parte
   python src/main/juego_moneda_dinamico.py segunda-parte-set-datos/20.txt

   Ejemplo tercera parte
   python src/main/batalla_naval.py tercera-parte-set-datos/5_5_6.txt

   Ejemplo tercera parte
   python src/main/batalla_naval_greedy.py tercera-parte-set-datos/5_5_6.txt
   ```

4. La salida esperada del programa, ejemplo con el set de datos de 25 monedas de la primera parte

   ```
   Última moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo; Última moneda para Sophia; Primera moneda para Mateo; Última moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo; Última moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Primera moneda para Mateo; Primera moneda para Sophia; Primera moneda para Mateo; Última moneda para Sophia; Última moneda para Mateo; Última moneda para Sophia; Primera moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo; Última moneda para Sophia
   Ganancia de Sophia:  9635

   ```

5. Se pueden ver los resultados esperados en los datasets de cada parte.

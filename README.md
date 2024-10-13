# tda-tp-async

## Integrantes

Nombre Apellido, Padron

Lucas Ricardo Williams, 103018

Rodrigo Ladaga, 100188

Gaston Proz, 105868

Nazareno Napolitano, 107910

Ramiro Besse Molina, 110657


# Juego de Monedas

Este juego consiste de "dos" jugadores, Sophia y Mateo, donde seleccionan monedas de una lista, en cada turno se puede elegir entre la primer y ultima moneda. Sophia siempre elige la mayor moneda en su turno, y como Mateo es todavia muy pequeño, Sophia le elige la moneda en su turno, es buena hermana pero como es muy competitiva siempre elige la menor para el pequeño Mateo.

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
    python src/main/juego.py "PATH_AL_ARCHIVO_CON_VALORES_DE_MONEDAS"
    ```
4. La salida esperada del programa, ejemplo con el set de datos de 25 monedas.
    ```
    ['Ultima moneda para Sophia', 'Ultima moneda para Mateo', 'Primera moneda para Sophia', 'Ultima moneda para Mateo', 'Primera moneda para Sophia', 'Ultima moneda para Mateo', 'Ultima moneda para Sophia', 'Primera moneda para Mateo', 'Ultima moneda para Sophia', 'Ultima moneda para Mateo', 'Primera moneda para Sophia', 'Ultima moneda para Mateo', 'Ultima moneda para Sophia', 'Ultima moneda para Mateo', 'Primera moneda para Sophia', 'Primera moneda para Mateo', 'Primera moneda para Sophia', 'Primera moneda para Mateo', 'Ultima moneda para Sophia', 'Ultima moneda para Mateo', 'Ultima moneda para Sophia', 'Primera moneda para Mateo', 'Primera moneda para Sophia', 'Ultima moneda para Mateo', 'Ultima moneda para Sophia']
    Ganancia de Sophia: 9635
    ```
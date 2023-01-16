# Insta Bot

este codigo seguirar y dejara de seguir ususuarios de una base de datos

## Installing

correr `pip install -r requirements.txt`

## Usage

En el archivo keys.py pegar usr y pssw:
- USERNAME = "pepa"
- PASSWORD = "pig123"

1. Editar linea 68 de `conseguir_seguidores.py` con las cuentas de las que quiero conseguir seguidores: **recomendacion** editar con 5-6 cuentas para que dure la base de datos
2. Correr `python conseguir_seguidores.py`  esto creara el archivo historial.txt con los nombres: no volver a correr hasta que el archivo historial.txt tenga menos de 50 lineas
3. Correr `python ir_a_seguir.py` correr 1 vez al dia, dara follow a 10-20 cuentas y guarda los nombres en seguidos.txt
4. Correr `python dejar de seguir.py` correr cuando el archivo seguidos.txt tenga mas de 50 lineas

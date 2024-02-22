# TalanaKombat

Talana Kombat es un juego donde 2 personajes se enfrentan hasta la muerte. Cada personaje tiene 2 golpes especiales que se ejecutan con una combinación de movimientos + 1 botón de golpe. Los botones que se usan son (W)Arriba, (S)Abajo, (A)Izquierda, (D)Derecha, (P)Puño, (K)Patada.

#### Golpes de Nuestros Personajes
- **Tonyn Stallone:**
  - Combinación: DSD + P
  - Energía que quita: 3
  - Nombre del movimiento: Taladoken

  - Combinación: SD + K
  - Energía que quita: 2
  - Nombre del movimiento: Remuyuken

  - Combinación: P o K
  - Energía que quita: 1
  - Nombre del movimiento: Puño o Patada

- **Arnaldor Shuatseneguer:**
  - Combinación: SA + K
  - Energía que quita: 3
  - Nombre del movimiento: Remuyuken

  - Combinación: ASA + P
  - Energía que quita: 2
  - Nombre del movimiento: Taladoken

  - Combinación: P o K
  - Energía que quita: 1
  - Nombre del movimiento: Puño o Patada

#### Información Importante
- Parte atacando el jugador que envió una combinación menor de botones (movimiento + golpes).
- En caso de empate, parte el con menos movimientos, si empatan de nuevo, inicia el con menos golpes, si hay empate de nuevo, inicia el player 1 (total el player 2 siempre es del hermano chico).
- La secuencia completa del combate de cada jugador se entrega de una vez (consolidada en un JSON).
- Cada personaje tiene 6 Puntos de energía.
- Un personaje muere cuando su energía llega a 0 y de inmediato finaliza la pelea.
- Tony es el player 1, siempre ataca hacia la derecha (y no cambia de lado).
- Arnaldor es el player 2, siempre ataca hacia la izquierda (y no cambia de lado).
- Los personajes se atacan uno a la vez estilo JRPG, por turnos hasta que uno es derrotado, los golpes no pueden ser bloqueados, se asume que siempre son efectivos.

#### Datos de Entrada
Los datos llegan como un JSON con botones de movimiento y golpe que se correlacionan para cada jugada. Los movimientos pueden ser un string de largo máximo 5 (puede ser vacío), y los golpes pueden ser un solo botón máximo (puede ser vacío). Se asume que el botón de golpe es justo después de la secuencia de movimiento, es decir, AADSD + P es un Taladoken (antes se movió para atrás 2 veces); DSDAA + P son movimientos más un puño.

### Desarrollo de la Solución
Desarrolla una solución que relate la pelea e informe el resultado final. Asegúrate de seguir las condiciones y restricciones del desafío.


### Ejecución con python 3.9
```bash
python main.py --file-json peleas/file.json
python main.py --json '{"player1":{"movimientos":["SDD", "DSD", "SA", "DSD"] ,"golpes":["K", "P", "K", "P"]},
"player2":{"movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],"golpes":["P", "K", "K", "K", "P",
"K"]}}'
```

### Ejecución de las pruebas 
```bash
python -m unittest discover -s test -p "*.py"
```

### Ejecución con docker
```bash
docker build -t nombre_de_tu_imagen .
docker run nombre_de_tu_imagen  --file-json peleas/file.json
docker run nombre_de_tu_imagen  --json_args '{"player1":{"movimientos":["SDD", "DSD", "SA", "DSD"] ,"golpes":["K", "P", "K", "P"]},
"player2":{"movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],"golpes":["P", "K", "K", "K", "P",
"K"]}}'
```
### Error comunes
```bash
# Errors should never pass silently.
docker run nombre_de_tu_imagen  --json_args '{"player1":{"movimientos":["S", "D"] ,"golpes":["K", "P"]},
"player2":{"movimientos":["DSD", "WSAW"],"golpes":["P", "p"]}}'

# Las validaciones  son sencibles ala mayuculas y minusculas 
Error: Los movimientos s en 'player1' deben ser cadenas de máximo 5 caracteres y solo pueden contener (W), (S), (A) o (D) en mayúsculas.
Error: Los golpes en 'player2' deben ser cadenas de un solo carácter, o solo (P) o (K) en mayúsculas.

```

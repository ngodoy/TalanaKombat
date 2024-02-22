import argparse

from src.utils import read_json, validate_kombat_json, parse_json
from src.characters import TonynStallone, ArnaldorShuatseneguer
from src.kombat import CombatArena


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Un script simple de Python con argumentos de línea de comandos.')
    parser.add_argument('--json_args', type=parse_json, default='', help='JSON específico')
    parser.add_argument('--file-json', type=str, default='', help='Ruta a un archivo JSON específico')
    args = parser.parse_args()

    if not args.json_args and not args.file_json:
        parser.error('Se debe proporcionar uno de --json o --file-json.')

    if args.json_args and args.file_json:
        parser.error('--json o --file-json son mutuamente excluentes')

    if args.file_json:
        # Handle args.file_json
        file_json = args.file_json
        json_args = read_json(file_json)
    else:
        # Handle args.json_args
        json_args = args.json_args

    print()

    if validate_kombat_json(json_args):
        tony = TonynStallone(json_args["player1"]["movimientos"], json_args["player1"]["golpes"])
        arnaldor = ArnaldorShuatseneguer(json_args["player2"]["movimientos"], json_args["player2"]["golpes"])
        combat_arena = CombatArena(tony, arnaldor)
        combat_arena.run()

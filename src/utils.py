import json
import re
import argparse
from typing import List


def read_json(file_path: str) -> dict:
    """
    This method reads a JSON file and returns the data as a dictionary.

    :param file_path: Path of the JSON file to read.
    :type file_path: str
    :returns: Data from the JSON file as a dictionary.
    :rtype: dict
    """
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


def parse_json(json_str):
    if not json_str:
        return None
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise argparse.ArgumentTypeError(f"Invalid JSON format: {e}")


def is_valid_movement(player: str, movement: str) -> bool:
    """
    Validates the movements of a player in the Talana Kombat JRPG game.

    :param player: The player's identifier (e.g., "player1", "player2").
    :type player: str
    :param movement: The player's movement sequence.
    :type movement: str
    :return: True if the movements are valid, False otherwise.
    :rtype: bool
    """
    # Regular expression to check if it is a string with a maximum of 5 characters
    max_5_chars_regex = re.compile(r'^.{0,5}$')

    # Regular expression to check if it is an empty string or contains only uppercase W, S, A, D
    only_WSAD_regex = re.compile(r'^[WSAD]*$')
    condition = only_WSAD_regex.match(movement) and 0 <= len(movement) <= 5
    if not condition:
        print(
            f"Error: Los movimientos {movement} en '{player}' deben ser cadenas de máximo 5 caracteres y solo pueden contener (W), (S), (A) o (D) en mayúsculas.")
        return False
    return True


def is_valid_strike(player: str, strike: str) -> bool:
    """
    Validates the strikes of a player in the Talana Kombat JRPG game.

    :param player: The player's identifier (e.g., "player1", "player2").
    :type player: str
    :param strike: The player's strike sequence.
    :type strike: str
    :return: True if the strikes are valid, False otherwise.
    :rtype: bool
    """
    # Regular expression to check if it is a string with a maximum of 1 character,
    # an empty string, or contains only uppercase P or K
    strike_regex = re.compile(r'^(|[PK]{1})$')

    # Conditions using the combined regular expression
    if not strike_regex.match(strike):
        print(
            f"Error: Los golpes en '{player}' deben ser cadenas de un solo carácter, o solo (P) o (K) en mayúsculas.")
        return False

    return True


def validate_movements(player: str, movements: List[str]) -> bool:
    """
    Validate movements for a player.

    :param player: Player name.
    :param movements: List of movements.
    :return: True if all movements are valid, False otherwise.
    """
    return all(is_valid_movement(player, movement) for movement in movements)


def validate_strikes(player: str, strikes: List[str]) -> bool:
    """
    Validate strikes for a player.

    :param player: Player name.
    :param strikes: List of strikes.
    :return: True if all strikes are valid, False otherwise.
    """
    return all(is_valid_strike(player, strike) for strike in strikes)


def validate_player_data(player: str, data: dict) -> bool:
    """
    Validate player data.

    :param player: Player name.
    :param player_data: Dictionary containing player data.
    :return: True if player data is valid, False otherwise.
    """
    players_secuencia = ["movimientos", "golpes"]

    if player not in data:
        print(f"Error: Falta la key '{player}' en el diccionario.")
        return False

    player_data = data.get(player, {})
    if not all(key in player_data for key in players_secuencia):
        print(f"Error: Falta una o ambas key 'movimientos' y 'golpes' en '{player}'.")
        return False

    movements = player_data.get("movimientos", [])
    strikes = player_data.get("golpes", [])

    return validate_movements(player, movements) and validate_strikes(player, strikes)


def validate_kombat_json(data: dict) -> bool:
    """
    Validates the structure and content of a JSON data representing a Talana Kombat JRPG game.

    :param data: The JSON data to be validated.
    :type data: dict
    :return: True if the JSON data is valid, False otherwise.
    :rtype: bool
    """
    players = ["player1", "player2"]
    for player in players:
        if not validate_player_data(player, data):
            return False
    return True

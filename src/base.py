import re
import copy
from typing import List, Dict, Union
from itertools import zip_longest
from .utils import validate_movements, validate_strikes


def has_index(my_list, index):
    """
    Checks if a specific index exists in a list.

    Args:
        my_list (list): The list to check the index in.
        index (int): The index to check.

    Returns:
        tuple: A tuple indicating whether the index exists and the value at that index.
               The first element is a boolean indicating existence, and the second element is the value
               at the specified index. If the index does not exist, the second element is set to None.
    """
    try:
        value_at_index = my_list[index]
        return True, value_at_index
    except IndexError:
        return False, None


class BaseCharacter:
    """
    Base class representing a character in the Talana Kombat JRPG game.
    """

    energy: int = 6
    name: str = 'BaseCharacter'
    tag: str = 'player_tag'
    order: int

    punches_base: Dict[str, Dict[str, Union[str, int]]] = {
        "P": {"nombre": "un Puño", "energia": 1},
        "K": {"nombre": "una Patada", "energia": 1}
    }

    punches_combo: Dict[str, Dict[str, Union[str, int]]] = {}

    movements: Dict[str, str] = {
        "W": "Arriba", "S": "Abajo", "A": "Izquierda", "D": "Derecha"
    }

    def __init__(self, movements_sequence: List[str], strikes_sequence: List[str]):
        """
        Initializes a character with sequences of movements and strikes.

        :param movements_sequence: Sequence of movements for the character.
        :type movements_sequence: List[str]
        :param strikes_sequence: Sequence of strikes for the character.
        :type strikes_sequence: List[str]
        """

        self.punches_combo.update(self.punches_base)
        self._movements_sequence = movements_sequence
        self._strikes_sequence = strikes_sequence
        self.combo_sequence_energy = self.get_combo_sequence_energy()

    @property
    def movements_sequence(self) -> List[str]:
        """
        Gets the sequence of movements for the character.

        :return: Sequence of movements for the character.
        :rtype: List[str]
        """

        return self._movements_sequence

    @movements_sequence.setter
    def movements_sequence(self, value: List[str]) -> None:
        """
        Sets the sequence of movements for the character.

        :param value: New sequence of movements.
        :type value: List[str]
        """
        validate_movements(player=self.tag, movements=value)
        self._movements_sequence = value

    @property
    def strikes_sequence(self) -> List[str]:
        """
        Gets the sequence of strikes for the character.

        :return: Sequence of strikes for the character.
        :rtype: List[str]
        """

        return self._strikes_sequence

    @strikes_sequence.setter
    def strikes_sequence(self, value: List[str]) -> None:
        """
        Sets the sequence of strikes for the character.

        :param value: New sequence of strikes.
        :type value: List[str]
        """
        validate_strikes(player=self.tag, strikes=value)
        self._strikes_sequence = value

    def is_alive(self) -> bool:
        """
        Checks if the character is alive.

        :return: True if the character is alive, False otherwise.
        :rtype: bool
        """
        return self.energy > 0

    def get_combo_sequence(self) -> List[str]:
        """
        Gets the combination of movements and strikes for the character.

        :return: Combination of movements and strikes for the character.
        :rtype: List[str]
        """

        combo_sequence = list(
            map(''.join,
                zip_longest(self.movements_sequence, self.strikes_sequence, fillvalue='')
                )
        )

        return combo_sequence

    def get_combo_sequence_energy(self):
        """
        Gets the combination of movements and strikes with energy information for the character.

        :return: Combination of movements and strikes with energy information for the character.
        :rtype: dict
        """

        pattern = "|".join(re.escape(key) for key in self.punches_combo.keys())

        combo_sequence_energy = {}
        for index, item in enumerate(self.get_combo_sequence()):
            match = re.search(pattern, item)
            if match:
                dict_flag = copy.copy(self.punches_combo.get(match.group()))
                exists, value = has_index(self.movements_sequence, index)
                name_flag = self.movements.get(value, "")

                if exists and name_flag:
                    dict_flag["nombre"] = f"{name_flag} y da {dict_flag['nombre']}"
                else:
                    dict_flag["nombre"] = f"conecta {dict_flag['nombre']}"

                combo_sequence_energy[item] = dict_flag
            else:
                combo_sequence_energy[item] = {'nombre': self.movements.get(item, "se mueve"), 'energia': 0}

        return combo_sequence_energy

    def narration(self):
        """
        Narrates the character's action.

        :return: Energy associated with the performed action.
        :rtype: int
        """

        movement_element = self.movements_sequence.pop(0) if self.movements_sequence else ""
        strike_element = self.strikes_sequence.pop(0) if self.strikes_sequence else ""
        if movement_element or strike_element:
            print(f"➢ {self} {self.combo_sequence_energy.get(movement_element + strike_element)['nombre']}")
            return self.combo_sequence_energy.get(movement_element + strike_element)['energia']
        return 0

    def __str__(self):
        """
        Returns a string representation of the character.

        :return: String representation of the character.
        :rtype: str
        """

        return f"{self.name}"

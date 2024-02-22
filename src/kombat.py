from typing import Optional
from typing import Tuple

from src.characters import *


# Calculate priority of the players
def cal_total_buttons(moves_strikes: list[str]) -> int:
    """
    This function calculates how many buttons a player used.
    Args:
      moves (list[str]): The moves of the player.
      strikes (list[str]): The punches of the player.
    Returns:
      total_buttons (int): The total buttons of the player used.
      :param moves_strikes:
    """
    buttons = "".join(moves_strikes)
    return len(buttons)


def define_winner(first_player: BaseCharacter, second_player: BaseCharacter) -> Optional[BaseCharacter]:
    """
     Defines the winner of the combat according to the established rules.

     :param first_player: Player 1.
     :param second_player: Player 2.
     :return: The winning character or None in case of a tie.
     :rtype: Optional[BaseCharacter]
    """
    if first_player.is_alive() and not second_player.is_alive():
        return first_player
    elif not first_player.is_alive() and second_player.is_alive():
        return second_player
    elif first_player.energy > second_player.energy:
        return first_player
    elif first_player.energy < second_player.energy:
        return second_player
    else:
        return None


class CombatArena:

    def __init__(self, player1: BaseCharacter, player2: BaseCharacter):
        self.player1 = player1
        self.player2 = player2

    def run(self):
        first_player, second_player = self.define_start()
        self.simulate_combat(first_player, second_player)

    def define_start(self) -> Tuple[BaseCharacter, BaseCharacter]:
        """
        Defines the beginning of the fight according to the established rules. Attacks are initiated by the player
        who inputs a lesser combination of buttons (movement + strikes). In the event of a tie, the one with fewer
        movements starts, and if they tie again, the one with fewer strikes starts. If there is still a tie,
        Player 1 initiates (overall, Player 2 always starts if there is a tie).

        :return: Tuple with characters in the order of starting.
        :rtype: tuple
        """

        first_player1 = (self.player1, self.player2)
        first_player2 = (self.player2, self.player1)

        total_buttons_player1 = cal_total_buttons(self.player1.movements_sequence + self.player1.strikes_sequence)
        total_buttons_player2 = cal_total_buttons(self.player2.movements_sequence + self.player2.strikes_sequence)

        if total_buttons_player1 < total_buttons_player2:
            return first_player1
        elif total_buttons_player2 < total_buttons_player1:
            return first_player2

        total_movements_player1 = cal_total_buttons(self.player1.movements_sequence)
        total_movements_player2 = cal_total_buttons(self.player2.movements_sequence)

        if total_movements_player1 < total_movements_player2:
            return first_player1
        elif total_movements_player2 < total_buttons_player2:
            return first_player2

        total_strikes_player1 = cal_total_buttons(self.player1.strikes_sequence)
        total_strikes_player2 = cal_total_buttons(self.player2.strikes_sequence)

        if total_strikes_player1 < total_strikes_player2:
            return first_player1
        elif total_strikes_player2 < total_strikes_player1:
            return first_player2

        return first_player1

    def simulate_combat(self, first_player: BaseCharacter, second_player: BaseCharacter) -> None:
        """
        Simulates a combat between two characters.

        :param first_player: Player 1.
        :param second_player: Player 2.
        """
        max_turns = max(len(first_player.movements_sequence), len(second_player.movements_sequence))
        for i in range(max_turns):
            if not first_player.is_alive() or not second_player.is_alive():
                break

            energy = first_player.narration()
            second_player.energy -= energy
            if second_player.is_alive():
                energy = second_player.narration()
                first_player.energy -= energy

        winner = define_winner(first_player, second_player)

        if winner is not None:
            print(f"{winner} gana la pelea y le queda {winner.energy} de energía")
        else:
            print(f"{first_player} y {second_player} quedan empatados con {second_player.energy} de energía")

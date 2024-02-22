import unittest

from src.base import BaseCharacter


class TestBaseCharacter(unittest.TestCase):
    def setUp(self):
        # Set up a sample BaseCharacter instance for testing
        movements_sequence = ["WASD", "S"]
        strikes_sequence = ["P", "K"]
        self.character = BaseCharacter(movements_sequence, strikes_sequence)
        self.character.name = "BaseCharacter"

    def test_is_alive(self):
        # Test if the character is initially alive
        self.assertTrue(self.character.is_alive())

        # Set character's energy to 0 and test if it's not alive
        self.character.energy = 0
        self.assertFalse(self.character.is_alive())

    def test_get_combo_sequence(self):
        # Test if the combo sequence is generated correctly
        expected_combo_sequence = ['WASDP', 'SK']
        self.assertEqual(self.character.get_combo_sequence(), expected_combo_sequence)

    def test_get_combo_sequence_energy(self):
        # Test if the combo sequence with energy information is generated correctly
        expected_combo_sequence_energy = {
            'WASDP': {'nombre': 'conecta un Puño', 'energia': 1},
            'SK': {'nombre': 'Abajo y da una Patada', 'energia': 1}
        }
        self.assertEqual(self.character.get_combo_sequence_energy(), expected_combo_sequence_energy)

    def test_narration(self):
        # Test if narracion prints the expected message and returns the correct energy
        expected_output = "➢ BaseCharacter Up and performs a Punch"
        self.assertEqual(self.character.narration(), 1)
        self.assertEqual(self.character.narration(), 1)
        self.assertEqual(self.character.narration(), 0)  # Narration for the second action (no output)

    def test_str(self):
        # Test if __str__ returns the correct string representation
        expected_str = "BaseCharacter"
        self.assertEqual(str(self.character), expected_str)


if __name__ == '__main__':
    unittest.main()

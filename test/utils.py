import unittest

from src.utils import is_valid_movement, is_valid_strike, validate_kombat_json


class TestKombatValidation(unittest.TestCase):

    def test_is_valid_movement(self):
        # Valid movements
        self.assertTrue(is_valid_movement("player1", "WASD"))
        self.assertTrue(is_valid_movement("player2", "SD"))
        # Invalid movements
        self.assertFalse(is_valid_movement("player1", "XYZ"))
        self.assertFalse(is_valid_movement("player2", "WASDX"))
        self.assertFalse(is_valid_movement("player1", "WSADXYZ"))

    def test_is_valid_strike(self):
        # Valid strikes
        self.assertTrue(is_valid_strike("player1", "P"))
        self.assertTrue(is_valid_strike("player2", "K"))
        self.assertTrue(is_valid_strike("player1", ""))
        # Invalid strikes
        self.assertFalse(is_valid_strike("player2", "PK"))
        self.assertFalse(is_valid_strike("player1", "xyz"))
        self.assertFalse(is_valid_strike("player1", "PKxyz"))

    def test_validate_kombat_json(self):
        # Valid data
        valid_data = {
            "player1": {"movimientos": ["WASD", "S"], "golpes": ["P", "K"]},
            "player2": {"movimientos": ["WSAD", "SA"], "golpes": ["K", "P"]}
        }

        # Invalid data
        invalid_data_missing_keys = {
            "player1": {"movimientos": ["XYZ", "WASD"], "golpes": ["P", "K"]},
            "player3": {"movimientos": ["WSAD", "SA"], "golpes": ["K", "P"]}
        }

        invalid_data_invalid_movements = {
            "player1": {"movimientos": ["XYZ", "WASDXYZ"], "golpes": ["P", "K"]},
            "player2": {"movimientos": ["WSAD", "SA"], "golpes": ["K", "P"]}
        }

        invalid_data_invalid_strikes = {
            "player1": {"movimientos": ["WASD", "S"], "golpes": ["PK", "XYZ"]},
            "player2": {"movimientos": ["WSAD", "SA"], "golpes": ["K", "P"]}
        }

        self.assertTrue(validate_kombat_json(valid_data))
        self.assertFalse(validate_kombat_json(invalid_data_missing_keys))
        self.assertFalse(validate_kombat_json(invalid_data_invalid_movements))
        self.assertFalse(validate_kombat_json(invalid_data_invalid_strikes))


if __name__ == '__main__':
    unittest.main()

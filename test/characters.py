import unittest

from src.characters import TonynStallone, ArnaldorShuatseneguer


class TestCharacters(unittest.TestCase):
    def setUp(self):
        # Set up instances of TonynStallone and ArnaldorShuatseneguer for testing
        self.tonyn = TonynStallone(["WASD", "S"], ["P", "K"])
        self.arnaldor = ArnaldorShuatseneguer(["AS", "D"], ["K", "P"])

    def test_tonyn_initialization(self):
        # Test TonynStallone character initialization
        self.assertEqual(self.tonyn.name, "Tonyn")
        self.assertEqual(self.tonyn.tag, "player1")
        self.assertEqual(self.tonyn.punches_combo["DSDP"]["energia"], 3)
        self.assertEqual(self.tonyn.punches_combo["SDK"]["nombre"], "un Remuyuken")

    def test_arnaldor_initialization(self):
        # Test ArnaldorShuatseneguer character initialization
        self.assertEqual(self.arnaldor.name, "Arnaldor")
        self.assertEqual(self.arnaldor.tag, "player2")
        self.assertEqual(self.arnaldor.punches_combo["SAK"]["energia"], 3)
        self.assertEqual(self.arnaldor.punches_combo["ASAP"]["nombre"], "un Taladoken")

    def test_tonyn_narration(self):
        # Test TonynStallone character narration
        expected_output = "➢ Tonyn se mueve y da un Puño"
        self.assertEqual(self.tonyn.narration(), 1)
        self.assertEqual(self.tonyn.narration(), 1)  # Narration for the second action (no output)

    def test_arnaldor_narration(self):
        # Test ArnaldorShuatseneguer character narration
        expected_output = "➢ Arnaldor se mueve y da una Patada"
        self.assertEqual(self.arnaldor.narration(), 1)
        self.assertEqual(self.arnaldor.narration(), 1)  # Narration for the second action (no output)

    def test_str_representation(self):
        # Test string representation of characters
        self.assertEqual(str(self.tonyn), "Tonyn")
        self.assertEqual(str(self.arnaldor), "Arnaldor")

    def test_combo_sequence_energy(self):
        # Test generation of combo sequence with energy information
        tonyn_combo_energy = self.tonyn.get_combo_sequence_energy()
        arnaldor_combo_energy = self.arnaldor.get_combo_sequence_energy()

        self.assertEqual(tonyn_combo_energy["WASDP"]["nombre"], "conecta un Puño")
        self.assertEqual(arnaldor_combo_energy["ASK"]["energia"], 1)


if __name__ == '__main__':
    unittest.main()

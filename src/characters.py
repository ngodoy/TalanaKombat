from .base import BaseCharacter


class TonynStallone(BaseCharacter):
    name = "Tonyn"
    tag = "player1"

    punches_combo = {
        "DSDP": {"nombre": "un Taladoken", "energia": 3},
        "SDK": {"nombre": "un Remuyuken", "energia": 2}
    }


class ArnaldorShuatseneguer(BaseCharacter):
    name = "Arnaldor"
    tag = "player2"

    punches_combo = {
        "SAK": {"nombre": "un Remuyuken", "energia": 3, },
        "ASAP": {"nombre": "un Taladoken", "energia": 2}
    }

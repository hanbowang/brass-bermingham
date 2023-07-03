from __future__ import annotations
from enum import Enum

class Industry(Enum):
    COTTON = 1
    MANUFACTURER = 2
    POTTERY = 3
    BREWRY = 4
    COAL = 5
    IRON = 6


class Resource(Enum):
    COAL = 1
    IRON = 2
    BEER = 3
    MONEY = 4

class Era(Enum):
    CANAL = 1
    RAIL = 2
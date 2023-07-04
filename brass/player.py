from __future__ import annotations
from enum import Enum

class Player:
    def __init__(self, name:str) -> None:
        self.name = name
        self.tiles = None
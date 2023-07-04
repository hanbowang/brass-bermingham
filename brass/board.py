from __future__ import annotations
from enum import Enum

from brass.location import create_all_locations

class GameBoard:
    def __init__(self, num_players:int) -> None:
        self.num_players = num_players
        self.locations = create_all_locations()




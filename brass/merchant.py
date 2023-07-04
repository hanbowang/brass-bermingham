from __future__ import annotations
from enum import Enum

from brass.common import Industry

class BeerBonus(Enum):
    DEVELOP = 1 # Remove 1 of the lowest level tiles of any industry from your Player Mat (for no iron cost).  
    INCOME = 2  # Advance your Income Marker 2 spaces along the Progress Track.
    VICTORY = 3 # Advance your VP Marker along the Progress Track by the number of spaces indicated.
    MONEY = 4   # Receive £5 from the Bank.

class Merchant:
    def __init__(self, industries:set[Industry], beer_bonus:BeerBonus) -> None:
        self.industries = industries
        self.beer_bonus = beer_bonus
        self.beer = False
from __future__ import annotations
from enum import Enum

from brass.common import Industry
from brass.common import Resource
from brass.common import Era

class TileState(Enum):
    UNBUILT = 1
    UNFLIPPED = 2
    FLIPPED = 3
    REMOVED = 4

class Tile:
    def __init__(self, industry:Industry, level:int, victory_point:int, income:int, link_multiplier:int, cost:dict, beer_consumption:int, remaining_resource:int=0, era:Era=None) -> None:
        self.industry = industry
        self.level = level
        self.victory_point = victory_point
        self.income = income
        self.link_multiplier = link_multiplier
        self.cost = cost
        self.beer_consumption = beer_consumption
        self.remaining_resource = remaining_resource
        self.era = era
        self.state = TileState.UNBUILT

def create_cotton_tiles() -> list[Tile]:
    tiles = []
    cotton_level_4 = Tile(
        industry=Industry.COTTON,
        level=4,
        victory_point=12,
        income=2,
        link_multiplier=1,
        cost={Resource.COAL: 1, Resource.IRON: 1, Resource.MONEY: 18},
        beer_consumption=1
    )

    cotton_level_3 = Tile(
        industry=Industry.COTTON,
        level=3,
        victory_point=9,
        income=3,
        link_multiplier=1,
        cost={Resource.COAL: 1, Resource.IRON: 1, Resource.MONEY: 16},
        beer_consumption=1
    )

    cotton_level_2 = Tile(
        industry=Industry.COTTON,
        level=2,
        victory_point=5,
        income=4,
        link_multiplier=2,
        cost={Resource.COAL: 1, Resource.MONEY: 14},
        beer_consumption=1
    )

    cotton_level_1 = Tile(
        industry=Industry.COTTON,
        level=1,
        victory_point=5,
        income=6,
        link_multiplier=1,
        cost={Resource.MONEY: 12},
        beer_consumption=1,
        era=Era.CANAL
    )

    tiles.append(cotton_level_4)
    tiles.append(cotton_level_3)
    tiles.append(cotton_level_2)
    tiles.append(cotton_level_1)

    return tiles
from __future__ import annotations
from enum import Enum

from brass.common import Industry

# class Color(Enum):
#     BLUE = 1
#     TEAL = 2
#     YELLOW = 3
#     BROWN = 4
#     PURPLE = 5


class LinkType(Enum):
    RAIL = 1
    CANAL = 2

class BeerBonus(Enum):
    DEVELOP = 1
    INCOME = 2
    VICTORY = 3
    MONEY = 4

class GameBoard:
    def __init__(self) -> None:
        pass

class Space:
    def __init__(self, industries:list[Industry]) -> None:
        self.industries = industries
        self.tile = None

class Merchant:
    def __init__(self, industries:set[Industry], beer_bonus:BeerBonus) -> None:
        self.industries = industries
        self.beer_bonus = beer_bonus
        self.beer = False
        

class Line:
    def __init__(self, connected_locations:list[Location], allowed_link_types: set[LinkType]) -> None:
        self.connected_locations = connected_locations
        self.allowed_link_types = allowed_link_types


class Location:
    def __init__(self, name:str) -> None:
        self.name = name
        self.lines = []

    def add_line(self, line:Line):
        self.lines.append(line)

class RegularLocation(Location):
    def __init__(self, name:str, spaces:list[Space]=[]) -> None:
        super().__init__(name)
        self.spaces = spaces


class MarketLocation(Location):
    def __init__(self, name:str, merchants:list[Merchant]=[]) -> None:
        super().__init__(name)
        self.merchants = merchants

class FarmBrewryLocation(RegularLocation):
    def __init__(self) -> None:
        super().__init__(None, [Space(Industry.BREWRY)])


def connect(connected_locations:list[Location], allowed_link_types: set[LinkType]):
    line = Line(connected_locations, allowed_link_types)
    for location in connected_locations:
        location.add_line(line)


redditch = RegularLocation(
    name='redditch',
    spaces=[
        Space([Industry.MANUFACTURER, Industry.COAL]),
        Space([Industry.IRON])
    ]
)

birmingham = RegularLocation(
    name='birmingham',
    spaces=[
        Space([Industry.COTTON, Industry.MANUFACTURER]),
        Space([Industry.MANUFACTURER]),
        Space([Industry.IRON]),
        Space([Industry.MANUFACTURER])
    ]
)

connect([redditch, birmingham], {LinkType.RAIL})

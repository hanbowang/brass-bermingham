from __future__ import annotations
from enum import Enum


class Color(Enum):
    BLUE = 1
    TEAL = 2
    YELLOW = 3
    BROWN = 4
    PURPLE = 5

class Industry(Enum):
    COTTON = 1
    MANUFACTURER = 2
    POTTERY = 3
    BREWRY = 4
    COAL = 5
    IRON = 6

class LinkType(Enum):
    RAIL = 1
    CANAL = 2

class GameBoard:
    def __init__(self) -> None:
        pass

class Space:
    def __init__(self, industries:list[Industry]) -> None:
        self.industries = industries


class Line:
    def __init__(self, location_left:Location, location_right:Location, allowed_link_types: set[LinkType]) -> None:
        self.location_left = location_left
        self.location_right = location_right
        self.allowed_link_types = allowed_link_types


class Location:
    def __init__(self, color:Color, name:str, spaces:list[Space]) -> None:
        self.color = color
        self.name = name
        self.spaces = spaces


redditch = Location(
    color=Color.PURPLE,
    name='redditch',
    spaces=[
        Space([Industry.MANUFACTURER, Industry.COAL]),
        Space([Industry.IRON])
    ]
)


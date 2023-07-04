from __future__ import annotations
from enum import Enum

from brass.common import Industry
from brass.merchant import Merchant

# class Color(Enum):
#     BLUE = 1
#     TEAL = 2
#     YELLOW = 3
#     BROWN = 4
#     PURPLE = 5

class LOCATION_NAME(Enum):
    # Regular
    WORCHESTER = 1
    KIDDERMINSTER = 2
    DUDLEY = 3
    COALBROOKDALE = 4
    WOLVERHAMPTON = 5
    REDDITCH = 6
    BIRMINGHAM = 7
    COVENTRY = 8
    NUNEATON = 9
    STAFFORD = 10
    WALSALL = 11
    TAMWORTH = 12
    CANNOCK = 13
    BURTON_ON_TRENT = 14
    DERBY = 15
    BELPER = 16
    UTTOXETER = 17
    STONE = 18
    STOKE_ON_TRENT = 19
    LEEK = 20
    # Market
    SHREWSBURY = 21
    GLOUCESTER = 22
    OXFORD = 23
    NOTTINGHAM = 24
    WARRINGTON = 25
    # Farm Brewery
    CANNOCK_FARM_BREWERY = 26
    KIDDERMINSTER_WORCHESTER_FARM_BREWERY = 27


class LinkType(Enum):
    RAIL = 1
    CANAL = 2

class GameBoard:
    def __init__(self) -> None:
        pass

class Space:
    def __init__(self, industries:list[Industry]) -> None:
        self.industries = industries
        self.tile = None
        

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
    def __init__(self, name:str, spaces:list[Space]) -> None:
        super().__init__(name)
        self.spaces = spaces


class MarketLocation(Location):
    def __init__(self, name:str, merchants:list[Merchant]) -> None:
        super().__init__(name)
        self.merchants = merchants

class FarmBrewryLocation(RegularLocation):
    def __init__(self) -> None:
        super().__init__(None, [Space(Industry.BREWERY)])


def connect(connected_locations:list[Location], allowed_link_types: set[LinkType]):
    line = Line(connected_locations, allowed_link_types)
    for location in connected_locations:
        location.add_line(line)


def create_all_locations() -> dict[LOCATION_NAME, Location]:
    all_locations = {
        LOCATION_NAME.REDDITCH: RegularLocation(
            name='redditch',
            spaces=[
                Space([Industry.MANUFACTURER, Industry.COAL]),
                Space([Industry.IRON])
            ]
        ),

        LOCATION_NAME.BIRMINGHAM: RegularLocation(
            name='birmingham',
            spaces=[
                Space([Industry.COTTON, Industry.MANUFACTURER]),
                Space([Industry.MANUFACTURER]),
                Space([Industry.IRON]),
                Space([Industry.MANUFACTURER])
            ]
        ),

        LOCATION_NAME.COVENTRY: RegularLocation(
            name='coventry',
            spaces=[
                Space([Industry.POTTERY],),
                Space([Industry.MANUFACTURER, Industry.COAL]),
                Space([Industry.IRON, Industry.MANUFACTURER])
            ]
        ),

        LOCATION_NAME.NUNEATON: RegularLocation(
            name='nuneaton',
            spaces=[
                Space([Industry.BREWERY, Industry.MANUFACTURER]),
                Space([Industry.COTTON, Industry.COAL])
            ]
        ),

        LOCATION_NAME.WORCHESTER: RegularLocation(
            name='worchester',
            spaces=[
                Space([Industry.COTTON]),
                Space([Industry.COTTON])
            ]
        ),

        LOCATION_NAME.KIDDERMINSTER: RegularLocation(
            name='kidderminster',
            spaces=[
                Space([Industry.COTTON]),
                Space([Industry.COTTON, Industry.COAL])
            ]
        ),

        LOCATION_NAME.DUDLEY: RegularLocation(
            name='dudley',
            spaces=[
                Space([Industry.COAL]),
                Space([Industry.IRON])
            ]
        ),

        LOCATION_NAME.COALBROOKDALE: RegularLocation(
            name='coalbrookdale',
            spaces=[
                Space([Industry.IRON, Industry.BREWERY]),
                Space([Industry.IRON]),
                Space([Industry.COAL])
            ]
        ),
        
        LOCATION_NAME.WOLVERHAMPTON: RegularLocation(
            name='wolverhampton',
            spaces=[
                Space([Industry.MANUFACTURER]),
                Space([Industry.MANUFACTURER, Industry.COAL])
            ]
        ),

        LOCATION_NAME.WALSALL: RegularLocation(
            name='walsall',
            spaces=[
                Space([Industry.MANUFACTURER, Industry.IRON]),
                Space([Industry.MANUFACTURER, Industry.BREWERY])
            ]
        ),

        LOCATION_NAME.TAMWORTH: RegularLocation(
            name='tamworth',
            spaces=[
                Space([Industry.COTTON, Industry.COAL]),
                Space([Industry.COTTON, Industry.COAL])
            ]
        ),

        LOCATION_NAME.CANNOCK: RegularLocation(
            name='cannock',
            spaces=[
                Space([Industry.COAL]),
                Space([Industry.COAL, Industry.MANUFACTURER])
            ]
        ),

        LOCATION_NAME.STAFFORD: RegularLocation(
            name='stafford',
            spaces=[
                Space([Industry.POTTERY]),
                Space([Industry.MANUFACTURER, Industry.BREWERY])
            ]
        ),

        LOCATION_NAME.BURTON_ON_TRENT: RegularLocation(
            name='burton-on-trent',
            spaces=[
                Space([Industry.BREWERY]),
                Space([Industry.MANUFACTURER, Industry.COAL])
            ]
        ),

        LOCATION_NAME.DERBY: RegularLocation(
            name='derby',
            spaces=[
                Space([Industry.MANUFACTURER, Industry.COTTON]),
                Space([Industry.COTTON, Industry.BREWERY]),
                Space([Industry.IRON])
            ]
        ),

        LOCATION_NAME.BELPER: RegularLocation(
            name='belper',
            spaces=[
                Space([Industry.COTTON, Industry.MANUFACTURER]),
                Space([Industry.COAL]),
                Space([Industry.POTTERY])
            ]
        ),

        LOCATION_NAME.UTTOXETER: RegularLocation(
            name='uttoxeter',
            spaces=[
                Space([Industry.MANUFACTURER, Industry.BREWERY]),
                Space([Industry.COTTON, Industry.BREWERY])
            ]
        ),

        LOCATION_NAME.STONE: RegularLocation(
            name='stone',
            spaces=[
                Space([Industry.COTTON, Industry.BREWERY]),
                Space([Industry.MANUFACTURER, Industry.COAL])
            ]
        ),

        LOCATION_NAME.STOKE_ON_TRENT: RegularLocation(
            name='stoke-on-trent',
            spaces=[
                Space([Industry.POTTERY, Industry.IRON]),
                Space([Industry.COTTON, Industry.MANUFACTURER]),
                Space([Industry.MANUFACTURER])
            ]
        ),

        LOCATION_NAME.LEEK: RegularLocation(
            name='leek',
            spaces=[
                Space([Industry.COTTON, Industry.MANUFACTURER]),
                Space([Industry.COTTON, Industry.COAL])
            ]
        )
    }

    connect([all_locations[LOCATION_NAME.REDDITCH], all_locations[LOCATION_NAME.BIRMINGHAM]], {LinkType.RAIL})

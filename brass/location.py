from __future__ import annotations
from enum import Enum

from brass.common import Industry
from brass.merchant import Merchant
from brass.tile import IndustryTile
from brass.player import Player

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

class Space:
    def __init__(self, industries:list[Industry]) -> None:
        self.industries = industries
        self.tile:IndustryTile = None

class Location:
    def __init__(self, name:str) -> None:
        self.name: str = name
        self.lines: list[Line] = []

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


class Line:
    def __init__(self, connected_locations:list[Location], allowed_link_types: set[LinkType]) -> None:
        self.connected_locations = connected_locations
        self.allowed_link_types = allowed_link_types
        self.built_player:Player = None


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
        ),

        LOCATION_NAME.KIDDERMINSTER_WORCHESTER_FARM_BREWERY: FarmBrewryLocation(),
        LOCATION_NAME.CANNOCK_FARM_BREWERY: FarmBrewryLocation(),

        LOCATION_NAME.SHREWSBURY: MarketLocation(),
        LOCATION_NAME.WARRINGTON: MarketLocation(),
        LOCATION_NAME.NOTTINGHAM: MarketLocation(),
        LOCATION_NAME.OXFORD: MarketLocation(),
        LOCATION_NAME.GLOUCESTER: MarketLocation()
    }

    _connect_all_locations(all_locations)


def _connect(connected_locations:list[Location], allowed_link_types: set[LinkType]):
    line = Line(connected_locations, allowed_link_types)
    for location in connected_locations:
        location.add_line(line)

def _connect_all_locations(all_locations) -> None:
    _connect([all_locations[LOCATION_NAME.REDDITCH], all_locations[LOCATION_NAME.BIRMINGHAM]], {LinkType.RAIL})
    _connect([all_locations[LOCATION_NAME.BIRMINGHAM], all_locations[LOCATION_NAME.COVENTRY]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.BIRMINGHAM], all_locations[LOCATION_NAME.WALSALL]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.BIRMINGHAM], all_locations[LOCATION_NAME.NUNEATON]], {LinkType.RAIL})
    _connect([all_locations[LOCATION_NAME.BIRMINGHAM], all_locations[LOCATION_NAME.TAMWORTH]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.BIRMINGHAM], all_locations[LOCATION_NAME.DUDLEY]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.BIRMINGHAM], all_locations[LOCATION_NAME.WORCHESTER]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.COVENTRY], all_locations[LOCATION_NAME.NUNEATON]], {LinkType.RAIL})
    _connect([all_locations[LOCATION_NAME.NUNEATON], all_locations[LOCATION_NAME.TAMWORTH]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.WORCHESTER], all_locations[LOCATION_NAME.KIDDERMINSTER], all_locations[LOCATION_NAME.KIDDERMINSTER_WORCHESTER_FARM_BREWERY]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.KIDDERMINSTER], all_locations[LOCATION_NAME.DUDLEY]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.KIDDERMINSTER], all_locations[LOCATION_NAME.COALBROOKDALE]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.DUDLEY], all_locations[LOCATION_NAME.WOLVERHAMPTON]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.COALBROOKDALE], all_locations[LOCATION_NAME.WOLVERHAMPTON]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.WOLVERHAMPTON], all_locations[LOCATION_NAME.WALSALL]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.WOLVERHAMPTON], all_locations[LOCATION_NAME.CANNOCK]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.WALSALL], all_locations[LOCATION_NAME.TAMWORTH]], {LinkType.RAIL})
    _connect([all_locations[LOCATION_NAME.WALSALL], all_locations[LOCATION_NAME.CANNOCK]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.WALSALL], all_locations[LOCATION_NAME.BURTON_ON_TRENT]], {LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.TAMWORTH], all_locations[LOCATION_NAME.BURTON_ON_TRENT]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.CANNOCK], all_locations[LOCATION_NAME.CANNOCK_FARM_BREWERY]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.CANNOCK], all_locations[LOCATION_NAME.STAFFORD]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.CANNOCK], all_locations[LOCATION_NAME.BURTON_ON_TRENT]], {LinkType.RAIL})
    _connect([all_locations[LOCATION_NAME.BURTON_ON_TRENT], all_locations[LOCATION_NAME.DERBY]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.BURTON_ON_TRENT], all_locations[LOCATION_NAME.STONE]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.DERBY], all_locations[LOCATION_NAME.BELPER]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.DERBY], all_locations[LOCATION_NAME.UTTOXETER]], {LinkType.RAIL})
    _connect([all_locations[LOCATION_NAME.BELPER], all_locations[LOCATION_NAME.LEEK]], {LinkType.RAIL})
    _connect([all_locations[LOCATION_NAME.UTTOXETER], all_locations[LOCATION_NAME.STONE]], {LinkType.RAIL})
    _connect([all_locations[LOCATION_NAME.STONE], all_locations[LOCATION_NAME.STOKE_ON_TRENT]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.STOKE_ON_TRENT], all_locations[LOCATION_NAME.LEEK]], {LinkType.RAIL, LinkType.CANAL})

    # Markets
    _connect([all_locations[LOCATION_NAME.GLOUCESTER], all_locations[LOCATION_NAME.WORCHESTER]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.GLOUCESTER], all_locations[LOCATION_NAME.REDDITCH]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.OXFORD], all_locations[LOCATION_NAME.REDDITCH]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.OXFORD], all_locations[LOCATION_NAME.BIRMINGHAM]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.SHREWSBURY], all_locations[LOCATION_NAME.COALBROOKDALE]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.WARRINGTON], all_locations[LOCATION_NAME.STOKE_ON_TRENT]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LOCATION_NAME.NOTTINGHAM], all_locations[LOCATION_NAME.DERBY]], {LinkType.RAIL, LinkType.CANAL})

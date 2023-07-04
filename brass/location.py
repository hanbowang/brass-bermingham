from __future__ import annotations
from enum import Enum

from brass.common import Industry
from brass.merchant import Merchant
from brass.tile import IndustryTile
from brass.player import Player

class LocationName(Enum):
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
    def __init__(self, name:str) -> None:
        super().__init__(name)
        self.merchants = None

class FarmBrewryLocation(RegularLocation):
    def __init__(self) -> None:
        super().__init__(None, [Space(Industry.BREWERY)])


class Line:
    def __init__(self, connected_locations:list[Location], allowed_link_types: set[LinkType]) -> None:
        self.connected_locations = connected_locations
        self.allowed_link_types = allowed_link_types
        self.built_player:Player = None


def create_all_locations() -> dict[LocationName, Location]:
    all_locations = {
        LocationName.REDDITCH: RegularLocation(
            name='redditch',
            spaces=[
                Space([Industry.MANUFACTURER, Industry.COAL]),
                Space([Industry.IRON])
            ]
        ),

        LocationName.BIRMINGHAM: RegularLocation(
            name='birmingham',
            spaces=[
                Space([Industry.COTTON, Industry.MANUFACTURER]),
                Space([Industry.MANUFACTURER]),
                Space([Industry.IRON]),
                Space([Industry.MANUFACTURER])
            ]
        ),

        LocationName.COVENTRY: RegularLocation(
            name='coventry',
            spaces=[
                Space([Industry.POTTERY],),
                Space([Industry.MANUFACTURER, Industry.COAL]),
                Space([Industry.IRON, Industry.MANUFACTURER])
            ]
        ),

        LocationName.NUNEATON: RegularLocation(
            name='nuneaton',
            spaces=[
                Space([Industry.BREWERY, Industry.MANUFACTURER]),
                Space([Industry.COTTON, Industry.COAL])
            ]
        ),

        LocationName.WORCHESTER: RegularLocation(
            name='worchester',
            spaces=[
                Space([Industry.COTTON]),
                Space([Industry.COTTON])
            ]
        ),

        LocationName.KIDDERMINSTER: RegularLocation(
            name='kidderminster',
            spaces=[
                Space([Industry.COTTON]),
                Space([Industry.COTTON, Industry.COAL])
            ]
        ),

        LocationName.DUDLEY: RegularLocation(
            name='dudley',
            spaces=[
                Space([Industry.COAL]),
                Space([Industry.IRON])
            ]
        ),

        LocationName.COALBROOKDALE: RegularLocation(
            name='coalbrookdale',
            spaces=[
                Space([Industry.IRON, Industry.BREWERY]),
                Space([Industry.IRON]),
                Space([Industry.COAL])
            ]
        ),
        
        LocationName.WOLVERHAMPTON: RegularLocation(
            name='wolverhampton',
            spaces=[
                Space([Industry.MANUFACTURER]),
                Space([Industry.MANUFACTURER, Industry.COAL])
            ]
        ),

        LocationName.WALSALL: RegularLocation(
            name='walsall',
            spaces=[
                Space([Industry.MANUFACTURER, Industry.IRON]),
                Space([Industry.MANUFACTURER, Industry.BREWERY])
            ]
        ),

        LocationName.TAMWORTH: RegularLocation(
            name='tamworth',
            spaces=[
                Space([Industry.COTTON, Industry.COAL]),
                Space([Industry.COTTON, Industry.COAL])
            ]
        ),

        LocationName.CANNOCK: RegularLocation(
            name='cannock',
            spaces=[
                Space([Industry.COAL]),
                Space([Industry.COAL, Industry.MANUFACTURER])
            ]
        ),

        LocationName.STAFFORD: RegularLocation(
            name='stafford',
            spaces=[
                Space([Industry.POTTERY]),
                Space([Industry.MANUFACTURER, Industry.BREWERY])
            ]
        ),

        LocationName.BURTON_ON_TRENT: RegularLocation(
            name='burton-on-trent',
            spaces=[
                Space([Industry.BREWERY]),
                Space([Industry.MANUFACTURER, Industry.COAL])
            ]
        ),

        LocationName.DERBY: RegularLocation(
            name='derby',
            spaces=[
                Space([Industry.MANUFACTURER, Industry.COTTON]),
                Space([Industry.COTTON, Industry.BREWERY]),
                Space([Industry.IRON])
            ]
        ),

        LocationName.BELPER: RegularLocation(
            name='belper',
            spaces=[
                Space([Industry.COTTON, Industry.MANUFACTURER]),
                Space([Industry.COAL]),
                Space([Industry.POTTERY])
            ]
        ),

        LocationName.UTTOXETER: RegularLocation(
            name='uttoxeter',
            spaces=[
                Space([Industry.MANUFACTURER, Industry.BREWERY]),
                Space([Industry.COTTON, Industry.BREWERY])
            ]
        ),

        LocationName.STONE: RegularLocation(
            name='stone',
            spaces=[
                Space([Industry.COTTON, Industry.BREWERY]),
                Space([Industry.MANUFACTURER, Industry.COAL])
            ]
        ),

        LocationName.STOKE_ON_TRENT: RegularLocation(
            name='stoke-on-trent',
            spaces=[
                Space([Industry.POTTERY, Industry.IRON]),
                Space([Industry.COTTON, Industry.MANUFACTURER]),
                Space([Industry.MANUFACTURER])
            ]
        ),

        LocationName.LEEK: RegularLocation(
            name='leek',
            spaces=[
                Space([Industry.COTTON, Industry.MANUFACTURER]),
                Space([Industry.COTTON, Industry.COAL])
            ]
        ),

        LocationName.KIDDERMINSTER_WORCHESTER_FARM_BREWERY: FarmBrewryLocation(),
        LocationName.CANNOCK_FARM_BREWERY: FarmBrewryLocation(),

        LocationName.SHREWSBURY: MarketLocation(name='shrewsbury'),
        LocationName.WARRINGTON: MarketLocation(name='warrington'),
        LocationName.NOTTINGHAM: MarketLocation(name='nottingham'),
        LocationName.OXFORD: MarketLocation(name='oxford'),
        LocationName.GLOUCESTER: MarketLocation(name='gloucester'),
    }

    _connect_all_locations(all_locations)


def _connect(connected_locations:list[Location], allowed_link_types: set[LinkType]):
    line = Line(connected_locations, allowed_link_types)
    for location in connected_locations:
        location.add_line(line)

def _connect_all_locations(all_locations) -> None:
    _connect([all_locations[LocationName.REDDITCH], all_locations[LocationName.BIRMINGHAM]], {LinkType.RAIL})
    _connect([all_locations[LocationName.BIRMINGHAM], all_locations[LocationName.COVENTRY]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.BIRMINGHAM], all_locations[LocationName.WALSALL]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.BIRMINGHAM], all_locations[LocationName.NUNEATON]], {LinkType.RAIL})
    _connect([all_locations[LocationName.BIRMINGHAM], all_locations[LocationName.TAMWORTH]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.BIRMINGHAM], all_locations[LocationName.DUDLEY]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.BIRMINGHAM], all_locations[LocationName.WORCHESTER]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.COVENTRY], all_locations[LocationName.NUNEATON]], {LinkType.RAIL})
    _connect([all_locations[LocationName.NUNEATON], all_locations[LocationName.TAMWORTH]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.WORCHESTER], all_locations[LocationName.KIDDERMINSTER], all_locations[LocationName.KIDDERMINSTER_WORCHESTER_FARM_BREWERY]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.KIDDERMINSTER], all_locations[LocationName.DUDLEY]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.KIDDERMINSTER], all_locations[LocationName.COALBROOKDALE]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.DUDLEY], all_locations[LocationName.WOLVERHAMPTON]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.COALBROOKDALE], all_locations[LocationName.WOLVERHAMPTON]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.WOLVERHAMPTON], all_locations[LocationName.WALSALL]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.WOLVERHAMPTON], all_locations[LocationName.CANNOCK]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.WALSALL], all_locations[LocationName.TAMWORTH]], {LinkType.RAIL})
    _connect([all_locations[LocationName.WALSALL], all_locations[LocationName.CANNOCK]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.WALSALL], all_locations[LocationName.BURTON_ON_TRENT]], {LinkType.CANAL})
    _connect([all_locations[LocationName.TAMWORTH], all_locations[LocationName.BURTON_ON_TRENT]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.CANNOCK], all_locations[LocationName.CANNOCK_FARM_BREWERY]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.CANNOCK], all_locations[LocationName.STAFFORD]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.CANNOCK], all_locations[LocationName.BURTON_ON_TRENT]], {LinkType.RAIL})
    _connect([all_locations[LocationName.BURTON_ON_TRENT], all_locations[LocationName.DERBY]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.BURTON_ON_TRENT], all_locations[LocationName.STONE]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.DERBY], all_locations[LocationName.BELPER]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.DERBY], all_locations[LocationName.UTTOXETER]], {LinkType.RAIL})
    _connect([all_locations[LocationName.BELPER], all_locations[LocationName.LEEK]], {LinkType.RAIL})
    _connect([all_locations[LocationName.UTTOXETER], all_locations[LocationName.STONE]], {LinkType.RAIL})
    _connect([all_locations[LocationName.STONE], all_locations[LocationName.STOKE_ON_TRENT]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.STOKE_ON_TRENT], all_locations[LocationName.LEEK]], {LinkType.RAIL, LinkType.CANAL})

    # Markets
    _connect([all_locations[LocationName.GLOUCESTER], all_locations[LocationName.WORCHESTER]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.GLOUCESTER], all_locations[LocationName.REDDITCH]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.OXFORD], all_locations[LocationName.REDDITCH]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.OXFORD], all_locations[LocationName.BIRMINGHAM]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.SHREWSBURY], all_locations[LocationName.COALBROOKDALE]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.WARRINGTON], all_locations[LocationName.STOKE_ON_TRENT]], {LinkType.RAIL, LinkType.CANAL})
    _connect([all_locations[LocationName.NOTTINGHAM], all_locations[LocationName.DERBY]], {LinkType.RAIL, LinkType.CANAL})

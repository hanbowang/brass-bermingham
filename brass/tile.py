from __future__ import annotations
from enum import Enum

from brass.common import Industry
from brass.common import Resource
from brass.common import Era
from brass.player import Player

class TileState(Enum):
    UNBUILT = 1
    UNFLIPPED = 2
    FLIPPED = 3
    REMOVED = 4

class IndustryTile:
    def __init__(
            self,
            player: Player,
            industry:Industry,
            level:int,
            victory_point:int,
            income:int,
            link_multiplier:int,
            cost:dict,
            beer_consumption:int=0,
            max_resource:dict=None,
            era:Era=None,
            can_be_developed:bool=True
    ) -> None:
        self.player = player
        self.industry = industry
        self.level = level
        self.victory_point = victory_point
        self.income = income
        self.link_multiplier = link_multiplier
        self.cost = cost
        self.beer_consumption = beer_consumption
        self.max_resource = max_resource
        self.era = era
        self.can_be_developed = can_be_developed
        self.state = TileState.UNBUILT

def create_cotton_tiles(player: Player) -> list[IndustryTile]:
    cotton_level_4 = IndustryTile(
        player=player,
        industry=Industry.COTTON,
        level=4,
        victory_point=12,
        income=2,
        link_multiplier=1,
        cost={Resource.COAL: 1, Resource.IRON: 1, Resource.MONEY: 18},
        beer_consumption=1
    )

    cotton_level_3 = IndustryTile(
        player=player,
        industry=Industry.COTTON,
        level=3,
        victory_point=9,
        income=3,
        link_multiplier=1,
        cost={Resource.COAL: 1, Resource.IRON: 1, Resource.MONEY: 16},
        beer_consumption=1
    )

    cotton_level_2 = IndustryTile(
        player=player,
        industry=Industry.COTTON,
        level=2,
        victory_point=5,
        income=4,
        link_multiplier=2,
        cost={Resource.COAL: 1, Resource.MONEY: 14},
        beer_consumption=1
    )

    cotton_level_1 = IndustryTile(
        player=player,
        industry=Industry.COTTON,
        level=1,
        victory_point=5,
        income=6,
        link_multiplier=1,
        cost={Resource.MONEY: 12},
        beer_consumption=1,
        era=Era.CANAL
    )
    tiles = [cotton_level_4, cotton_level_3, cotton_level_2, cotton_level_1]

    return tiles

def create_coal_tiles(player:Player) -> list[IndustryTile]:
    coal_level_4 = IndustryTile(
        player=player,
        industry=Industry.COAL,
        level=4,
        victory_point=4,
        income=5,
        link_multiplier=1,
        cost={Resource.IRON: 1, Resource.MONEY: 10},
        max_resource={
            Era.CANAL: 5,
            Era.RAIL: 5
        }
    )
    coal_level_3 = IndustryTile(
        player=player,
        industry=Industry.COAL,
        level=3,
        victory_point=3,
        income=6,
        link_multiplier=1,
        cost={Resource.IRON: 1, Resource.MONEY: 8},
        max_resource={
            Era.CANAL: 4,
            Era.RAIL: 4
        }
    )
    coal_level_2 = IndustryTile(
        player=player,
        industry=Industry.COAL,
        level=2,
        victory_point=2,
        income=7,
        link_multiplier=1,
        cost={Resource.MONEY: 7},
        max_resource={
            Era.CANAL: 3,
            Era.RAIL: 3
        }
    )
    coal_level_1 = IndustryTile(
        player=player,
        industry=Industry.COAL,
        level=1,
        victory_point=1,
        income=4,
        link_multiplier=2,
        cost={Resource.MONEY: 5},
        max_resource={
            Era.CANAL: 2,
            Era.RAIL: 2
        },
        era=Era.CANAL
    )
    tiles = [coal_level_4, coal_level_3, coal_level_2, coal_level_1]
    return tiles

def create_iron_tiles(player:Player) -> list[IndustryTile]:
    iron_level_4 = IndustryTile(
        player=player,
        industry=Industry.IRON,
        level=4,
        victory_point=9,
        income=1,
        link_multiplier=1,
        cost={Resource.COAL: 1, Resource.MONEY: 12},
        max_resource={
            Era.CANAL: 6,
            Era.RAIL: 6
        }
    )
    iron_level_3 = IndustryTile(
        player=player,
        industry=Industry.IRON,
        level=3,
        victory_point=7,
        income=2,
        link_multiplier=1,
        cost={Resource.COAL: 1, Resource.MONEY: 9},
        max_resource={
            Era.CANAL: 5,
            Era.RAIL: 5
        }
    )
    iron_level_2 = IndustryTile(
        player=player,
        industry=Industry.IRON,
        level=2,
        victory_point=5,
        income=3,
        link_multiplier=1,
        cost={Resource.COAL: 1, Resource.MONEY: 7},
        max_resource={
            Era.CANAL: 4,
            Era.RAIL: 4
        }
    )
    iron_level_1 = IndustryTile(
        player=player,
        industry=Industry.IRON,
        level=1,
        victory_point=3,
        income=3,
        link_multiplier=1,
        cost={Resource.COAL: 1, Resource.MONEY: 5},
        max_resource={
            Era.CANAL: 4,
            Era.RAIL: 4
        },
        era=Era.CANAL
    )
    tiles = [iron_level_4, iron_level_3, iron_level_2, iron_level_1]
    return tiles

def create_brewery_tiles(player:Player) -> list[IndustryTile]:
    brewery_level_4 = IndustryTile(
        player=player,
        industry=Industry.BREWERY,
        level=4,
        victory_point=10,
        income=5,
        link_multiplier=2,
        cost={Resource.IRON: 1, Resource.MONEY: 9},
        max_resource={
            Era.CANAL: 1,
            Era.RAIL: 2
        },
        era=Era.RAIL
    )

    brewery_level_3 = IndustryTile(
        player=player,
        industry=Industry.BREWERY,
        level=3,
        victory_point=7,
        income=5,
        link_multiplier=2,
        cost={Resource.IRON: 1, Resource.MONEY: 9},
        max_resource={
            Era.CANAL: 1,
            Era.RAIL: 2
        }
    )

    brewery_level_2 = IndustryTile(
        player=player,
        industry=Industry.BREWERY,
        level=2,
        victory_point=5,
        income=5,
        link_multiplier=2,
        cost={Resource.IRON: 1, Resource.MONEY: 7},
        max_resource={
            Era.CANAL: 1,
            Era.RAIL: 2
        }
    )

    brewery_level_1 = IndustryTile(
        player=player,
        industry=Industry.BREWERY,
        level=1,
        victory_point=4,
        income=4,
        link_multiplier=2,
        cost={Resource.IRON: 1, Resource.MONEY: 5},
        max_resource={
            Era.CANAL: 1,
            Era.RAIL: 1
        },
        era=Era.CANAL
    )

    tiles = [brewery_level_4, brewery_level_3, brewery_level_2, brewery_level_1]
    return tiles

def create_manufacturer_tiles(player:Player) -> list[IndustryTile]:
    manufacture_level_8 = IndustryTile(
        player=player,
        industry=Industry.MANUFACTURER,
        level=8,
        victory_point=11,
        income=1,
        link_multiplier=1,
        cost={Resource.IRON: 2, Resource.MONEY: 20},
        beer_consumption=1
    )

    manufacture_level_7 = IndustryTile(
        player=player,
        industry=Industry.MANUFACTURER,
        level=7,
        victory_point=9,
        income=4,
        link_multiplier=0,
        cost={Resource.COAL: 1, Resource.IRON: 1, Resource.MONEY: 16},
        beer_consumption=0
    )

    manufacture_level_6 = IndustryTile(
        player=player,
        industry=Industry.MANUFACTURER,
        level=6,
        victory_point=7,
        income=6,
        link_multiplier=1,
        cost={Resource.MONEY: 20},
        beer_consumption=1
    )

    manufacture_level_5 = IndustryTile(
        player=player,
        industry=Industry.MANUFACTURER,
        level=5,
        victory_point=8,
        income=2,
        link_multiplier=2,
        cost={Resource.COAL: 1, Resource.MONEY: 16},
        beer_consumption=2
    )

    manufacture_level_4 = IndustryTile(
        player=player,
        industry=Industry.MANUFACTURER,
        level=4,
        victory_point=3,
        income=6,
        link_multiplier=1,
        cost={Resource.IRON: 1, Resource.MONEY: 8},
        beer_consumption=1
    )

    manufacture_level_3 = IndustryTile(
        player=player,
        industry=Industry.MANUFACTURER,
        level=3,
        victory_point=4,
        income=4,
        link_multiplier=0,
        cost={Resource.COAL: 2, Resource.MONEY: 12},
        beer_consumption=0
    )

    manufacture_level_2 = IndustryTile(
        player=player,
        industry=Industry.MANUFACTURER,
        level=2,
        victory_point=5,
        income=1,
        link_multiplier=1,
        cost={Resource.IRON: 1, Resource.MONEY: 10},
        beer_consumption=1
    )

    manufacture_level_1 = IndustryTile(
        player=player,
        industry=Industry.MANUFACTURER,
        level=1,
        victory_point=3,
        income=5,
        link_multiplier=2,
        cost={Resource.COAL: 1, Resource.MONEY: 8},
        beer_consumption=1,
        era=Era.CANAL
    )

    tiles = [manufacture_level_8, manufacture_level_7, manufacture_level_6, manufacture_level_5, manufacture_level_4, manufacture_level_3, manufacture_level_2, manufacture_level_1]
    return tiles

def create_pottery_tiles(player:Player) -> list[IndustryTile]:
    pottery_level_5 = IndustryTile(
        player=player,
        industry=Industry.POTTERY,
        level=5,
        victory_point=20,
        income=5,
        link_multiplier=1,
        cost={Resource.COAL: 2, Resource.MONEY: 24},
        beer_consumption=2,
        era=Era.RAIL
    )

    pottery_level_4 = IndustryTile(
        player=player,
        industry=Industry.POTTERY,
        level=4,
        victory_point=1,
        income=1,
        link_multiplier=1,
        cost={Resource.COAL: 1},
        beer_consumption=1
    )

    pottery_level_3 = IndustryTile(
        player=player,
        industry=Industry.POTTERY,
        level=3,
        victory_point=11,
        income=5,
        link_multiplier=1,
        cost={Resource.COAL: 2, Resource.MONEY: 22},
        can_be_developed=False,
        beer_consumption=2
    )

    pottery_level_2 = IndustryTile(
        player=player,
        industry=Industry.POTTERY,
        level=2,
        victory_point=1,
        income=1,
        link_multiplier=1,
        cost={Resource.COAL: 1},
        beer_consumption=1
    )

    pottery_level_1 = IndustryTile(
        player=player,
        industry=Industry.POTTERY,
        level=1,
        victory_point=10,
        income=5,
        link_multiplier=1,
        cost={Resource.IRON: 1, Resource.MONEY: 17},
        beer_consumption=1,
        can_be_developed=False
    )

    tiles = [pottery_level_5, pottery_level_4, pottery_level_3, pottery_level_2, pottery_level_1]
    return tiles

def create_all_tiles(player:Player) -> dict:
    all_tiles = {
        Industry.BREWERY: create_brewery_tiles(player),
        Industry.MANUFACTURER: create_manufacturer_tiles(player),
        Industry.POTTERY: create_pottery_tiles(player),
        Industry.COTTON: create_cotton_tiles(player),
        Industry.IRON: create_iron_tiles(player),
        Industry.COAL: create_coal_tiles(player)
    }

    return all_tiles

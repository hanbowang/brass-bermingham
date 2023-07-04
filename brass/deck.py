from __future__ import annotations
import random

from brass.location import LocationName
from brass.common import Industry

class Card:
    def __init__(self, locations:list[LocationName] = None, industries:list[Industry] = None) -> None:
        self.locations = locations
        self.industries = industries

def create_wild_location_card() -> Card:
    return Card(locations=[
        LocationName.STAFFORD,
        LocationName.BURTON_ON_TRENT,
        LocationName.CANNOCK,
        LocationName.TAMWORTH,
        LocationName.WALSALL,
        LocationName.COALBROOKDALE,
        LocationName.DUDLEY,
        LocationName.KIDDERMINSTER,
        LocationName.WOLVERHAMPTON,
        LocationName.WORCHESTER,
        LocationName.BIRMINGHAM,
        LocationName.COVENTRY,
        LocationName.NUNEATON,
        LocationName.REDDITCH,
        LocationName.LEEK,
        LocationName.STOKE_ON_TRENT,
        LocationName.STONE,
        LocationName.UTTOXETER,
        LocationName.BELPER,
        LocationName.DERBY,
    ])

def create_wild_industry_card() -> Card:
    return Card(industries=[
        Industry.COTTON,
        Industry.MANUFACTURER,
        Industry.POTTERY,
        Industry.BREWERY,
        Industry.COAL,
        Industry.IRON,
    ])

def create_wild_location_deck() -> list[Card]:
    return [
        create_wild_location_card(),
        create_wild_location_card(),
        create_wild_location_card(),
        create_wild_location_card()
    ]


def create_wild_industry_deck() -> list[Card]:
    return [
        create_wild_industry_card(),
        create_wild_industry_card(),
        create_wild_industry_card(),
        create_wild_industry_card()
    ]

def create_deck(num_player:int) -> list[LocationName]:
    deck = [
        Card(locations=[LocationName.STAFFORD]),
        Card(locations=[LocationName.STAFFORD]),
        Card(locations=[LocationName.BURTON_ON_TRENT]),
        Card(locations=[LocationName.BURTON_ON_TRENT]),
        Card(locations=[LocationName.CANNOCK]),
        Card(locations=[LocationName.CANNOCK]),
        Card(locations=[LocationName.TAMWORTH]),
        Card(locations=[LocationName.WALSALL]),
        Card(locations=[LocationName.COALBROOKDALE]),
        Card(locations=[LocationName.COALBROOKDALE]),
        Card(locations=[LocationName.COALBROOKDALE]),
        Card(locations=[LocationName.DUDLEY]),
        Card(locations=[LocationName.DUDLEY]),
        Card(locations=[LocationName.KIDDERMINSTER]),
        Card(locations=[LocationName.KIDDERMINSTER]),
        Card(locations=[LocationName.WOLVERHAMPTON]),
        Card(locations=[LocationName.WOLVERHAMPTON]),
        Card(locations=[LocationName.WORCHESTER]),
        Card(locations=[LocationName.WORCHESTER]),
        Card(locations=[LocationName.BIRMINGHAM]),
        Card(locations=[LocationName.BIRMINGHAM]),
        Card(locations=[LocationName.BIRMINGHAM]),
        Card(locations=[LocationName.COVENTRY]),
        Card(locations=[LocationName.COVENTRY]),
        Card(locations=[LocationName.COVENTRY]),
        Card(locations=[LocationName.NUNEATON]),
        Card(locations=[LocationName.REDDITCH]),
        Card(industries=[Industry.IRON]),
        Card(industries=[Industry.IRON]),
        Card(industries=[Industry.IRON]),
        Card(industries=[Industry.IRON]),
        Card(industries=[Industry.COAL]),
        Card(industries=[Industry.COAL]),
        Card(industries=[Industry.POTTERY]),
        Card(industries=[Industry.POTTERY]),
        Card(industries=[Industry.BREWERY]),
        Card(industries=[Industry.BREWERY]),
        Card(industries=[Industry.BREWERY]),
        Card(industries=[Industry.BREWERY]),
        Card(industries=[Industry.BREWERY]),
    ]

    if num_player > 2:
        deck.extend([
            Card(locations=[LocationName.LEEK]),
            Card(locations=[LocationName.LEEK]),
            Card(locations=[LocationName.STOKE_ON_TRENT]),
            Card(locations=[LocationName.STOKE_ON_TRENT]),
            Card(locations=[LocationName.STOKE_ON_TRENT]),
            Card(locations=[LocationName.STONE]),
            Card(locations=[LocationName.STONE]),
            Card(locations=[LocationName.UTTOXETER]),
            Card(industries=[Industry.COTTON, Industry.MANUFACTURER]),
            Card(industries=[Industry.COTTON, Industry.MANUFACTURER]),
            Card(industries=[Industry.COTTON, Industry.MANUFACTURER]),
            Card(industries=[Industry.COTTON, Industry.MANUFACTURER]),
            Card(industries=[Industry.COTTON, Industry.MANUFACTURER]),
            Card(industries=[Industry.COTTON, Industry.MANUFACTURER]),
        ])

    if num_player > 3:
        deck.extend([
            Card(locations=[LocationName.BELPER]),
            Card(locations=[LocationName.BELPER]),
            Card(locations=[LocationName.DERBY]),
            Card(locations=[LocationName.DERBY]),
            Card(locations=[LocationName.DERBY]),
            Card(locations=[LocationName.UTTOXETER]),
            Card(industries=[Industry.COAL]),
            Card(industries=[Industry.COTTON, Industry.MANUFACTURER]),
            Card(industries=[Industry.COTTON, Industry.MANUFACTURER]),
            Card(industries=[Industry.POTTERY]),
        ])

    return deck

def shuffle(deck: list[Card]) -> list[Card]:
    return random.shuffle(deck)

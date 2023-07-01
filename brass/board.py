from enum import Enum

class GameBoard:
    def __init__(self) -> None:
        pass
    

class Space:
    def __init__(self, industries:List[Industry]) -> None:
        self.industries = industries


class Location:
    def __init__(self, color:Color, name:str, spaces:List[Space]) -> None:
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
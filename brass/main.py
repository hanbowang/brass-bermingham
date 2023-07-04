from brass.player import Player
from brass.tile import create_all_tiles

def main():
    players = create_players()
    for player in players:
        player.tiles = create_all_tiles(player)
        

def create_players() -> list[Player]:
    players = []
    for i in range(2):
        name = input(f'Enter name for player {i+1}: ')
        player = Player(name)
        players.append(player)
    return players

if __name__ == '__main__':
    main()

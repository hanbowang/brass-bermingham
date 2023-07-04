from brass.player import Player
from brass.board import GameBoard
from brass.tile import create_all_tiles

def main():
    players = create_players()
    for player in players:
        player.tiles = create_all_tiles(player)
    
    board = GameBoard(len(players))
        

def create_players() -> list[Player]:
    num_players = int(input('Enter number of players: '))
    players = []
    for i in range(num_players):
        name = input(f'Enter name for player {i+1}: ')
        player = Player(name)
        players.append(player)
    return players

if __name__ == '__main__':
    main()

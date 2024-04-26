from src.strategy import minimax_search
from src.ttt import TicTacToe

game = TicTacToe()
game.play_game(minimax_search, minimax_search)
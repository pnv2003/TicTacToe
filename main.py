from src.strategy import alpha_beta_search, minimax_search, random_play
from src.ttt import TicTacToe

game = TicTacToe()
game.play_game(alpha_beta_search, minimax_search)
from src.game import play_game
from src.player import player, random_player
from src.strategy import h_alphabeta_search
from src.ttt import TicTacToe

play_game(TicTacToe(height=9, width=9, k=5), {'X':player(h_alphabeta_search), 'O':random_player})
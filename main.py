from src.player import leveled_player, query_player, random_player
from src.ttt import TicTacToe

game = TicTacToe(h=10, v=10, k=5)

# when the nobrainer challenge every pro players
game.play_game(random_player, leveled_player(level=1))
game.play_game(random_player, leveled_player(level=2))
game.play_game(random_player, leveled_player(level=3))
game.play_game(random_player, leveled_player(level=4))
game.play_game(random_player, leveled_player(level=5))
game.play_game(random_player, leveled_player(level=6))
game.play_game(random_player, leveled_player(level=7))
game.play_game(random_player, leveled_player(level=8))
game.play_game(random_player, leveled_player(level=9))
game.play_game(random_player, leveled_player(level=10))

# can it win against human?
game.play_game(random_player, query_player)

# easy task: winning the lowest leveled player
game.play_game(query_player, leveled_player(level=1))

# hard task: winning the best player ever (kinda)
game.play_game(query_player, leveled_player(level=10))
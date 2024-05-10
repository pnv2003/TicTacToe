import random
from src.strategy import cutoff_depth

def random_player(game, state): 
    return random.choice(list(game.actions(state)))

def player(search_algorithm, level=1):
    """A game player who uses the specified search algorithm"""
    return lambda game, state: search_algorithm(game, state, cutoff_depth(level))[1]
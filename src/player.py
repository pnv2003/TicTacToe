import random
from src.strategy import alpha_beta_cutoff_search

def query_player(game, state):
    """Make a move by querying standard input."""
    print("current state:")
    game.display(state)
    print("available moves: {}".format(game.actions(state)))
    print("")
    move = None
    if game.actions(state):
        move_string = input('Your move? ')
        try:
            move = eval(move_string)
        except NameError:
            move = move_string
    else:
        print('no legal moves: passing turn to next player')
    return move

def random_player(game, state):
    """A player that chooses a legal move at random."""
    return random.choice(game.actions(state)) if game.actions(state) else None

def leveled_player(level = 1):
    
    def alpha_beta_player(game, state):
        return alpha_beta_cutoff_search(game, state, d=level)
    
    return alpha_beta_player
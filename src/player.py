import random
from src.strategy import alpha_beta_cutoff_search

def query_player(game, state):
    """Make a move by querying standard input."""
    states = game.actions(state)
    
    print("current state:")
    game.display(state)
    # print("available moves: {}".format(states))
    print("")
    print("Type '<x>,<y>' to move at row x column y (for example: '1,2')")
    print("Type 'q' to exit")
    # print("For example: '1,2' means row 1 column 2")
    move = None
    if states:
        while True:
            move_string = input('Your move? ')
            try:
                move = eval(move_string)
            except NameError:
                move = move_string
                
            if move == "q":
                exit(0)
            elif type(move) is tuple and move in states:
                break
            else:
                print("Try again.")
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
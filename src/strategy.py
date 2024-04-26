import math
import random
from src.game import Game
from src.state import State

def random_play(game: Game, state: State):
    return random.choice(list(game.actions(state)))

def minimax_search(game: Game, state: State):
    player = game.to_move(state)
    
    def max_value(game: Game, state: State):
        
        if game.terminal_test(state):
            return game.utility(state, player), None
        
        v = -math.inf
        move = None
        for a in game.actions(state):
            
            v2, a2 = min_value(game, game.result(state, a))
            if v2 > v:
                v, move = v2, a
                
        return v, move
    
    def min_value(game: Game, state: State):
        
        if game.terminal_test(state):
            return game.utility(state, player), None
        
        v = math.inf
        move = None
        for a in game.actions(state):
            
            v2, a2 = max_value(game, game.result(state, a))
            if v2 < v:
                v, move = v2, a
                
        return v, move
    
    value, move = max_value(game, state)
    print(f"Value: {value}")
    return move

def alpha_beta_search(game: Game, state: State):
    pass

def monte_carlo_tree_search(game: Game, state: State):
    pass
from functools import lru_cache
import math
import random
from src.game import Game
from src.state import State
cache = lru_cache(10**6)

def random_play(game: Game, state: State):
    return random.choice(list(game.actions(state)))

def minimax_search(game: Game, state: State):
    player = game.to_move(state)
    
    @cache
    def max_value(state: State):
        
        if game.terminal_test(state):
            return game.utility(state, player), None
        
        v = -math.inf
        move = None
        for a in game.actions(state):
            
            v2, a2 = min_value(game.result(state, a))
            if v2 > v:
                v, move = v2, a
                
        return v, move
    
    @cache
    def min_value(state: State):
        
        if game.terminal_test(state):
            return game.utility(state, player), None
        
        v = math.inf
        move = None
        for a in game.actions(state):
            
            v2, a2 = max_value(game.result(state, a))
            if v2 < v:
                v, move = v2, a
                
        return v, move
    
    value, move = max_value(state)
    print(f"Value: {value}")
    return move

def alpha_beta_search(game: Game, state: State):
    player = game.to_move(state)
    
    def max_value(state: State, alpha, beta):
        
        if game.terminal_test(state):
            return game.utility(state, player), None
        
        v = -math.inf
        move = None
        for a in game.actions(state):
            
            v2, a2 = min_value(game.result(state, a), alpha, beta)
            if v2 > v:
                v, move = v2, a
                alpha = max(alpha, v)
            if v >= beta:
                return v, move
            
        return v, move
    
    def min_value(state: State, alpha, beta):
        
        if game.terminal_test(state):
            return game.utility(state, player), None
        
        v = math.inf
        move = None
        for a in game.actions(state):
            
            v2, a2 = max_value(game.result(state, a), alpha, beta)
            if v2 < v:
                v, move = v2, a
                beta = min(beta, v)
            if v <= alpha:
                return v, move
            
        return v, move
    
    value, move = max_value(state, -math.inf, math.inf)
    return move

def monte_carlo_tree_search(game: Game, state: State):
    pass
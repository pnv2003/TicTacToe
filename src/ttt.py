from src.game import Game
from src.state import State

class TicTacToe(Game):
    MAXPL = State.XMARK # default MAX player
    
    def __init__(self, h=3, w=3, k=3) -> None:
        self.h = h
        self.w = w
        self.k = k
        self.initial = State(h, w, k, to_move=State.XMARK)
    
    def actions(self, state: State):
        return state.possible_moves()
    
    def result(self, state: State, move):
        
        player = state.to_move
        res = state.mark(*move)
        
        # compute utility
        if self.k_in_row(res, player, move):
            res.status = player
        
        return res
    
    def utility(self, state: State, player):
        
        # with open("./test.txt", "a") as f:
        #     f.write("At state:")
        #     f.write(str(state))
        #     f.write("Got util:")
        #     f.write(str(
        #         (
        #             1 if player == TicTacToe.MAXPL
        #             else -1
        #         ) if state.game_over
        #         else 0
        #     ))
        #     f.write("\n")
            
        if state.status == State.DRAW:
            return 0
        
        if state.status == player:
            return 1
        
        return -1
        
    def terminal_test(self, state: State):
        return state.status != State.DRAW or len(state.possible_moves()) == 0
        
    def to_move(self, state: State):
        return state.to_move
        
    def k_in_row(self, state: State, player, move):
        
        dir = [
            (0, 1), (1, 1), 
            (1, 0), (1, -1)
        ]
                    
        for dr, dc in dir:
            
            count = 0
            
            r, c = move    
            while state.at(r, c) == player:
                count += 1
                r, c = r + dr, c + dc
            
            r, c = move    
            while state.at(r, c) == player:
                count += 1
                r, c = r - dr, c - dc
                
            count -= 1
            if count >= self.k:
                return True
            
        return False
    
    def play_game(self, *players):
        
        turn = 1
        state = self.initial
        while True:
            for player in players:
                move = player(self, state)
                state = self.result(state, move)
                print(f"Player {turn} move: {move}")
                print(state)
                if self.terminal_test(state):
                    if state.status == State.DRAW:
                        print("Draw!")
                    else:
                        print(f"Player {turn} won!")
                    self.display(state)
                    return self.utility(state, self.to_move(self.initial))
                
                turn = 3 - turn
    
    
    
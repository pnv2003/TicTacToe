from copy import deepcopy


class State:
    # marker
    EMPTY = '.'
    XMARK = 'X' # MAX player
    OMARK = 'O' # MIN player
    
    # status
    DRAW = '-'
    
    def __init__(self, h, w, k, to_move) -> None:
        self.h = h # height
        self.w = w # width
        self.k = k # k in rows to win
        
        if to_move != State.XMARK and to_move != State.OMARK:
            raise Exception("Not XO")
        
        self.to_move = to_move
        self.status = State.DRAW
        self.board = [
            [
                State.EMPTY
                for j in range(self.w)
            ]
            for i in range(self.h)
        ]
        
        self.empty_cells = {
            (row, col)
            for row in range(self.h)
            for col in range(self.w)
        }
    
    def out_of_board(self, row, col):
        if 0 <= row < self.h and 0 <= col < self.w:
            return False
        return True
    
    def at(self, row, col):
        
        if self.out_of_board(row, col):
            return None
        
        return self.board[row][col]
    
    def mark(self, row, col):
            
        if self.at(row, col) != State.EMPTY:
            raise Exception("Marked")
        
        state = deepcopy(self)
        
        # state switch
        state.board[row][col] = self.to_move
        state.to_move = (
            State.XMARK 
            if self.to_move == State.OMARK 
            else State.OMARK
        )
        state.empty_cells.remove((row, col))
    
        return state
        
    def possible_moves(self):
        return list(self.empty_cells)
    
    def __repr__(self) -> str:
        return (
            # f"Board to_move={self.to_move} status={self.status}\n" + 
            '\n'.join([
                ' '.join([
                    self.at(row, col)
                    for col in range(self.w)
                ])
                for row in range(self.h)
            ]) + '\n'
        )
        
    def __eq__(self, other: 'State') -> bool:
        return (
            self.to_move == other.to_move and
            self.status == other.status and
            self.board == other.board
        )
    
    def __hash__(self) -> int:
        return hash((
            self.to_move,
            self.status,
            tuple(
                tuple(
                    self.board[row][col]
                    for col in range(self.w)
                )
                for row in range(self.h)
            ) 
        ))
            
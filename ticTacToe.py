class TicTakToe:
    def __init__(self, side=3, player='x', *args, **kwargs):
        """
        Board's one side length (since its a square board 
        it requires only one side)
        
        Choose first player from {
                                "x": you,
                                "o": AI
                                }
        """
        self.board = list((["."]*side for _ in range(side)))
        self.player = player
        self.side = side
    
    def printBoard(self):
        # prints board
        for i, row in enumerate(self.board):
            print(f'{i}', end='  ')
            print(' '.join(row))
        print('');  print('   ', end='')
        
        for i in range(self.side):  print(i, end=' ')
        print('');  print('')
        
    def isValid(self, px,py):
        # checks for valid move
        return  not (self.side<px or px<0 or \
            self.side<py or py<0 or \
            self.board[px][py]!='.')
    
    def isEnd(self):
        # checks if game has been ended
        
        # for rows
        for row in range(self.side):
            if self.board[row][0]!='.':
                for col in range(1, self.side):
                    if self.board[row][col]!=self.board[row][col-1]:
                        break
                else:
                    return self.board[row][0]
        
        # for columns
        for col in range(self.side):
            if self.board[row][col]!='.':
                for row in range(1, self.side):
                    if self.board[row][col]!=self.board[row-1][col]:
                        break
                else:
                    return self.board[0][col]

            # diagonal left to right
            if self.board[0][0]!='.':
                for i in range(1, self.side):
                    if self.board[i][i]!=self.board[i-1][i-1] or self.board[i][i]=='.':
                        break
                else:
                    return self.board[0][0]
            
        # diagonal right to left
        if self.board[0][-1]!='.':
            for i in range(1, self.side):
                if self.board[i][-i-1]!=self.board[i-1][-i] or self.board[i][-i-1]=='.':
                    break
            else:
                return self.board[0][-1]

        # checks if there is free space to play
        for i in range(self.side):
            for j in range(self.side):
                if self.board[i][j]=='.':
                    return None
        
        # returns for tie
        return '.'
    
    def minLevel(self, alpha, beta):
        # Player
        nodeVal = float('inf')
        py = None
        px = None
        result = self.isEnd()
        
        if result == 'x': return -1, 0, 0       # x won 
        if result == 'o': return 1, 0, 0       # o won
        if result == '.': return 0, 0, 0        # tie

        # doing backtracking here for min max tree
        for i in range(self.side):
            for j in range(self.side):
                if self.board[i][j]=='.':
                    self.board[i][j] = 'x'    # set x to that position (chosen)
                    minVal, tx, ty = self.maxLevel(alpha, beta)
                    
                    if minVal<nodeVal:
                        px, py, nodeVal = i, j, minVal
                    self.board[i][j] = '.' # unchosen

                    if nodeVal<=alpha:
                        return nodeVal, px ,py
                    beta = min(beta, nodeVal)
                        
        return nodeVal, px ,py
    
    def maxLevel(self, alpha, beta):
        # AI
        nodeVal = -float('inf')
        py = None
        px = None
        result = self.isEnd()
        
        if result == 'x':   return -1, 0, 0     # x won 
        if result == 'o':   return 1, 0, 0      # o won
        if result == '.':   return 0, 0, 0      # tie

        # doing backtracking here for min max tree
        for i in range(self.side):
            for j in range(self.side):
                if self.board[i][j]=='.':
                    self.board[i][j] = 'o'    # set o to that position (chosen)
                    maxVal, tx, ty = self.minLevel(alpha, beta)
                    
                    if maxVal>nodeVal:
                        px, py, nodeVal = i, j, maxVal
                        
                    self.board[i][j] = '.' # unchosen

                    if nodeVal>=beta:
                        return nodeVal, px, py
                    alpha = max(nodeVal, alpha)
        return nodeVal, px ,py
                        
    def play(self, RecommendMoves=False):
        import time
        alpha = -float('inf')
        beta = float('inf')
        while True:
            self.printBoard()
            res = self.isEnd()
            if res:
                if res=='o':  print('o won')
                elif res=='x':  print('x won')
                elif res=='.':  print('tie')
                return 'done'
            
            
            while True and self.player=='x':
                if RecommendMoves:
                    nodeVal, qx, qy = self.minLevel(alpha, beta)
                    print('Recommended move: X = {}, Y = {}'.format(qx, qy))

                try:
                    px = int(input('Insert the X coordinate: '))
                    py = int(input('Insert the Y coordinate: '))
                    if self.isValid(px, py):
                        self.board[px][py] = 'x'
                        self.player = 'o'
                        break
                    print('The move is not valid! Try again.')
                    print(' ')
                
                except ValueError:
                    print('Warning: Choose int as input')
                    print(' ')
                    
            else:
                # If it's AI's turn
                start = time.time()
                nodeVal, px, py = self.maxLevel(alpha, beta)
                end = time.time()
                print('Evaluation time: {}s'.format(round(end - start, 7)))
                self.board[px][py] = 'o'
                self.player = 'x'

if __name__ == "__main__":
    game = TicTakToe(3, player='o')
    game.play(RecommendMoves=0)
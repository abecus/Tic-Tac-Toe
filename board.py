class TicTakToe:
    def __init__(self, *args, **kwargs):    
        self.board = [
                    ['.', '.', '.'],
                    ['.', '.', '.'],
                    ['.', '.', '.']
                    ]
        self.player = 'x'
    
    def printBoard(self):
        # prints board
        for row in self.board:
            print(' '.join(row))
        print('')
        
    def isValid(self, px,py):
        # checks for valid move
        if 2<px or px<0 or 2<py or py<0 or self.board[px][py]!='.':    return 0
        return 1
    
    # def isEnd(self, nRow, nCol):
    #     # checks if game has been ended
        
    #     for row in range(nRow):
    #         # for rows
    #         if self.board[row][0]!='.':
    #             if all(self.board[row][col]==self.board[row][col-1]
    #                     and self.board[row][col]!='.'
    #                     for col in range(1, nCol)):
    #                 return self.board[row][0]
    #         break
        
    #     for col in range(nCol):
    #         # for columns
    #         if self.board[0][col]!='.':
    #             if all(self.board[row][col]==self.board[row-1][col] 
    #                     and self.board[row][col]!='.'
    #                     for row in range(1, nRow)):
    #                 return self.board[0][col]
    #         break
        
    #     if self.board[0][0]!='.':
    #         if all(self.board[i][i]==self.board[i-1][i-1]
    #                 and self.board[i][i]!='.'
    #                 for i in range(1, nRow)):
    #             return self.board[0][0]
            
    #     if self.board[0][-1]!='.':
    #         if all(self.board[i][-i-1]==self.board[i-1][-i]
    #                 and self.board[i][-i-1]!='.'
    #                 for i in range(1, nRow)):
    #             return self.board[0][-1]

    #     if any(self.board[i][j]=='.' for j in range(nCol) for i in range(nRow)):
    #         return None
    
    #     return '.'
    
    def isEnd(self, p, q):
        # Vertical win
        for i in range(0, 3):
            if (self.board[0][i] != '.' and
                self.board[0][i] == self.board[1][i] and
                self.board[1][i] == self.board[2][i]):
                return self.board[0][i]

        # Horizontal win
        for i in range(0, 3):
            if (self.board[i] == ['x', 'x', 'x']):
                return 'x'
            elif (self.board[i] == ['o', 'o', 'o']):
                return 'o'

        # Main diagonal win
        if (self.board[0][0] != '.' and
            self.board[0][0] == self.board[1][1] and
            self.board[0][0] == self.board[2][2]):
            return self.board[0][0]

        # Second diagonal win
        if (self.board[0][2] != '.' and
            self.board[0][2] == self.board[1][1] and
            self.board[0][2] == self.board[2][0]):
            return self.board[0][2]

        # Is whole board full?
        for i in range(0, 3):
            for j in range(0, 3):
                # There's an empty field, we continue the game
                if (self.board[i][j] == '.'):
                    return None

        # It's a tie!
        return '.'

    def minLevel(self):
        # Player
        nodeVal = float('inf')
        py = None
        px = None
        result = self.isEnd(3,3)
        
        if result == 'x': return (-1, 0, 0) # x won 
        if result == 'o': return (1, 0, 0) # o won
        if result == '.': return (0, 0, 0) # tie

        # doing backtracking here for min max tree
        for i in range(3):
            for j in range(3):
                if self.board[i][j]=='.':
                    self.board[i][j] = 'x'    # set x to that position (chosen)
                    (minVal, tx, ty) = self.maxLevel()
                    
                    if minVal<nodeVal:
                        px, py, nodeVal = i, j, minVal
                        # nodeVal = minVal
                        # px = i
                        # py = j
                    self.board[i][j] = '.' # unchosen
        
        return (nodeVal, px ,py)
    
    def maxLevel(self):
        # AI
        nodeVal = -float('inf')
        py = None
        px = None
        result = self.isEnd(3,3)
        
        if result == 'x':   return (-1, 0, 0) # x won 
        if result == 'o':   return (1, 0, 0) # o won
        if result == '.':   return (0, 0, 0) # tie

        # doing backtracking here for min max tree
        for i in range(3):
            for j in range(3):
                if self.board[i][j]=='.':
                    self.board[i][j] = 'o'    # set o to that position (chosen)
                    (maxVal, tx, ty) = self.minLevel()
                    
                    if maxVal>nodeVal:
                        px, py, nodeVal = i, j, maxVal
                        
                    self.board[i][j] = '.' # unchosen
        
        return (nodeVal, px ,py)
                        
    def play(self):
        import time
        
        while True:
            self.printBoard()
            res = self.isEnd(3,3)
            if res:
                if res=='o':  print('o won')
                elif res=='x':  print('x won')
                elif res=='.':  print('tie')
                return 'done'
            
            
            while True and self.player=='x':
                # start = time.time()
                # (nodeVal, qx, qy) = self.minLevel()
                # end = time.time()
                # print('Evaluation time: {}s'.format(round(end - start, 7)))
                # print('Recommended move: X = {}, Y = {}'.format(qx, qy))

                px = int(input('Insert the X coordinate: '))
                py = int(input('Insert the Y coordinate: '))

                # (qx, qy) = (px, py)

                if self.isValid(px, py):
                    self.board[px][py] = 'x'
                    self.player = 'o'
                    break
                else:
                    print('The move is not valid! Try again.')
                    print(' ')

            else:
                # If it's AI's turn
                (nodeVal, px, py) = self.maxLevel()
                self.board[px][py] = 'o'
                self.player = 'x'

if __name__ == "__main__":
    game = TicTakToe()
    game.play()
    # print(b.isEnd(3, 3))
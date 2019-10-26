import pygame
from ticTacToe import *
import time


class UI:
    def __init__(self, player): 
        self.player = player
        
        pygame.init()
        
        self.width = 300
        self.height = 350
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        
        pygame.display.set_caption('Mini AI Tic-Tac-Toe 3x3')
        gameIcon = pygame.image.load('ticTacToe.png')
        pygame.display.set_icon(gameIcon)
        
    
    def quitGame(self):
        pygame.quit()
        quit()
    
    @staticmethod
    def text_objects(text, font, c):
        textSurface = font.render(text, True, c)
        return textSurface, textSurface.get_rect()
    
    def renderText(self, size, text, x, y, c=(0,0,0), font='comicsansms'):
        playtext = pygame.font.SysFont(font, size)
        TextSurf, TextRect = self.text_objects(text, playtext, c)
        TextRect.center = (x, y)
        self.screen.blit(TextSurf, TextRect)
        
    def renderOX(self, game):
        for i, row in enumerate(game.board):
            for j, ele in enumerate(row):
                x=j*100 +50
                y=50+ i*100 +50
                if ele=='o':
                    self.renderText(60, ele, x=x, y=y, c=(255, 0, 0))
                elif ele=='x':
                    self.renderText(60, ele, x=x, y=y, c=(0, 255, 0))
                else:
                    self.renderText(60, ele, x=x, y=y)

    def getBox(self):
        mouse = pygame.mouse.get_pos()
        x = mouse[0]//100 *100
        y = max(50, (mouse[1]-50)//100 *100 +50)
        
        # override the boxes by gray box
        pygame.draw.rect(self.screen, (200, 200, 200), (x, y, 100, 100))
        return x, y
    
    def button(self, msg, x, y, w, h, ic, ac, action=None):
        # creates buttons and gives logic to them
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w>mouse[0]>x and y+h>mouse[1]>y:
            pygame.draw.rect(self.screen, ac, (x,y,w,h))
            if click[0]==1 and action!=None:
                time.sleep(0.5)
                action()
        else:
            pygame.draw.rect(self.screen, ic, (x,y,w,h))

        self.renderText(16, msg, (x+w//2), (y+h//2))
    
    def playOnce(self, game, px, py, mark):
        # game playing function
        game.board[px][py] = mark
        game.printBoard()
        print('-'*30)
        res = game._isEnd()
        
        if res:
            self.renderOX(game)
            if res=='o':
                self.renderText(30, "AI Won", x=150, y=25, c=(255, 0, 0))
            elif res=='x':
                self.renderText(30, "You Won", x=150, y=25, c=(0,255,0))
            elif res=='.':
                self.renderText(30, "It's A Draw", x=150, y=25, c=(0,0,255))
            pygame.display.update()
            time.sleep(2)
            
            self.main()     # call for new game
            return 1

    def intro(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.screen.fill((255,255,255))
            self.renderText(30, "TicTacToe XO", (self.width//2), (self.height//2 -100))

            self.button("GO!", 50,250, 50, 25, (0,200,0), (0,255,0), self.main)
            self.button("Quit", 225, 250, 50, 25, (200,0,0), (255,0,0), self.quitGame)

            pygame.display.update()
            self.clock.tick(5)
            
    def main(self):
        alpha=-float('inf')
        beta=float('inf')
        game = TicTakToe(3, player=self.player)
        res = None

        while 1:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    self.quitGame()

            self.screen.fill((255,255,255))

            x, y = self.getBox()
            py = x//100
            px = (y-50) //100

            if pygame.mouse.get_pressed()[0] and game.isValid(px, py):
                # player/you play here
                res = self.playOnce(game, px, py, 'x')
                game.player = 'o'

            elif game.player == 'o':
                # AI plays here
                _, px, py = game.miniMax(palyer=game.player)
                time.sleep(0.2)
                res = self.playOnce(game, px, py, 'o')
                game.player = 'x'

            self.renderOX(game)

            pygame.display.update()
            self.clock.tick(30)
            
if __name__ == "__main__":
    game = UI(player='o')
    game.intro()
    game.main()

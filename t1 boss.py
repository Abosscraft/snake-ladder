import pygame 
import random

pygame.init()

screen = pygame.display.set_mode((1000, 800))
p = pygame.image.load("rook 1.png")
p = pygame.transform.scale(p, (40, 50))

bg = pygame.image.load("Snake and ladders board.jpg")
bg = pygame.transform.scale(bg, (1000, 800))

clock = pygame.time.Clock()

class Player():
    def __init__(self, file, player_X, player_Y):
        self.file = file
        self.player_X = player_X
        self.player_Y = player_Y
    
    def climbling_ladder(self):
        while self.player_X != 410 and self.player_Y != 420:
            if self.player_X != 410 : 
                self.player_X += 6.5  
            if self.player_Y != 420 : 
                self.player_Y -= 10   
            screen.fill( (0, 0, 0) )
            screen.blit(bg, (0, 0))
            screen.blit(player1.file, (player1.player_X, player1.player_Y))
            pygame.display.update()
            pygame.time.delay(30)

        self.player_X,self.player_Y = 410, 420
        print(self.player_X, self.player_Y)
        screen.fill( (0, 0, 0) )
        screen.blit(bg, (0, 0))
        screen.blit(player1.file, (player1.player_X, player1.player_Y))
        pygame.display.update()
        pygame.time.delay(30)

player1 = Player(p, 210, 730) #Player(file, X, Y) This line you can change X and Y for player's starting point

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 :  
                player1.climbling_ladder()

    screen.fill( (0, 0, 0) )
    screen.blit(bg, (0, 0))
    screen.blit(player1.file, (player1.player_X, player1.player_Y))
    pygame.display.update()
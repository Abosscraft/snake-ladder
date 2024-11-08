import pygame 

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
    
    def snake_stage(self):
        # stage 12 to stage 8 x += -4 y = 4
        # (starting stage to stop stage, X, Y) 
        # [ ("12->8", -4, 4), (),..] 
        while self.player_X >= 710 and self.player_Y <= 730:
            if self.player_X != 710 : 
                self.player_X -= 4
            if self.player_Y != 730 : 
                self.player_Y += 4  
            screen.fill( (0, 0, 0) )
            screen.blit(bg, (0, 0))
            screen.blit(player1.file, (player1.player_X, player1.player_Y))
            pygame.display.update()
            pygame.time.delay(30)

        self.player_X,self.player_Y = 710, 730
        print(self.player_X, self.player_Y)
        screen.fill( (0, 0, 0) )
        screen.blit(bg, (0, 0))
        screen.blit(player1.file, (player1.player_X, player1.player_Y))
        pygame.display.update()
        pygame.time.delay(30)

player1 = Player(p, 810, 660) #Player(file, X, Y) This line you can change X and Y for player's starting point

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 :  
                player1.snake_stage()

    if running :
        screen.fill( (0, 0, 0) )
        screen.blit(bg, (0, 0))
        screen.blit(player1.file, (player1.player_X, player1.player_Y))
        pygame.display.update()
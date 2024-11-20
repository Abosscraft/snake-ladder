import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Snake and Ladders")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)
                    
class Map():
    def __init__(self, file) :
        self.players = []
        self.file = file

    def add_player(self, player) :
        self.players.append( player )

    def show_map(self):
        screen.blit(self.file, (0, 0) )

    def player_walk(self, current_player_index, count, number) :
        human_Upturn_R = [ (910,730), (910,580), (910,420), (910,260), (910,100)]
        move_up = { 730 : 660, 660 : 580, 580 : 500, 500 : 420, 420 : 340, 340 : 260, 260 : 180, 180 : 100, 100 : 30 }
        human_Upturn_L = [ (10,660), (10,500), (10,340), (10,180) ]
        bot_Upturn_R = [ (945,730), (945,580), (945,420), (945,260), (945,100)]
        bot_Upturn_L = [ (45,660), (45,500), (45,340), (45,180) ]
        walk_right_to_left = [ 660, 500, 340, 180, 30 ]

        if self.players[current_player_index].walk_backwards :
            self.players[current_player_index].player_x += 100
            if count == number :
                self.players[current_player_index].walk_backwards = False
        elif current_player_index == 0:
            if (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in human_Upturn_R :
                self.players[current_player_index].player_y = move_up[ self.players[current_player_index].player_y ] 
            elif (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in human_Upturn_L :
                self.players[current_player_index].player_y = move_up[ self.players[current_player_index].player_y ]
            elif self.players[current_player_index].player_y in [ y[1] for y in human_Upturn_R ]:
                self.players[current_player_index].player_x += 100
            elif self.players[current_player_index].player_y in walk_right_to_left :
                self.players[current_player_index].player_x -= 100
        elif current_player_index == 1:
            if (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in bot_Upturn_R :
                self.players[current_player_index].player_y = move_up[ self.players[current_player_index].player_y ]
            elif (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in bot_Upturn_L :
                self.players[current_player_index].player_y = move_up[ self.players[current_player_index].player_y ]
            elif self.players[current_player_index].player_y in [ y[1] for y in bot_Upturn_R ]:
                self.players[current_player_index].player_x += 100
            elif self.players[current_player_index].player_y in walk_right_to_left :
                self.players[current_player_index].player_x -= 100
        screen.fill( (192, 192, 192) )
        all_bg[select_map].show_map()
        all_bg[0].players[0].add_image_to_screen()
        all_bg[0].players[1].add_image_to_screen()
        screen.blit( storage_of_file_dice_face[number - 1], (1025, 600) )
        pygame.display.update()
        pygame.time.delay(100)
        
        human_ladder = [ [(210,730),(410,420)], [(710,730),(810,660)], [(610,660),(510,580)],[(10,580),(110,500)],[(910,500),(710,180)],[(110,340),(10,180)],[(210,100),(310,30)],[(910,100),(810,30)]]
        human_d_ladder = { (l[0]) : l[1] for l in human_ladder }
        bot_ladder = [ [ (l[0][0] + 35 , l[0][1] ), (l[1][0] + 35, l[1][1]) ] for l in human_ladder ]
        bot_d_ladder = { (l[0]) : l[1] for l in bot_ladder }
        
        all_stage_snake = [ (910, 660), (610, 340), (310, 340), (210, 180), (810, 100), (510, 30), (210, 30) ]
        snake_11_player1 = { (910, 660) : (830, 680), (830, 680) : (680, 690), (680, 690) : (610, 740), (610, 740) : (510, 730) }
        snake_54_player1 = { (610, 340) : (760, 390), (760, 390) : (700, 450), (700, 450) : (650, 540), (650, 540) : (610, 580) }
        snake_57_player1 = { (310, 340) : (190, 440), (190, 440) : (230, 570), (230, 570) : (170, 630), (170, 630) : (110, 730) }
        snake_78_player1 = { (210, 180) : (470, 180), (470, 180) : (520, 360), (520, 360) : (500, 520), (500, 520) : (510, 660) }
        snake_89_player1 = { (810, 100) : (720, 110), (720, 110) : (630, 90), (630, 90) : (530, 140), (530, 140) : (410, 100) }
        snake_95_player1 = { (510, 30) : (600, 100), (600, 100) : (570, 180), (570, 180) : (610, 260) }
        snake_99_player1 = { (210, 30) : (100, 170), (100, 170) : (60, 250), (60, 250) : (100, 340), (100, 340) : (10, 420) }
        d_snake = { (910, 660) : snake_11_player1, (610, 340) : snake_54_player1, (310, 340) : snake_57_player1\
                  , (210, 180) : snake_78_player1, (810, 100) : snake_89_player1, (510, 30) : snake_95_player1, (210, 30) : snake_99_player1 }
        player1_animation_ladder = {(210, 730) : [15, -21], (710, 730) : [10, -7], (610, 660) : [-10, -8], (10, 580) : [10, -8], (910, 500) : [-10, -16], (110, 340) : [-5, -16], (210, 100) : [10, -7], (910, 100) : [-10, -7]}
        player2_animation_ladder = { (k[0] + 35, k[1]) : [v[0], v[1]] for k,v in player1_animation_ladder.items() }

        all_stage_snake_for_player2 = [ (945, 660), (645, 340), (345, 340), (245, 180), (845, 100), (545, 30), (245, 30) ]
        snake_11_player2 = { (945, 660) : (830, 680), (830, 680) : (680, 690), (680, 690) : (610, 740), (610, 740) : (545, 730) }
        snake_54_player2 = { (645, 340) : (760, 390), (760, 390) : (700, 450), (700, 450) : (650, 540), (650, 540) : (645, 580) }
        snake_57_player2 = { (345, 340) : (190, 440), (190, 440) : (230, 570), (230, 570) : (170, 630), (170, 630) : (145, 730) }
        snake_78_player2 = { (245, 180) : (470, 180), (470, 180) : (520, 360), (520, 360) : (500, 520), (500, 520) : (545, 660) }
        snake_89_player2 = { (845, 100) : (720, 110), (720, 110) : (630, 90), (630, 90) : (530, 140), (530, 140) : (445, 100) }
        snake_95_player2 = { (545, 30) : (600, 100), (600, 100) : (570, 180), (570, 180) : (645, 260) }
        snake_99_player2 = { (245, 30) : (100, 170), (100, 170) : (60, 250), (60, 250) : (100, 340), (100, 340) : (45, 420) }
        d_snake_for_player2 = { (945, 660) : snake_11_player2, (645, 340) : snake_54_player2, (345, 340) : snake_57_player2\
                  , (245, 180) : snake_78_player2, (845, 100) : snake_89_player2, (545, 30) : snake_95_player2, (245, 30) : snake_99_player2 }
        
        if count == number :
            if current_player_index == 0 :
                if (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in [ (l[0][0], l[0][1]) for l in human_ladder ] :
                    ani_x = player1_animation_ladder[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)][0]
                    ani_y = player1_animation_ladder[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)][1]
                    limit_x = human_d_ladder[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)][0]
                    limit_y = human_d_ladder[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)][1]
                    if limit_x > self.players[current_player_index].player_x :
                        while self.players[current_player_index].player_x <= limit_x and self.players[current_player_index].player_y >= limit_y:
                            self.players[current_player_index].player_x += ani_x
                            self.players[current_player_index].player_y += ani_y
                            screen.fill((192, 192, 192))
                            all_bg[select_map].show_map()
                            all_bg[0].players[0].add_image_to_screen()
                            all_bg[0].players[1].add_image_to_screen()
                            screen.blit( storage_of_file_dice_face[number - 1], (1025, 600) )
                            pygame.display.update() 
                            pygame.time.delay(150)
                    else :
                        while self.players[current_player_index].player_x >= limit_x and self.players[current_player_index].player_y >= limit_y:
                            self.players[current_player_index].player_x += ani_x
                            self.players[current_player_index].player_y += ani_y
                            screen.fill((192, 192, 192))
                            all_bg[select_map].show_map()
                            all_bg[0].players[0].add_image_to_screen()
                            all_bg[0].players[1].add_image_to_screen()
                            screen.blit( storage_of_file_dice_face[number - 1], (1025, 600) )
                            pygame.display.update() 
                            pygame.time.delay(150)

                    (self.players[current_player_index].player_x, self.players[current_player_index].player_y) = limit_x, limit_y
                elif (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in all_stage_snake :
                    player_on_stage = d_snake[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)]
                    for count in range(len(player_on_stage.keys())):
                        self.players[current_player_index].player_x, self.players[current_player_index].player_y = player_on_stage[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)]    
                        screen.fill((192, 192, 192))
                        all_bg[select_map].show_map()
                        all_bg[0].players[0].add_image_to_screen()
                        all_bg[0].players[1].add_image_to_screen()
                        screen.blit( storage_of_file_dice_face[number - 1], (1025, 600) )
                        pygame.display.update() 
                        pygame.time.delay(250)
            elif current_player_index == 1 :
                if (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in [ (l[0][0], l[0][1]) for l in bot_ladder ] :
                    ani_x = player2_animation_ladder[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)][0]
                    ani_y = player2_animation_ladder[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)][1]
                    limit_x = bot_d_ladder[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)][0]
                    limit_y = bot_d_ladder[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)][1]
                    if limit_x > self.players[current_player_index].player_x :
                        while self.players[current_player_index].player_x <= limit_x and self.players[current_player_index].player_y >= limit_y:
                            self.players[current_player_index].player_x += ani_x
                            self.players[current_player_index].player_y += ani_y
                            screen.fill((192, 192, 192))
                            all_bg[select_map].show_map()
                            all_bg[0].players[0].add_image_to_screen()
                            all_bg[0].players[1].add_image_to_screen()
                            screen.blit( storage_of_file_dice_face[number - 1], (1025, 600) )
                            pygame.display.update() 
                            pygame.time.delay(150)
                        (self.players[current_player_index].player_x, self.players[current_player_index].player_y) = limit_x, limit_y
                    else :
                        while self.players[current_player_index].player_x >= limit_x and self.players[current_player_index].player_y >= limit_y:
                            self.players[current_player_index].player_x += ani_x
                            self.players[current_player_index].player_y += ani_y
                            screen.fill((192, 192, 192))
                            all_bg[select_map].show_map()
                            all_bg[0].players[0].add_image_to_screen()
                            all_bg[0].players[1].add_image_to_screen()
                            screen.blit( storage_of_file_dice_face[number - 1], (1025, 600) )
                            pygame.display.update() 
                            pygame.time.delay(150)
                        (self.players[current_player_index].player_x, self.players[current_player_index].player_y) = limit_x, limit_y
                elif (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in all_stage_snake_for_player2 :
                    player_on_stage = d_snake_for_player2[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)]
                    for count in range(len(player_on_stage.keys())):
                        self.players[current_player_index].player_x, self.players[current_player_index].player_y = player_on_stage[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)]    
                        screen.fill((192, 192, 192))
                        all_bg[select_map].show_map()
                        all_bg[0].players[0].add_image_to_screen()
                        all_bg[0].players[1].add_image_to_screen()
                        screen.blit( storage_of_file_dice_face[number - 1], (1025, 600) )
                        pygame.display.update() 
                        pygame.time.delay(250)

        # Result 
        if current_player_index == 0 :
            if self.players[current_player_index].player_x == 10 and self.players[current_player_index].player_y == 30 and (number - count) == 0:
                print('check1')
            elif self.players[current_player_index].player_x == 10 and self.players[current_player_index].player_y == 30 and (number - count) != 0:
                self.players[current_player_index].walk_backwards = True
        
        if current_player_index == 1 :
            if self.players[current_player_index].player_x == 45 and self.players[current_player_index].player_y == 30 and (number - count) == 0:
                print('check2')
            elif self.players[current_player_index].player_x == 45 and self.players[current_player_index].player_y == 30 and (number - count) != 0:
                self.players[current_player_index].walk_backwards = True

        screen.fill( (192, 192, 192) )
        all_bg[select_map].show_map()
        all_bg[0].players[0].add_image_to_screen()
        all_bg[0].players[1].add_image_to_screen()
        screen.blit( storage_of_file_dice_face[number - 1], (1025, 600) )
        pygame.display.update()
        pygame.time.delay(100)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    def player_walk_on_map_2(self, current_player_index, count, number) :
        human_Upturn_R = [ (910,730), (910,580), (910,420), (910,260), (910,100)]
        move_up = { 730 : 660, 660 : 580, 580 : 500, 500 : 420, 420 : 340, 340 : 260, 260 : 180, 180 : 100, 100 : 30 }
        human_Upturn_L = [ (10,660), (10,500), (10,340), (10,180) ]
        bot_Upturn_R = [ (945,730), (945,580), (945,420), (945,260), (945,100)]
        bot_Upturn_L = [ (45,660), (45,500), (45,340), (45,180) ]
        walk_right_to_left = [ 660, 500, 340, 180, 30 ]

        if self.players[current_player_index].walk_backwards :
            self.players[current_player_index].player_x += 100
            if count == number :
                self.players[current_player_index].walk_backwards = False
        elif current_player_index == 0:
            if (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in human_Upturn_R :
                self.players[current_player_index].player_y = move_up[ self.players[current_player_index].player_y ] 
            elif (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in human_Upturn_L :
                self.players[current_player_index].player_y = move_up[ self.players[current_player_index].player_y ]
            elif self.players[current_player_index].player_y in [ y[1] for y in human_Upturn_R ]:
                self.players[current_player_index].player_x += 100
            elif self.players[current_player_index].player_y in walk_right_to_left :
                self.players[current_player_index].player_x -= 100
        elif current_player_index == 1:
            if (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in bot_Upturn_R :
                self.players[current_player_index].player_y = move_up[ self.players[current_player_index].player_y ]
            elif (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in bot_Upturn_L :
                self.players[current_player_index].player_y = move_up[ self.players[current_player_index].player_y ]
            elif self.players[current_player_index].player_y in [ y[1] for y in bot_Upturn_R ]:
                self.players[current_player_index].player_x += 100
            elif self.players[current_player_index].player_y in walk_right_to_left :
                self.players[current_player_index].player_x -= 100
        screen.fill( (192, 192, 192) )
        all_bg[select_map].show_map()
        all_bg[0].players[0].add_image_to_screen()
        all_bg[0].players[1].add_image_to_screen()
        screen.blit( storage_of_file_dice_face[number - 1], (1025, 600) )
        pygame.display.update()
        pygame.time.delay(100)
        
        player1_ladder_map2 = [[(110,730),(210,580)],[(510,730),(410,420)],[(10,660),(110,340)],[(310,340),(410,30)],[(810,340),(810,180)],[(910,180),(810,30)]]
        human_d_ladder = { (l[0]) : l[1] for l in player1_ladder_map2 }
        bot_ladder = [ [ (l[0][0] + 35 , l[0][1] ), (l[1][0] + 35, l[1][1]) ] for l in player1_ladder_map2 ]
        bot_d_ladder = { (l[0]) : l[1] for l in bot_ladder }
        
        all_stage_snake = [ (210, 420), (910, 420), (410, 340), (710, 180), (310, 100), (610, 100), (210, 30) ]
        snake_43_player1 = { (210, 420) : (360, 430), (360, 430) : (390, 490), (390, 490) : (320, 550), (320, 550) : (310, 660) }
        snake_50_player1 = { (910, 420) : (780, 540), (780, 540) : (650, 580), (650, 580) : (590, 690), (590, 690) : (410, 730) }
        snake_56_player1 = { (410, 340) : (650, 340), (650, 340) : (680, 510), (680, 510) : (700, 650), (700, 650) : (710, 730) }
        snake_73_player1 = { (710, 180) : (560, 270), (560, 270) : (580, 430), (580, 430) : (530, 510), (530, 510) : (510, 660) }
        snake_84_player1 = { (310, 100) : (500, 150), (500, 150) : (350, 200), (350, 200) : (210, 260) }
        snake_87_player1 = { (610, 100) : (820, 120), (820, 120) : (870, 300), (870, 300) : (810, 420) }
        snake_98_player1 = { (210, 30) : (80, 100), (80, 100) : (130, 260), (130, 260) : (70, 370), (70, 370) : (10, 500) }
        d_snake = { (210, 420) : snake_43_player1, (910, 420) : snake_50_player1, (410, 340) : snake_56_player1\
                  , (710, 180) : snake_73_player1, (310, 100) : snake_84_player1, (610, 100) : snake_87_player1, (210, 30) : snake_98_player1 }
        
        all_stage_snake_for_player2 = [ (x + 35, y) for x,y in all_stage_snake ]
        snake_43_player2 = { (245, 420) : (360, 430), (360, 430) : (390, 490), (390, 490) : (320, 550), (320, 550) : (345, 660) }
        snake_50_player2 = { (945, 420) : (780, 540), (780, 540) : (650, 580), (650, 580) : (590, 690), (590, 690) : (445, 730) }
        snake_56_player2 = { (445, 340) : (650, 340), (650, 340) : (680, 510), (680, 510) : (700, 650), (700, 650) : (745, 730) }
        snake_73_player2 = { (745, 180) : (560, 270), (560, 270) : (580, 430), (580, 430) : (530, 510), (530, 510) : (545, 660) }
        snake_84_player2 = { (345, 100) : (500, 150), (500, 150) : (350, 200), (350, 200) : (245, 260) }
        snake_87_player2 = { (645, 100) : (820, 120), (820, 120) : (870, 300), (870, 300) : (845, 420) }
        snake_98_player2 = { (245, 30) : (80, 100), (80, 100) : (130, 260), (130, 260) : (70, 370), (70, 370) : (45, 500) }
        d_snake_for_player2 = { (245, 420) : snake_43_player2, (945, 420) : snake_50_player2, (445, 340) : snake_56_player2\
                  , (745, 180) : snake_73_player2, (345, 100) : snake_84_player2, (645, 100) : snake_87_player2, (245, 30) : snake_98_player2 }

        
        player1_animation_ladder_map2 = {(110,730) : [10,-15], (510,730) : [-6,-21], (10,660) : [10,-32], (310,340) : [10,-31], (810,340) : [0,-12], (910,180) : [-6,-15] }
        player2_animation_ladder_map2 = { (k[0] + 35, k[1]) : [v[0], v[1]] for k,v in player1_animation_ladder_map2.items() }

        if count == number :
            if current_player_index == 0 :
                if (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in [ (l[0][0], l[0][1]) for l in player1_ladder_map2 ] :
                    ani_x = player1_animation_ladder_map2[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)][0]
                    ani_y = player1_animation_ladder_map2[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)][1]
                    limit_x = human_d_ladder[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)][0]
                    limit_y = human_d_ladder[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)][1]
                    if limit_x > self.players[current_player_index].player_x :
                        while self.players[current_player_index].player_x <= limit_x and self.players[current_player_index].player_y >= limit_y:
                            self.players[current_player_index].player_x += ani_x
                            self.players[current_player_index].player_y += ani_y
                            screen.fill((192, 192, 192))
                            all_bg[select_map].show_map()
                            all_bg[0].players[0].add_image_to_screen()
                            all_bg[0].players[1].add_image_to_screen()
                            screen.blit( storage_of_file_dice_face[number - 1], (1025, 600) )
                            pygame.display.update() 
                            pygame.time.delay(150)
                    else :
                        while self.players[current_player_index].player_x >= limit_x and self.players[current_player_index].player_y >= limit_y:
                            self.players[current_player_index].player_x += ani_x
                            self.players[current_player_index].player_y += ani_y
                            screen.fill((192, 192, 192))
                            all_bg[select_map].show_map()
                            all_bg[0].players[0].add_image_to_screen()
                            all_bg[0].players[1].add_image_to_screen()
                            screen.blit( storage_of_file_dice_face[number - 1], (1025, 600) )
                            pygame.display.update() 
                            pygame.time.delay(150)

                    (self.players[current_player_index].player_x, self.players[current_player_index].player_y) = limit_x, limit_y
                elif (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in all_stage_snake :
                    player_on_stage = d_snake[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)]
                    for count in range(len(player_on_stage.keys())):
                        self.players[current_player_index].player_x, self.players[current_player_index].player_y = player_on_stage[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)]    
                        screen.fill((192, 192, 192))
                        all_bg[select_map].show_map()
                        all_bg[0].players[0].add_image_to_screen()
                        all_bg[0].players[1].add_image_to_screen()
                        screen.blit( storage_of_file_dice_face[number - 1], (1025, 600) )
                        pygame.display.update() 
                        pygame.time.delay(350)

            elif current_player_index == 1 :
                if (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in [ (l[0][0], l[0][1]) for l in bot_ladder ] :
                    ani_x = player2_animation_ladder_map2[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)][0]
                    ani_y = player2_animation_ladder_map2[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)][1]
                    limit_x = bot_d_ladder[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)][0]
                    limit_y = bot_d_ladder[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)][1]
                    if limit_x > self.players[current_player_index].player_x :
                        while self.players[current_player_index].player_x <= limit_x and self.players[current_player_index].player_y >= limit_y:
                            self.players[current_player_index].player_x += ani_x
                            self.players[current_player_index].player_y += ani_y
                            screen.fill((192, 192, 192))
                            all_bg[select_map].show_map()
                            all_bg[0].players[0].add_image_to_screen()
                            all_bg[0].players[1].add_image_to_screen()
                            screen.blit( storage_of_file_dice_face[number - 1], (1025, 600) )
                            pygame.display.update() 
                            pygame.time.delay(150)
                        (self.players[current_player_index].player_x, self.players[current_player_index].player_y) = limit_x, limit_y
                    else :
                        while self.players[current_player_index].player_x >= limit_x and self.players[current_player_index].player_y >= limit_y:
                            self.players[current_player_index].player_x += ani_x
                            self.players[current_player_index].player_y += ani_y
                            screen.fill((192, 192, 192))
                            all_bg[select_map].show_map()
                            all_bg[0].players[0].add_image_to_screen()
                            all_bg[0].players[1].add_image_to_screen()
                            screen.blit( storage_of_file_dice_face[number - 1], (1025, 600) )
                            pygame.display.update() 
                            pygame.time.delay(150)
                        (self.players[current_player_index].player_x, self.players[current_player_index].player_y) = limit_x, limit_y
                elif (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in all_stage_snake_for_player2 :
                    player_on_stage = d_snake_for_player2[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)]
                    for count in range(len(player_on_stage.keys())):
                        self.players[current_player_index].player_x, self.players[current_player_index].player_y = player_on_stage[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)]    
                        screen.fill((192, 192, 192))
                        all_bg[select_map].show_map()
                        all_bg[0].players[0].add_image_to_screen()
                        all_bg[0].players[1].add_image_to_screen()
                        screen.blit( storage_of_file_dice_face[number - 1], (1025, 600) )
                        pygame.display.update() 
                        pygame.time.delay(350)

        # Result 
        if current_player_index == 0 :
            if self.players[current_player_index].player_x == 10 and self.players[current_player_index].player_y == 30 and (number - count) == 0:
                print('check1')
            elif self.players[current_player_index].player_x == 10 and self.players[current_player_index].player_y == 30 and (number - count) != 0:
                self.players[current_player_index].walk_backwards = True
        
        if current_player_index == 1 :
            if self.players[current_player_index].player_x == 45 and self.players[current_player_index].player_y == 30 and (number - count) == 0:
                print('check2')
            elif self.players[current_player_index].player_x == 45 and self.players[current_player_index].player_y == 30 and (number - count) != 0:
                self.players[current_player_index].walk_backwards = True

        screen.fill( (192, 192, 192) )
        all_bg[select_map].show_map()
        all_bg[0].players[0].add_image_to_screen()
        all_bg[0].players[1].add_image_to_screen()
        screen.blit( storage_of_file_dice_face[number - 1], (1025, 600) )
        pygame.display.update()
        pygame.time.delay(100)



class Player():
    def __init__(self, name, player_file, player_x, player_y):
        self.name = name
        self.player_file = player_file
        self.player_x = player_x
        self.player_y = player_y
        self.walk_backwards = False

    def add_image_to_screen(self):
        screen.blit( self.player_file, (self.player_x, self.player_y) )


bg = [ pygame.image.load(f'Snake and ladders board {number}.jpg') for number in range(1,2+1) ]
bg = [ pygame.transform.scale( file_bg, (1000, 800) ) for file_bg in bg ]
all_bg = [ Map(file_bg) for file_bg in bg ]


storage_of_file_player = [ pygame.image.load(f'rook {count}.png') for count in range(1,2+1) ]
storage_of_file_dice_face = [ pygame.image.load(f'Dice Faces {face}.png') for face in range(1,6+1) ] 

storage_of_file_player = [ pygame.transform.scale(image_player ,(40, 50) ) for image_player in storage_of_file_player ]
storage_of_file_dice_face = [ pygame.transform.scale(image_dice, (150, 150) ) for image_dice in storage_of_file_dice_face ]

#730 : 660, 660 : 580, 580 : 500, 500 : 420, 420 : 340, 340 : 260, 260 : 180, 180 : 100, 100 : 30
for index in range(len(storage_of_file_player)) :
    if index == 0 :
        all_bg[0].add_player(Player("Player1", storage_of_file_player[0], 10 , 730)) 
    if index == 1 :
        all_bg[0].add_player(Player("Player2", storage_of_file_player[1], 45, 730)) 

def display_dice(number):
    global storage_of_file_dice_face
    for c in range(5+1):
        screen.fill( (192, 192, 192) )
        all_bg[select_map].show_map()
        all_bg[0].players[0].add_image_to_screen()
        all_bg[0].players[1].add_image_to_screen()
        screen.blit( storage_of_file_dice_face[c], (1025, 600) )
        pygame.display.update()
        pygame.time.delay(100) 
    for c in range(5+1):
        if c != 7 :
            screen.fill( (192, 192, 192) )
            all_bg[select_map].show_map()
            all_bg[0].players[0].add_image_to_screen()
            all_bg[0].players[1].add_image_to_screen()
            screen.blit( storage_of_file_dice_face[c], (1025, 600) )
            pygame.display.update()
            pygame.time.delay(100) 
        else:
            screen.fill( (192, 192, 192) )
            all_bg[select_map].show_map()
            all_bg[0].players[0].add_image_to_screen()
            all_bg[0].players[1].add_image_to_screen()
            screen.blit( storage_of_file_dice_face[number - 1], (1025, 600) )
            pygame.display.update()
            pygame.time.delay(100) 


# information about click to roll the dice
d_X = 1025
d_Y = 600
d_click = pygame.image.load("Dice Faces 1.png")
d_click = pygame.transform.scale(d_click, (150,150))
d_rect = pygame.Rect(d_X, d_Y, d_click.get_width(), d_click.get_height())

# information about choose map 
bg1_X = 100
bg1_Y = 250
bg2_X = 650
bg2_Y = 250
bg_for_select = [ pygame.image.load(f'Snake and ladders board {number}.jpg') for number in range(1,2+1) ] 
bg_for_select = [ pygame.transform.scale(map, (450, 450)) for map in bg_for_select ]
bg1_rect = pygame.Rect(bg1_X, bg1_Y, bg_for_select[0].get_width(), bg_for_select[0].get_height() )
bg2_rect = pygame.Rect(bg2_X, bg2_Y, bg_for_select[1].get_width(), bg_for_select[1].get_height() )

text_font = pygame.font.SysFont('Arial', 100)
text_font_win = pygame.font.SysFont('Arial', 200)
def draw_text(text, font, text_color, X, Y):
    text_image = font.render(text, True, text_color)
    screen.blit(text_image, (X, Y))

def draw_rect():
    pygame.draw.rect(screen, (245, 245, 245), pygame.Rect(300, 300, 620, 200, border_radius=10))


running = True
running1 = True
running2 = False
current_player_index = 0
select_map = -1 
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONUP and select_map == -1:
            if bg1_rect.collidepoint(event.pos):
                select_map = 0
                running1 = False
                running2 = True
            elif bg2_rect.collidepoint(event.pos):
                select_map = 1
                running1 = False
                running2 = True
        elif event.type == pygame.MOUSEBUTTONUP and select_map == 0:
            if d_rect.collidepoint(event.pos):
                number = random.randint(1,6)
                display_dice(number)
                if number >= 1 :
                    all_bg[0].player_walk(current_player_index, 1, number)  
                    pygame.time.delay(100)         
                if number >= 2 :
                    all_bg[0].player_walk(current_player_index, 2, number)    
                    pygame.time.delay(100) 
                if number >= 3 :
                    all_bg[0].player_walk(current_player_index, 3, number)
                    pygame.time.delay(100)       
                if number >= 4 :
                    all_bg[0].player_walk(current_player_index, 4, number)
                    pygame.time.delay(100)     
                if number >= 5 :
                    all_bg[0].player_walk(current_player_index, 5, number)
                    pygame.time.delay(100)     
                if number == 6 :
                    all_bg[0].player_walk(current_player_index, 6, number)
                
                if (all_bg[0].players[current_player_index].player_x, all_bg[0].players[current_player_index].player_y) in [(10, 30), (45, 30)]:
                    running2 = False
                else :
                    current_player_index = (current_player_index + 1) % 2
        elif event.type == pygame.MOUSEBUTTONUP and select_map == 1:
            if d_rect.collidepoint(event.pos):
                number = random.randint(1,6)
                display_dice(number)
                if number >= 1 :
                    all_bg[0].player_walk_on_map_2(current_player_index, 1, number)  
                    pygame.time.delay(100)         
                if number >= 2 :
                    all_bg[0].player_walk_on_map_2(current_player_index, 2, number)    
                    pygame.time.delay(100) 
                if number >= 3 :
                    all_bg[0].player_walk_on_map_2(current_player_index, 3, number)
                    pygame.time.delay(100)       
                if number >= 4 :
                    all_bg[0].player_walk_on_map_2(current_player_index, 4, number)
                    pygame.time.delay(100)     
                if number >= 5 :
                    all_bg[0].player_walk_on_map_2(current_player_index, 5, number)
                    pygame.time.delay(100)     
                if number == 6 :
                    all_bg[0].player_walk_on_map_2(current_player_index, 6, number)

                if (all_bg[0].players[current_player_index].player_x, all_bg[0].players[current_player_index].player_y) in [(10, 30), (45, 30)]:
                    running2 = False
                else :
                    current_player_index = (current_player_index + 1) % 2



    if running1 :
        screen.fill( (192, 192, 192) )
        draw_text('Choose Map', text_font, (0, 0, 0), 370, 60)
        screen.blit(bg_for_select[0], (100, bg1_Y))
        screen.blit(bg_for_select[1], (650, bg2_Y)) 
        pygame.display.update()       
    elif running2 :
        screen.fill( (192, 192, 192) )
        all_bg[select_map].show_map()
        all_bg[0].players[0].add_image_to_screen()
        all_bg[0].players[1].add_image_to_screen()
        screen.blit( d_click, (1025, 600) )
        pygame.display.update()
    else :
        screen.fill( (192, 192, 192) )
        all_bg[select_map].show_map()
        all_bg[0].players[0].add_image_to_screen()
        all_bg[0].players[1].add_image_to_screen()
        draw_rect()
        draw_text(all_bg[0].players[current_player_index].name + " Win" , text_font, (0, 0, 0), 400, 350)
        pygame.display.update()
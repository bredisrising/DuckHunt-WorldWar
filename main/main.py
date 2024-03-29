# [RUN THIS CODE TO PLAY]
# Fyi, if the game runs slowely, its not because it's mining crypto or anything, it was just written by idiots. -Alex M
import globals
import pygame
from game import Game
import os

pygame.init()
pygame.mixer.init()

globals.init_fonts_and_sounds()

monitor_info = pygame.display.Info()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (monitor_info.current_w//2 - globals.SCREEN_WIDTH//2, 0)

clock = pygame.time.Clock()


#initialize pygame

pygame.display.set_caption("Duck Hunt World War")
screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))


game = Game(screen)
game.switch_to_level(_level_index=game.current_level_index)

is_running = not False

delta_time = 0 
# whenever there is movement or important variable change such as a timer
# make sure to multiply by delta_time to make it independent from frame rate
# for example
# instead of timer += 1/30
# 30 being a constant require frame rate
# just do
# timer += delta_time
# this also needs to be done with probabilities
# big annoying change but helps a lot



while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False
            
        
    screen.fill((0, 0, 0))
    
    game.update()
     #print(clock.get_fps())
    pygame.display.update()

    # game already runs at seconds per frame, so I disabled this for now
   
    # Game seems to run at 24 fps when using mouse, so that will be my goal for tracking
    delta_time = clock.tick()/1000
    globals.DELTA_TIME = delta_time

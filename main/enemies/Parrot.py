import globals
from globals import PARROT_PATH, SCREEN_HEIGHT, SCREEN_WIDTH, USE_MOUSE

from abstract.enemy import Enemy
from abstract.enemy import AI
from sprite_sheet import Spritesheet
from sprite_sheet import Animation
from abstract.enemy import HitMarker


import pygame   
import random
import numpy as np

class Parrot(Enemy):
    def __init__(self, game):
        super().__init__()
        self.sprite_sheet = Spritesheet(PARROT_PATH)
        self.animation = Animation(self.sprite_sheet, 0, 0, 150, 150)
        self.depth = 4.7
        self.ai = AI(500, 400, game.player, self.depth)
        self.ai.velocity = 320
        self.world_coordinates = (self.ai.x, self.ai.y) 
        self.phase_2 = False

        self.time_per_hp_regen = 1 # in seconds
        self.current_time = 0
         

        self.rect = pygame.Rect(0, 0, 150, 150)
        self.aim_line_x_offset = 33
    
        self.rect.center = self.world_coordinates

        self.health = 150
        self.max_health = self.health

        self.player_ref = game.player

        
        self.random_std = 0.5
        self.aim_enter_prob = 1/100
        self.shoot_time = 1.5 # in seconds

        if not USE_MOUSE[0]:
            self.aim_enter_prob = 1/100
            self.time_per_hp_regen = 1
            self.current_time = 0
            self.health = 120
            self.max_health = self.health
            self.shoot_time = 1.5

        self.insults = []

    def insult(self):
        insult = random.choice(globals.PARROT_INSULTS)
        pygame.mixer.Sound.play(insult[0])
        self.hit_markers.append(HitMarker(self.hit_markers, len(self.hit_markers), (self.world_coordinates[0]+self.relative_hitmarker_position[0], self.world_coordinates[1]+self.relative_hitmarker_position[1]), insult[1], (75, 75, 200)))


    def render(self, _screen, _camera_offset):
        self.depth_render(_screen, _camera_offset)
        self.render_aim_line(_screen, _camera_offset)
        super().render(_screen, _camera_offset)

    def update(self):
        super().update()

        self.enter_aim()
        self.aim()
        self.ai.update()
        self.world_coordinates = (self.ai.x, self.ai.y)
        if self.current_time >= self.time_per_hp_regen and self.health < self.max_health:
            self.current_time = 0
            self.health += 1
        else:
            self.current_time += globals.DELTA_TIME

        ## Second stage triggers at hp < 30%
        if self.health < 50 and self.phase_2 != True:
            self.phase_2 = True
            
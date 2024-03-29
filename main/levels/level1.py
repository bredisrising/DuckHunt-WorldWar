from abstract.level import Level
from image_object import ImageObj
from enemies.vanila_duck import VanilaDuck
import globals
from globals import SCREEN_WIDTH, SCREEN_HEIGHT, SAVANNA_BUSH_FRONT, SAVANNA_BUSH_BACK, SAVANNA, HIT_BAR_FRAME, HIT_BAR, HIT_EFFECT, AMMO_4, DUCKCROSSHAIR, HITBOX, MUSIC_1
import pygame

class Level1(Level):
    def __init__(self, _name, _screen, _game_instance):
        super().__init__(_name, _screen, _game_instance)

        self.level_size = 1536

        self.background_image = [
            ImageObj(SAVANNA, 5, self.level_size, SCREEN_HEIGHT)
        ]
        
        self.foreground_images = [
            ImageObj(SAVANNA_BUSH_BACK, 4, 2100, 700, y_pos=500),
            ImageObj(SAVANNA_BUSH_FRONT, 3, 2000, 1000, y_pos=300)
        ]

        self.hp_bar = ImageObj(HIT_BAR, 0, 290, 90, x_pos=0, y_pos=20)
        self.hp_bar_frame = ImageObj(HIT_BAR_FRAME, 0, 300, 100, x_pos=-10, y_pos=5)
        self.hit_effect = ImageObj(HIT_EFFECT, 0, 100, 100)
        
        self.hit_box = ImageObj(HITBOX, 0, 400, 300)


        self.ammo_4 = ImageObj(AMMO_4, 0, 100, 300, x_pos=600, y_pos=0)

        self.game_level = True

        self.alive_enemies = [
            VanilaDuck(self.game_instance),
        ]

        self.animation_tick = 4
        self.current_tick = 0
        self.duck_hit = False
    
    def start(self):
        pygame.mixer.music.load(MUSIC_1)
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play(-1)

    def update_bar(self, max_health, current_health):
        return(0 - 295 + ((current_health/max_health)*290))

    def check_enemy_point_collisions(self, _point, _damage):
        for enemy in self.alive_enemies:
            if self.foreground_images[0].check_transparency(self.game_instance.player.x, _point[0], _point[1]):
                if enemy.rect.collidepoint(_point):
                    enemy.on_shot(_damage, _point)
                    self.duck_hit = True
                    self.current_tick = self.animation_tick
                    

                    if enemy.health <= 0:
                        self.alive_enemies.remove(enemy)
                        del enemy
                    break

        if len(self.alive_enemies) == 0 and not self.is_over:
            self.is_over = True
    
    def render(self):
        # render background first
        self.depth_render(self.background_image, self.game_instance.player.x)

        # then enemies
        for enemy in self.alive_enemies:
            enemy.render(self.screen, self.game_instance.player.x)

        # then foreground images like bushes
        self.depth_render(self.foreground_images, self.game_instance.player.x)

        if len(self.alive_enemies) > 0:
            self.screen.blit(self.hp_bar.image, (self.update_bar(self.alive_enemies[0].max_health, self.alive_enemies[0].health), self.hp_bar.y))
            self.screen.blit(self.hp_bar_frame.image, (self.hp_bar_frame.x, self.hp_bar_frame.y))
            self.screen.blit(self.hit_box.image, (self.hit_box.x - 200, self.hit_box.y - 150))

            if self.current_tick > 0 and self.duck_hit:
                self.current_tick -= 1
                self.screen.blit(self.hit_effect.image, self.game_instance.player.gun.crosshair_coords)
            else:
                self.duck_hit = False
            
            # this is really fucking janky, need to change if more than one enemy per level -AM
            if self.alive_enemies[0].firing:
                pygame.draw.circle(self.screen, (255, 0, 0), (self.alive_enemies[0].aim_coordinates[0] - self.game_instance.player.x + SCREEN_WIDTH/2, self.alive_enemies[0].aim_coordinates[1]), 200 - (self.alive_enemies[0].shoot_timer*(200/self.alive_enemies[0].shoot_time)), 4)
           



    def update(self):

        if self.is_over:
            self.current_victory_timer += globals.DELTA_TIME
            if self.current_victory_timer >= self.victory_deley:
                self.stop()
            
        for enemy in self.alive_enemies:
            enemy.update()
    

    def ended(self) -> bool:
        if len(self.alive_enemies) == 0 and self.current_victory_timer >= self.victory_deley:
            return True

    

    

    
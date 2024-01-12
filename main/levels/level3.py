from abstract.level import Level
from image_object import ImageObj
from enemies.eagle import Eagle
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from constants import CITY, CITYCARBACK, CITYCARFRONT, CITYFRONTFENCE, SAVANNA_BUSH_BACK,HIT_BAR_FRAME, HIT_BAR, HIT_EFFECT, AMMO_4, DUCKCROSSHAIR, HITBOX

class Level3(Level):
    def __init__(self, _name, _screen, _game_instance):
        super().__init__(_name, _screen, _game_instance)

        self.level_size = 1536

        self.background_image = [
            ImageObj(CITY, 5, self.level_size, SCREEN_HEIGHT, y_pos = SCREEN_HEIGHT/2 + 100)
        ]
        
        self.back_cars = [
            ImageObj(CITYCARBACK, 5, 1536, 720, y_pos=350),
            ImageObj(CITYCARBACK, 5, 1536, 720, x_pos= SCREEN_WIDTH/2 - 1536 ,y_pos=350)
        ]

        self.front_cars = [
            ImageObj(CITYCARFRONT, 4, 1536, 720, y_pos=550),
            ImageObj(CITYCARFRONT, 4, 1536, 720, x_pos= SCREEN_WIDTH/2 + 1536 ,y_pos=550)
        ]

        self.foreground_images = [
            ImageObj(CITYFRONTFENCE, 3, 2000, 1000, y_pos=300)
        ]

        self.hp_bar = ImageObj(HIT_BAR, 0, 290, 90, x_pos=0, y_pos=20)
        self.hp_bar_frame = ImageObj(HIT_BAR_FRAME, 0, 300, 100, x_pos=-10, y_pos=5)
        self.hit_effect = ImageObj(HIT_EFFECT, 0, 100, 100)
        
        self.hit_box = ImageObj(HITBOX, 0, 400, 300)


        self.ammo_4 = ImageObj(AMMO_4, 0, 100, 300, x_pos=600, y_pos=0)

        self.game_level = True

        self.alive_enemies = [
            Eagle(self.game_instance)
        ]

        self.animation_tick = 4
        self.current_tick = 0
        self.duck_hit = False
    
    def update_bar(self, max_health, current_health):
        return(0 - 295 + ((current_health/max_health)*290))



    # Function to try to get car scrolling working. Lawrd have mercy -AM
    def back_car_scroll(self):
        for self.image in self.back_cars:
            if self.image.x < SCREEN_WIDTH/2 + 1536:
                self.image.x += 5
                self.image.image_rect.center = (self.image.x, self.image.y)
            else:
                self.image.x = SCREEN_WIDTH/2 - 1536
                self.image.image_rect.center = (self.image.x, self.image.y)
    
    def front_car_scroll(self):
        for self.image in self.front_cars:
            if self.image.x > SCREEN_WIDTH/2 - 1536:
                self.image.x -= 5
                self.image.image_rect.center = (self.image.x, self.image.y)
            else:
                self.image.x = SCREEN_WIDTH/2 + 1536
                self.image.image_rect.center = (self.image.x, self.image.y)


    def check_enemy_point_collisions(self, _point, _damage):
        for enemy in self.alive_enemies:
            if enemy.rect.collidepoint(_point):
                enemy.on_shot(_damage)
                self.duck_hit = True
                self.current_tick = self.animation_tick
                

                if enemy.health <= 0:
                    self.alive_enemies.remove(enemy)
                    del enemy
                break

        if len(self.alive_enemies) == 0:
            self.stop()
    

    def start(self):
        pass
    
    def render(self):
        # render background first
        self.depth_render(self.background_image, self.game_instance.player.x)

        # then enemies
        for enemy in self.alive_enemies:
            enemy.render(self.screen, self.game_instance.player.x)
        
        self.back_car_scroll()
        self.front_car_scroll()
        # then foreground images like bushes
        #self.depth_render(self.back_cars, self.game_instance.player.x)
        self.depth_render(self.front_cars, self.game_instance.player.x)

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

    def update(self):
        for enemy in self.alive_enemies:
            enemy.update()
        
        

    
    def stop(self):
        del self

    def ended(self) -> bool:
        if len(self.alive_enemies) == 0:
            return True

    

    

    
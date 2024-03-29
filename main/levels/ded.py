from abstract.level import Level
from globals import SCREEN_HEIGHT, SCREEN_WIDTH, LOBBY_MUSIC_PATH, SPLASH_SCREEN_PATH, FPS, DED, WASTED
import pygame

class Ded(Level):
    def __init__(self, _name, _screen, _game_instance):
        super().__init__(_name, _screen, _game_instance)
        self.bg_image = pygame.image.load(DED).convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        self.frame_counter = 0
        self.game_level = False

    def start(self):
        print(__file__ + " " + self.name + " starting")
        pygame.mixer.music.load(WASTED)
        #pygame.mixer.music.set_volume()
        pygame.mixer.music.play(-1)

    def stop(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

    def ended(self):
        if self.frame_counter >= 5:
            return True
        return False
from abstract.level import Level
from globals import SCREEN_HEIGHT, SCREEN_WIDTH, LOBBY_MUSIC_PATH, LOADING_SCREEN_PATH, FPS, VICTORY2
import pygame

class lev2_victory(Level):
    def __init__(self, _name, _screen, _game_instance):
        super().__init__(_name, _screen, _game_instance)
        self.bg_image = pygame.image.load(VICTORY2).convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.frame_counter = 0
        self.game_level = False

    def start(self):
        print(__file__ + " " + self.name + " starting")
        pygame.mixer.music.load(LOBBY_MUSIC_PATH)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def stop(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        super().stop()

    def ended(self):
        if self.frame_counter >= 5:
            return True
        return False
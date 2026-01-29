import pygame
import config

class Fridge(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((120, 250), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0)) 
        self.rect = self.image.get_rect(topleft=(x, y))

    def interact(self):
        pass

class kitchenBench(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 0, 0)) 
        self.rect = self.image.get_rect(topleft=(x, y)) 
        

import config
import pygame
from pathlib import Path


SRC_DIR = Path(__file__).resolve().parent   #.../prosjekt/src
ROOT_DIR = SRC_DIR.parent                   #.../prosjekt
IMG_DIR = ROOT_DIR / "bilder"               #.../prosjekt/bilder


def load_image(name):
    path = IMG_DIR / name
    if not path.is_file():
        raise FileNotFoundError(f"Image file '{name}' not found in '{IMG_DIR}'")
    return pygame.image.load(path).convert_alpha()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = config.SPEED
        
        self.image = load_image("RED.png")
        self.image = pygame.transform.smoothscale(self.image, (100, 150))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (self.x, self.y)

    # implemeneter bevegelse
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed

    def rules(self):
        if self.x + 70 > 1485:
            self.x = 1415
        if self.x < 485:
            self.x = 485
        if self.y < 400:
            self.y = 400
        if self.y > 830:
            self.y = 830

    def update(self):
        self.move()
        self.rules()
        self.rect.midbottom = (self.x, self.y)
        
    
import config
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = config.SPEED
        
        self.image = pygame.image.load("bilder/RED.png").convert_alpha()
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
        self.rules()
        self.move()
        self.rect.midbottom = (self.x, self.y)
        
    
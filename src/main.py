import config
import pygame
from player import Player
from objects import Fridge
from objects import kitchenBench
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent   #.../prosjekt/src
ROOT_DIR = SRC_DIR.parent                   #.../prosjekt
IMG_DIR = ROOT_DIR / "bilder"               #.../prosjekt/bilder


def load_image(name):
    path = IMG_DIR / name
    if not path.is_file():
        raise FileNotFoundError(f"Image file '{name}' not found in '{IMG_DIR}'")
    return pygame.image.load(path).convert_alpha()

class main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("DD")
        self.text = pygame.font.SysFont("Arial", 24)
         # 1) Definer målområdet
        self.room_rect = pygame.Rect(0,0,1000,700)
        self.room_rect.center = self.screen.get_rect().center

        # 2) Last og skaler bildet (forutsetter at filen finnes)
        self.room_img = load_image("kitchen.png")
        self.room_img = pygame.transform.smoothscale(self.room_img, self.room_rect.size)

        self.livingroom = True
        self.bedroom = False
        self.kitchen = False
        self.toilet = False

        self.clock = pygame.time.Clock()
        self.running = True
        self.sprites = pygame.sprite.Group()
        self.fridge = Fridge(450, 170)
        self.kitchen_bench1 = kitchenBench(1000, 400, 300, 50)
        self.kitchen_bench2 = kitchenBench(1500, 400, 300, 50)
        self.sprites.add(self.kitchen_bench1)
        self.sprites.add(self.kitchen_bench2)
        self.sprites.add(self.fridge)
        self.player = Player(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT -180)
        self.sprites.add(self.player)

    # loop for at spillet skal kjøre
    def hendelser(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
    # kjører funksjonene for å kjøre spillet
    def run(self):
        while self.running:
            self.hendelser()
            self.update()
            self.draw()
            self.clock.tick(config.FPS)

        pygame.quit()

    def update(self):
        self.sprites.update()
        if self.player.rect.bottom <= self.fridge.rect.bottom and self.player.rect.colliderect(self.fridge.rect):
            self.player.rect.bottom = self.fridge.rect.bottom

    # implementer rom oppdatering
    def update_room(self):
        if self.livingroom:
            self.room_img = pygame.image.load("bilder/livingroom.png").convert_alpha()
            self.room_img = pygame.transform.smoothscale(self.room_img, self.room_rect.size)
            self.bedroom = False
            self.kitchen = False
            self.toilet = False
        elif self.bedroom:
            self.room_img = pygame.image.load("bilder/bedroom.png").convert_alpha()
            self.room_img = pygame.transform.smoothscale(self.room_img, self.room_rect.size)
            self.livingroom = False
            self.kitchen = False
            self.toilet = False
        elif self.kitchen:
            self.room_img = pygame.image.load("bilder/kitchen.png").convert_alpha()
            self.room_img = pygame.transform.smoothscale(self.room_img, self.room_rect.size)
            self.livingroom = False
            self.bedroom = False
            self.toilet = False
            self.fridge = Fridge(450, 170)
            self.sprites.add(self.fridge)
        elif self.toilet:
            self.room_img = pygame.image.load("bilder/toilet.png").convert_alpha()
            self.room_img = pygame.transform.smoothscale(self.room_img, self.room_rect.size)
            self.livingroom = False
            self.bedroom = False
            self.kitchen = False

        if self.player.rect.colliderect(self.fridge.rect):
            print("Collided with fridge!")
        

    # tegner skjermen
    def draw(self):
        self.screen.fill(config.PINK)   
        img_rect = self.room_img.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(self.room_img, img_rect)
        self.sprites.draw(self.screen)
        pygame.display.update()


if __name__ == "__main__":
    # Simple runner: create the app and run it when executed directly.
    app = main()
    app.run()
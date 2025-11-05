import pygame
import sys

# Code written while watching Clear Code's "Creating an animated button in Pygame" youtube tutorial

"""
Denne filen implementerer en enkel knapp-klasse i Pygame,
som kan brukes med hover og klikk-effekter.
Knappen har en hevet effekt som endres når musen 
hovrer over den eller når den klikkes.
"""


class Button:
    def __init__(self, text, font, text_color, top_color, bottom_color, hover_color, width, height, pos, elevation):
        self.pressed = False
        self.text = text
        self.font = font
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        # Geometri
        self.top_rect = pygame.Rect(pos, (width, height))
        self.bottom_rect = pygame.Rect(pos, (width, height))
        
        # Tekst
        self.text_surf = self.font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

        # Farger
        self.text_color = pygame.Color(text_color) 
        self.top_color = pygame.Color(top_color)
        self.bottom_color = pygame.Color(bottom_color)
        self.hover_color = pygame.Color(hover_color)
        self.top_color_current = self.top_color



    def draw(self, screen):
        # Elevation logic 
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        #Under knappen
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color_current, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click() #oppdaterer hover/klikk

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color_current = self.hover_color
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                #slipp
                self.dynamic_elevation = self.elevation
                if self.pressed:
                    #print(self.text) 
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color_current = self.top_color



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Gui Menu')
    clock = pygame.time.Clock()

    font_small = pygame.font.Font(None, 30)
    font_big   = pygame.font.Font(None, 36)

    button1 = Button(
        text='Click me',
        font=font_small,
        text_color='#FFE6EE',
        top_color='#FC94AF',
        bottom_color='#F26B8A',
        hover_color='#FFB6C1',
        width=200, height=40, pos=(150, 180),
        elevation=5
        
    )
    button2 = Button(
        text='Click me 2',
        font=font_big,
        text_color=(255,255,255),
        top_color=(80,110,255),
        bottom_color=(60,80,200),
        hover_color=(120,150,255),
        width=220, height=50, pos=(140, 280),
        elevation=6
    )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('#DCDDD8')
        button1.draw(screen)
        button2.draw(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

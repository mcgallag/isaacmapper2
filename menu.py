import pygame
import pygame.freetype


class Menu:
    def __init__(self):
        self.highlighted_color = pygame.Color(128, 0, 0)
        self.unhighlighted_color = pygame.Color(160, 160, 160)
        self.bgcolor = self.unhighlighted_color
        if not pygame.freetype.was_init():
            pygame.freetype.init()
        print(pygame.freetype.get_default_font())
        self.font = pygame.freetype.Font("RobotoMono-Regular.ttf", size=24)
        self.font_color = pygame.Color(0, 0, 0)
        self.highlighted = False

    def update(self):
        pass

    def highlight(self, b=None):
        if b is None:
            self.highlighted = not self.highlighted
            tmp_color = self.bgcolor
            self.bgcolor = self.highlighted_color
            self.highlighted_color = tmp_color
        else:
            if b:
                self.highlighted = True
                self.bgcolor = self.highlighted_color
            else:
                self.highlighted = False
                self.bgcolor = self.unhighlighted_color

    def draw(self, screen):
        # rendered_text = self.font.render("Hello World!", fgcolor=self.font_color)
        screen.fill(self.bgcolor)
        term = "bombs" if self.highlighted else "exits"
        msg = ["Use arrow keys to move highlighter", "Use WASD to add/remove {0}".format(term)]
        i = 0
        for line in msg:
            self.font.render_to(screen, (5, i * self.font.size + 5), line, fgcolor=self.font_color)
            i += 1
        # screen.blit(rendered_text)

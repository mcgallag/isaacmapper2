import pygame
import pygame.freetype


class Menu:
    def __init__(self):
        self.highlighted_color = pygame.Color(128, 0, 0)
        self.unhighlighted_color = pygame.Color(160, 160, 160)
        self.bgcolor = self.unhighlighted_color
        if not pygame.freetype.was_init():
            pygame.freetype.init()
        self.font = pygame.freetype.Font("RobotoMono-Regular.ttf", size=24)
        self.font_color = pygame.Color(0, 0, 0)
        self.highlighted = False
        self.msg = []
        self.msg.append("Use arrow keys to move highlighter")
        self.msg.append("Use WASD to add/remove {0}".format("bombs" if self.highlighted else "exits"))

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
        screen.fill(self.bgcolor)
        i = 0
        for line in self.msg:
            self.font.render_to(screen, (5, i * self.font.size + 5), line, fgcolor=self.font_color)
            i += 1

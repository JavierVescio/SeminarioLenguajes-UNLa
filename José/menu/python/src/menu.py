import pygame
from globals import *
import tool

class Menu:
    logo = None

    def __init__(self, screen, menu, selection = 0):
        self.screen = screen

        if not Menu.logo:
            Menu.logo = tool.load_image("logo")

        self.menu = menu
        self.selection = selection
        self.t = 0
    def run(self):
        done = False

        while not done:
            self.screen.blit(tool.load_image("fondo"), self.screen.get_rect())
            for i in xrange(len(self.menu)):
                self.render(i)
            
            rect = Menu.logo.get_rect()
            rect.centerx = self.screen.get_rect().centerx
            rect.top = 0
            self.screen.blit(Menu.logo, rect)

            image = tool.smallfont.render("asd", True, (0,0,0))
            rect = image.get_rect()
            rect.midbottom = self.screen.get_rect().midbottom
            self.screen.blit(image, rect)

            pygame.display.flip()

            self.t += 1
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.selection = -1
                    done = True
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.move_up()
                    elif event.key == K_DOWN:
                        self.move_down()
                    elif event.key == K_SPACE or event.key == K_RETURN:
                        done = True

        return self.selection
    


    def move_down(self):
        self.selection += 1
        if self.selection >= len(self.menu):
            self.selection = len(self.menu) - 1

    def move_up(self):
        self.selection -= 1
        if self.selection < 0:
            self.selection = 0

    def render(self, id):
        color = (100,0,0)
        if self.selection == id:
            color = (0, 100, 100)
        title = self.menu[id]
        image = tool.font.render(title,1,color)
        rect = image.get_rect()
        rect.centerx = self.screen.get_rect().centerx
        rect.top = Menu.logo.get_height() + id * rect.height * 1.1

        self.screen.blit(image, rect)
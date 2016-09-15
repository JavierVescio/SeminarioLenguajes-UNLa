import pygame
import tool
import sys
from globals import *
from menu import Menu
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_icon(tool.load_image("skyhaw"))
    pygame.display.set_caption("1982")
    tool.load_music("music")
   #aca se controla con un if cuando pongamos opciones de musica on off
    pygame.mixer.music.play(-1)
    main_selection = 0
    while True:
        main_selection = Menu(screen, ("Jugar", "Historia", "Opciones", "Ayuda","Creditos","Salir"), main_selection).run()
        if main_selection == 0:
            submenu =0
            while submenu != 2:
                submenu = Menu(screen, ("Modo Historia", "Modo Batalla?","Atras"), main_selection).run()
        if main_selection == 5:
            pygame.QUIT()
            sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    main()

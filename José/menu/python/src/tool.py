import pygame
import codecs
import os
from globals import *

pygame.font.init()
font = pygame.font.Font("data/font/myfont.ttf", 70)
smallfont = pygame.font.Font("data/font/myfont.ttf", 30)

def load_image(name):
    # devuelve la imagen 
    image = pygame.image.load("data/image/" + name + ".png").convert_alpha()
    return image

def load_sound(name):
    # devuelve el archivo de sonido 
    return pygame.mixer.Sound("data/sound/" + name + ".mp3")

def load_music(name):
    # devuelve el archivo de sonido de fondo
    pygame.mixer.music.load("data/music/" + name + ".mp3")
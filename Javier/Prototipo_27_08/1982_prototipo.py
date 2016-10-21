import pygame #Import the library
import time

pygame.init(); #Initializes pygame

#We define some basic colors.
white = (255,255,255);
black = (0,0,0);
red = (255,0,0);
green = (0,155,0);

display_width = 800;
display_height = 320;

gameDisplay = pygame.display.set_mode((display_width,display_height)); #Sets resolution
pygame.display.set_caption('1982'); #Sets game's name.

block_size = 5;
block_water_movement = 20;
FPS = 25;

clock = pygame.time.Clock();

gameExit = False;

planeImg = pygame.image.load('skyhawkb_perfil.gif')
oceanImg = pygame.image.load('ocean.png')
shipImg = pygame.image.load('coventry.gif')

lead_x = 50;
lead_y = 50;
lead_y_change = 0;
lead_X_change = 0;
water_movement = 0;

def blitImg(img,x,y):
    gameDisplay.blit(img, (x,y));

pos_x_ship = 1600;

while (not gameExit):
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            lead_y_change = 0;
            if (event.key == pygame.K_q):
                gameExit = True;
            elif (event.key == pygame.K_UP):
                lead_y_change = -block_size;
            elif (event.key == pygame.K_DOWN):
                lead_y_change = block_size;
            elif (event.key == pygame.K_LEFT):
                lead_X_change = -block_size;
            elif (event.key == pygame.K_RIGHT):
                lead_X_change = block_size;

    lead_y += lead_y_change;
    lead_x += lead_X_change;

    if (water_movement == -block_water_movement):
        water_movement = 0;
    else:
        water_movement -= block_water_movement;

    pos_x_ship -= block_water_movement;

    gameDisplay.fill(white);
    ##

    blitImg(planeImg,lead_x,lead_y);
    blitImg(oceanImg,water_movement,display_height-27);
    blitImg(shipImg,pos_x_ship,display_height-27-55);

    ##
    pygame.display.update();
    
    clock.tick(FPS);

pygame.quit();
quit();

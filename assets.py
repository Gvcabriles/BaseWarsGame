import pygame
import os
from settings import DISP_WIDTH, DISP_HEIGHT

#Player Sprites
TROOPER = pygame.transform.scale(pygame.image.load(os.path.join("sprites", "trooper_shoot.png")), (50, 40))

#Enemy Sprites
BATTLEDROID = pygame.transform.scale(pygame.image.load(os.path.join("sprites", "enemy1.png")), (50,50))
SUPERDROID = pygame.transform.scale(pygame.image.load(os.path.join("sprites","enemy2.png")), (50,50))
DROIDEKA = pygame.transform.scale(pygame.image.load(os.path.join("sprites","enemy3.png")), (50,50))

#Blaster Trail Sprites 
BLUE_TRAIL = pygame.transform.scale(pygame.image.load(os.path.join("sprites", "blue_las.png")), (50,25))
RED_TRAIL = pygame.transform.scale(pygame.image.load(os.path.join("sprites", "red_las.png")), (50,25))

#Background Image
bg = pygame.transform.scale(pygame.image.load(os.path.join("bg", "bg.jpg")), (DISP_WIDTH, DISP_HEIGHT))
menubg = pygame.transform.scale(pygame.image.load(os.path.join("bg", "menuBG.jpg")), (DISP_WIDTH, DISP_HEIGHT))
import pygame
import os

pygame.mixer.init()

#Background Music
bg_music = pygame.mixer.music.load(os.path.join("sounds", "bgmusic.wav"))
#menu_music = pygame.mixer.music.load(os.path.join("sounds", "menu_music.wav"))

#Shoot Sound Effects
SHOOT_SOUND = pygame.mixer.Sound(os.path.join("sounds","shootsound.wav"))

#Sound Effects 
DEATHs   = pygame.mixer.Sound(os.path.join("sounds", "deathsound.wav"))
HIT_SOUND = pygame.mixer.Sound(os.path.join("sounds", "hitsound.wav"))
DROID_DEATH = pygame.mixer.Sound(os.path.join("sounds", "droiddeath.wav"))
deathaudio = pygame.mixer.Sound(os.path.join("sounds", "defeatsound.wav"))
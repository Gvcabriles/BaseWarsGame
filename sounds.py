import pygame
import os

pygame.mixer.init()

#Background Music
bg_music = pygame.mixer.music.load(os.path.join("sounds", "bgmusic.wav"))
#menu_music = pygame.mixer.music.load(os.path.join("sounds", "menu_music.wav"))

#Shoot Sound Effects
shoot_sound = pygame.mixer.Sound(os.path.join("sounds","shootsound.wav"))

#Sound Effects 
death_sound = pygame.mixer.Sound(os.path.join("sounds", "deathsound.wav"))
hitsound = pygame.mixer.Sound(os.path.join("sounds", "hitsound.wav"))
droid_death = pygame.mixer.Sound(os.path.join("sounds", "droiddeath.wav"))
deathaudio = pygame.mixer.Sound(os.path.join("sounds", "defeatsound.wav"))
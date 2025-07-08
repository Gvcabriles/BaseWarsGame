import pygame
import os

pygame.mixer.init()
pygame.mixer.music.load(os.path.join("sounds", "bgmusic.wav"))

SHOOT_SOUND = pygame.mixer.Sound(os.path.join("sounds", "shootsound.wav"))
DEATH_SOUND = pygame.mixer.Sound(os.path.join("sounds", "deathsound.wav"))
HIT_SOUND = pygame.mixer.Sound(os.path.join("sounds", "hitsound.wav"))
DROID_DEATH = pygame.mixer.Sound(os.path.join("sounds", "droiddeath.wav"))
DEATH_AUDIO = pygame.mixer.Sound(os.path.join("sounds", "defeatsound.wav"))

DROID_DEATH.set_volume(0.3)
DEATH_SOUND.set_volume(0.5)
SHOOT_SOUND.set_volume(0.3)
DEATH_AUDIO.set_volume(0.1)

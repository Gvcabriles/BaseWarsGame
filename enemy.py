from player import Trooper
from assets import BATTLEDROID, SUPERDROID, DROIDEKA, RED_TRAIL
import pygame

class Droid(Trooper):
    ENEMYPOOL = {
        "one": (BATTLEDROID, RED_TRAIL),
        "two": (SUPERDROID, RED_TRAIL),
        "three": (DROIDEKA, RED_TRAIL)
    }

    def __init__(self, x, y, etype, health=1):
        super().__init__(x, y, health)
        self.trooper_img, self.trail_img = self.ENEMYPOOL[etype]
        self.mask = pygame.mask.from_surface(self.trooper_img)

    def move(self, vel):
        self.x -= vel

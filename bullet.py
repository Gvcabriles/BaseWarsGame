import pygame
from utils import collide

class Trail:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.x += vel

    def off_screen(self, width):
        return not(self.y < width and self.x >= 0)

    def collision(self, obj):
        return collide(obj, self)

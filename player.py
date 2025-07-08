from bullet import Trail
from assets import TROOPER, BLUE_TRAIL
from sounds import SHOOT_SOUND, HIT_SOUND, DROID_DEATH
import pygame

class Trooper:
    OVERHEAT = 50
    def __init__(self, x, y, health=1):
        self.x = x
        self.y = y
        self.health = health
        self.trooper_img = None
        self.trail_img = None
        self.trail = []
        self.overheat_counter = 0

    def draw(self, screen):
        screen.blit(self.trooper_img, (self.x, self.y))
        for t in self.trail:
            t.draw(screen)

    def move_trail(self, tvel, obj):
        self.overheat()
        for t in self.trail:
            t.move(tvel)
            if t.off_screen(1200):
                self.trail.remove(t)
            elif t.collision(obj):
                obj.health -= 1
                obj.hp -= 1
                HIT_SOUND.play()
                self.trail.remove(t)

    def get_width(self):
        return self.trooper_img.get_width()

    def get_height(self):
        return self.trooper_img.get_height()

    def overheat(self):
        if self.overheat_counter >= self.OVERHEAT:
            self.overheat_counter = 0
        elif self.overheat_counter > 0:
            self.overheat_counter += 1

    def shoot(self):
        if self.overheat_counter == 0:
            t = Trail(self.x, self.y, self.trail_img)
            self.trail.append(t)
            self.overheat_counter = 1
            SHOOT_SOUND.play()

class Player(Trooper):
    def __init__(self, x, y, health=4):
        super().__init__(x, y, health)
        self.trooper_img = TROOPER
        self.trail_img = BLUE_TRAIL
        self.mask = pygame.mask.from_surface(self.trooper_img)
        self.maxhp = health
        self.target_health = health
        self.hp = health
        self.healthsize = 600
        self.hpbar = self.maxhp / self.healthsize
        self.health_change_speed = 5

    def draw(self, screen):
        super().draw(screen)
        self.HPbar(screen)

    def HPbar(self, screen):
        twidth = 0
        colour = (255, 0, 0)

        if self.hp < self.target_health:
            self.hp += self.health_change_speed
            twidth = int((self.target_health - self.hp) / self.hpbar)
            colour = (0, 255, 0)
        elif self.hp > self.target_health:
            self.hp -= self.health_change_speed
            twidth = int((self.hp - self.target_health) / self.hpbar)

        hp_width = int(self.hp / self.hpbar)
        hp1bar = pygame.Rect(10, 45, hp_width, 25)
        hp2bar = pygame.Rect(hp1bar.right, 45, twidth, 25)

        pygame.draw.rect(screen, (0, 255, 0), hp1bar)
        pygame.draw.rect(screen, colour, hp2bar)
        pygame.draw.rect(screen, (255, 255, 255), (10, 45, self.healthsize, 25), 4)


import pygame
import random
from settings import DISP_WIDTH, DISP_HEIGHT, WHITE, GREEN, YELLOW, LIGHTGRAY, DARKGRAY, RED, FPS
from assets import MENUBG, BG
from sounds import DEATH_AUDIO
from player import Player
from enemy import Droid

screen = pygame.display.set_mode((DISP_WIDTH, DISP_HEIGHT))

def instructions():
    pygame.font.init()
    myfont = pygame.font.Font("8-bit-hud.TTF", 15)
    myfont2 = pygame.font.Font("8-BIT WONDER.TTF", 50)
    running = True
    while running:
        screen.blit(MENUBG, (0, 0))
        header_text = myfont2.render("Instructions", 1, YELLOW)
        body_texts = [
            "* Press the arrow keys to move the Trooper",
            "* Press >Space< to shoot the blaster",
            "* Do not let the Droids into the base!",
            "* The Droids move faster as one dies",
            "* The blaster cooldown will decrease the more Droids you destroy!",
            "Press >Escape< to return to the Main Menu"
        ]

        screen.blit(header_text, (DISP_WIDTH/2 - header_text.get_width()/2, 150))
        for i, text in enumerate(body_texts[:-1]):
            t = myfont.render(text, 1, LIGHTGRAY)
            screen.blit(t, (100, 250 + i * 100))

        exit_text = myfont.render(body_texts[-1], 1, WHITE)
        screen.blit(exit_text, (275, 750))

        pygame.display.update()
        keypress = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if keypress[pygame.K_ESCAPE]:
                return

def mainmenu():
    pygame.init()
    pygame.font.init()
    myfont = pygame.font.Font("8-bit-hud.TTF", 30)
    myfont2 = pygame.font.Font("8-BIT WONDER.TTF", 50)
    myfont3 = pygame.font.Font("8-bit-hud.TTF", 20)
    running = True
    while running:
        screen.blit(MENUBG, (0, 0))
        main_text = myfont2.render("Base Wars", 1, YELLOW)
        body_text = myfont.render("Defend the base from the Droids!", 1, DARKGRAY)
        instructions_text = myfont3.render("Press the >Right Shift< button for Instructions", 1, WHITE)
        start_text = myfont.render("Press Enter to Begin", 1, WHITE)

        screen.blit(main_text, (DISP_WIDTH/2 - main_text.get_width()/2, 250))
        screen.blit(body_text, (DISP_WIDTH/2 - body_text.get_width()/2, 350))
        screen.blit(start_text, (DISP_WIDTH/2 - start_text.get_width()/2, 500))
        screen.blit(instructions_text, (DISP_WIDTH/2 - body_text.get_width()/2, 650))

        pygame.display.update()
        keypress = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if keypress[pygame.K_RETURN]:
                main()
            if keypress[pygame.K_RSHIFT]:
                instructions()
    pygame.quit()

def main():
    pygame.mixer.music.play(-1)
    running = True
    clock = pygame.time.Clock()

    vel = 6
    tvel = 4
    level = 0
    base_health = 3
    player = Player(250, 250)
    enemies = []
    e_vel = 0.5
    enemycount = 3
    losestate = False
    losecounter = 0

    basefont = pygame.font.Font("8-bit-hud.TTF", 15)
    hpfont = pygame.font.Font("8-bit-hud.TTF", 15)
    defeat_font = pygame.font.Font("8-BIT WONDER.TTF", 100)

    def hudtext():
        screen.blit(BG, (0, 0))
        base_lives_text = basefont.render(f"Base Health = {base_health}", 1, WHITE)
        health_text = hpfont.render("HP", 1, GREEN)
        screen.blit(health_text, (DISP_WIDTH - health_text.get_width() - 1145, 20))
        screen.blit(base_lives_text, (DISP_WIDTH - base_lives_text.get_width() - 950, 80))
        for enemy in enemies:
            enemy.draw(screen)
        player.draw(screen)
        if losestate:
            defeat_screen = defeat_font.render("Defeat", 1, RED)
            screen.blit(defeat_screen, (DISP_WIDTH/2 - defeat_screen.get_width()/2, 350))
        pygame.display.update()

    while running:
        clock.tick(FPS)
        hudtext()

        if player.health <= 0 or base_health <= 0:
            pygame.mixer.music.stop()
            DEATH_AUDIO.play()
            losestate = True
            losecounter += 1

        if losestate:
            if losecounter > FPS * 8:
                running = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            e_vel += 0.25
            enemycount += 2
            for _ in range(enemycount):
                etype = random.choice(["one", "one", "one", "one", "two", "two", "three"])
                y_pos = random.randrange(50, DISP_HEIGHT - 100)
                enemy = Droid(random.randrange(1300, 2000), y_pos, etype)
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x + vel > 0:
            player.x -= vel
        if keys[pygame.K_RIGHT] and player.x + vel + player.get_width() < DISP_WIDTH:
            player.x += vel
        if keys[pygame.K_UP] and player.y - vel > 0:
            player.y -= vel
        if keys[pygame.K_DOWN] and player.y + vel + player.get_height() < DISP_HEIGHT:
            player.y += vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(e_vel)
            enemy.move_trail(-tvel, player)
            if random.randrange(0, 10 * 60) == 1:
                enemy.shoot()
            elif enemy.x + enemy.get_width() < 0:
                base_health -= 1
                enemies.remove(enemy)

        player.move_trail(tvel, enemies)

import os
import pygame
import random
import sys
import time
from pygame.locals import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 40
BADDIE_MIN_SIZE = 10
BADDIE_MAX_SIZE = 40
BADDIE_MIN_SPEED = 8
BADDIE_MAX_SPEED = 8
ADD_NEW_BADDIE_RATE = 6
PLAYER_MOVE_RATE = 5


def play():
    count = 3
    level = 1

    def terminate():
        pygame.quit()
        sys.exit()

    def wait_for_player_to_press_key():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:  # escape quits
                        terminate()
                    return

    def player_has_hit_baddie(player_rect, baddies):
        for b in baddies:
            if player_rect.colliderect(b['rect']):
                return True
        return False

    def draw_text(text, font, surface, x, y):
        text_to_obj = font.render(text, 1, TEXT_COLOR)
        text_rect = text_to_obj.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_to_obj, text_rect)

    # set up pygame, the window, and the mouse cursor
    pygame.init()
    mainClock = pygame.time.Clock()
    windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('car race')
    pygame.mouse.set_visible(False)

    # fonts
    font = pygame.font.SysFont(None, 30)

    # sounds
    pygame.mixer.music.load('assets/music/driving.wav')
    gameOverSound = pygame.mixer.Sound('assets/music/car_crash.wav')
    laugh = pygame.mixer.Sound('assets/music/game_over.wav')

    # images
    playerImage = pygame.image.load('assets/image/car1.png')
    car3 = pygame.image.load('assets/image/car3.png')
    car4 = pygame.image.load('assets/image/car4.png')
    playerRect = playerImage.get_rect()
    baddieImage = pygame.image.load('assets/image/car2.png')
    sample = [car3, car4, baddieImage]
    wallLeft = pygame.image.load('assets/image/left.png')
    wallRight = pygame.image.load('assets/image/right.png')

    # "Start" screen
    draw_text('Press any key to start the game.', font, windowSurface, (WINDOW_WIDTH / 3) - 30, (WINDOW_HEIGHT / 3))
    draw_text('And Enjoy', font, windowSurface, (WINDOW_WIDTH / 3), (WINDOW_HEIGHT / 3) + 30)
    pygame.display.update()
    wait_for_player_to_press_key()
    zero = 0
    if not os.path.exists("assets/data/save.dat"):
        f = open("assets/data/save.dat", 'w')
        f.write(str(zero))
        f.close()
    v = open("assets/data/save.dat", 'r')
    topScore = int(v.readline())
    v.close()
    while count > 0:
        # start of the game
        baddies = []
        score = 0
        playerRect.topleft = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50)
        moveLeft = moveRight = moveUp = moveDown = False
        reverseCheat = slowCheat = False
        baddieAddCounter = 0
        pygame.mixer.music.play(-1, 0.0)

        while True:  # the game loop
            score += 1  # increase score

            for event in pygame.event.get():

                if event.type == QUIT:
                    terminate()

                if event.type == KEYDOWN:
                    if event.key == ord('z'):
                        reverseCheat = True
                    if event.key == ord('x'):
                        slowCheat = True
                    if event.key == K_LEFT or event.key == ord('a'):
                        moveRight = False
                        moveLeft = True
                    if event.key == K_RIGHT or event.key == ord('d'):
                        moveLeft = False
                        moveRight = True
                    if event.key == K_UP or event.key == ord('w'):
                        moveDown = False
                        moveUp = True
                    if event.key == K_DOWN or event.key == ord('s'):
                        moveUp = False
                        moveDown = True

                if event.type == KEYUP:
                    if event.key == ord('z'):
                        reverseCheat = False
                        score = 0
                    if event.key == ord('x'):
                        slowCheat = False
                        score = 0
                    if event.key == K_ESCAPE:
                        terminate()

                    if event.key == K_LEFT or event.key == ord('a'):
                        moveLeft = False
                    if event.key == K_RIGHT or event.key == ord('d'):
                        moveRight = False
                    if event.key == K_UP or event.key == ord('w'):
                        moveUp = False
                    if event.key == K_DOWN or event.key == ord('s'):
                        moveDown = False

            # Add new baddies at the top of the screen
            if not reverseCheat and not slowCheat:
                baddieAddCounter += 1
            if baddieAddCounter == ADD_NEW_BADDIE_RATE:
                baddieAddCounter = 0
                baddieSize = 30
                newBaddie = {'rect': pygame.Rect(random.randint(140, 485), 0 - baddieSize, 23, 47),
                             'speed': random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED),
                             'surface': pygame.transform.scale(random.choice(sample), (23, 47)),
                             }
                baddies.append(newBaddie)
                sideLeft = {'rect': pygame.Rect(0, 0, 126, 600),
                            'speed': random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED),
                            'surface': pygame.transform.scale(wallLeft, (126, 599)),
                            }
                baddies.append(sideLeft)
                sideRight = {'rect': pygame.Rect(497, 0, 303, 600),
                             'speed': random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED),
                             'surface': pygame.transform.scale(wallRight, (303, 599)),
                             }
                baddies.append(sideRight)

            # Move the player around.
            if moveLeft and playerRect.left > 0:
                playerRect.move_ip(-1 * PLAYER_MOVE_RATE, 0)
            if moveRight and playerRect.right < WINDOW_WIDTH:
                playerRect.move_ip(PLAYER_MOVE_RATE, 0)
            if moveUp and playerRect.top > 0:
                playerRect.move_ip(0, -1 * PLAYER_MOVE_RATE)
            if moveDown and playerRect.bottom < WINDOW_HEIGHT:
                playerRect.move_ip(0, PLAYER_MOVE_RATE)

            for b in baddies:
                if not reverseCheat and not slowCheat:
                    b['rect'].move_ip(0, b['speed'])
                elif reverseCheat:
                    b['rect'].move_ip(0, -5)
                elif slowCheat:
                    b['rect'].move_ip(0, 1)

            for b in baddies[:]:
                if b['rect'].top > WINDOW_HEIGHT:
                    baddies.remove(b)

            # Draw the game world on the window.
            windowSurface.fill(BACKGROUND_COLOR)

            # Draw the score and top score.
            draw_text(f'Current score: {score}', font, windowSurface, 128, 0)
            draw_text(f'Top score: {topScore}', font, windowSurface, 128, 20)
            draw_text(f'Rest Life: {count}', font, windowSurface, 128, 40)
            draw_text(f'Level: {level}', font, windowSurface, 128, 60)

            windowSurface.blit(playerImage, playerRect)

            for b in baddies:
                windowSurface.blit(b['surface'], b['rect'])

            pygame.display.update()

            # Check if any of the car have hit the player.
            if player_has_hit_baddie(playerRect, baddies):
                if score > topScore:
                    g = open("assets/data/save.dat", 'w')
                    g.write(str(score))
                    g.close()
                    topScore = score
                break

            mainClock.tick(FPS)

        # "Game Over" screen.
        pygame.mixer.music.stop()
        count = count - 1
        gameOverSound.play()
        time.sleep(1)
        if count == 0:
            laugh.play()
            draw_text('Game over', font, windowSurface, (WINDOW_WIDTH / 3), (WINDOW_HEIGHT / 3))
            draw_text('Press any key to play again.', font, windowSurface, (WINDOW_WIDTH / 3) - 80,
                      (WINDOW_HEIGHT / 3) + 30)
            pygame.display.update()
            time.sleep(2)
            wait_for_player_to_press_key()
            count = 3
            gameOverSound.stop()

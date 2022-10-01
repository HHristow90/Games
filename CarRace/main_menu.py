import pygame
import sys
import gaming
from button import Button

pygame.init()
pygame.display.set_caption("Sport Car Racing 3D")
BG = pygame.image.load("assets/image/background.png")


def get_font(size):  # Returns font in the desired size
    return pygame.font.Font("assets/font/font.ttf", size)


def options():
    while True:
        screen = pygame.display.set_mode((800, 680))
        mouse_position = pygame.mouse.get_pos()

        screen.fill("white")

        options_text = get_font(45).render("Options", True, "#b68f40")
        options_rect = options_text.get_rect(center=(400, 50))
        screen.blit(options_text, options_rect)

        #Change speed
        change_speed_text = get_font(20).render(f"Change baddies speed ({gaming.BADDIE_MAX_SPEED}):", True, "#b68f40")
        change_speed_rect = change_speed_text.get_rect(center=(130, 160))
        screen.blit(change_speed_text, change_speed_rect)

        turn_down_volume = Button(image=pygame.image.load("assets/image/Button1.png"), pos=(300, 160),
                                  text_input="<", font=get_font(15), base_color="#d7fcd4", hovering_color="Red")
        turn_up_volume = Button(image=pygame.image.load("assets/image/Button1.png"), pos=(380, 160),
                                text_input=">", font=get_font(15), base_color="#d7fcd4", hovering_color="Green")

        #Change levels
        change_speed_text = get_font(20).render(f"Change current level:", True, "#b68f40")
        change_speed_rect = change_speed_text.get_rect(center=(130, 200))
        screen.blit(change_speed_text, change_speed_rect)

        level1 = Button(image=pygame.image.load("assets/image/Button2.png"), pos=(278, 200),
                                text_input="1", font=get_font(20), base_color="#d7fcd4", hovering_color="Green")
        level2 = Button(image=pygame.image.load("assets/image/Button2.png"), pos=(315, 200),
                                text_input="2", font=get_font(20), base_color="#d7fcd4", hovering_color="Green")
        level3 = Button(image=pygame.image.load("assets/image/Button2.png"), pos=(352, 200),
                                text_input="3", font=get_font(20), base_color="#d7fcd4", hovering_color="Green")
        level4 = Button(image=pygame.image.load("assets/image/Button2.png"), pos=(389, 200),
                                text_input="4", font=get_font(20), base_color="#d7fcd4", hovering_color="Green")
        level5 = Button(image=pygame.image.load("assets/image/Button2.png"), pos=(426, 200),
                                text_input="5", font=get_font(20), base_color="#d7fcd4", hovering_color="Green")

        #highlite buttons
        for button in [turn_up_volume, turn_down_volume, level1, level2, level3, level4, level5]:
            button.change_color(mouse_position)
            button.update(screen)

        #Reset Highscore
        reset_score_text = get_font(20).render(f"Reset top score:", True, "#b68f40")
        reset_score_rect = reset_score_text.get_rect(center=(130, 240))
        screen.blit(reset_score_text, reset_score_rect)

        reset_score = Button(image=pygame.image.load("assets/image/Button1.png"), pos=(300, 240),
                                text_input="Reset", font=get_font(20), base_color="#d7fcd4", hovering_color="Green")
        reset_score.change_color(mouse_position)
        reset_score.update(screen)


        #Back Button
        options_back = Button(image=pygame.image.load("assets/image/Button.png"), pos=(400, 650),
                              text_input="Back", font=get_font(25), base_color="#d7fcd4", hovering_color="Green")

        options_back.change_color(mouse_position)
        options_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_back.check_for_input(mouse_position):
                    main_menu()
                if turn_down_volume.check_for_input(mouse_position):
                    if gaming.BADDIE_MIN_SPEED > 6:
                        gaming.BADDIE_MIN_SPEED -= 1
                        gaming.BADDIE_MAX_SPEED -= 1
                if turn_up_volume.check_for_input(mouse_position):
                    gaming.BADDIE_MIN_SPEED += 1
                    gaming.BADDIE_MAX_SPEED += 1
                if level1.check_for_input(mouse_position):
                    gaming.BADDIE_MIN_SPEED = 8
                    gaming.BADDIE_MAX_SPEED = 8
                if level2.check_for_input(mouse_position):
                    gaming.BADDIE_MIN_SPEED = 10
                    gaming.BADDIE_MAX_SPEED = 10
                if level3.check_for_input(mouse_position):
                    gaming.BADDIE_MIN_SPEED = 12
                    gaming.BADDIE_MAX_SPEED = 12
                if level4.check_for_input(mouse_position):
                    gaming.BADDIE_MIN_SPEED = 15
                    gaming.BADDIE_MAX_SPEED = 15
                if level5.check_for_input(mouse_position):
                    gaming.BADDIE_MIN_SPEED = 20
                    gaming.BADDIE_MAX_SPEED = 20
                if reset_score.check_for_input(mouse_position):
                    data = open("assets/data/save.dat", "w")
                    data.write(str(0))
                    data.close()

        pygame.display.update()


def how_to_play():
    while True:
        screen = pygame.display.set_mode((800, 680))
        mouse_position = pygame.mouse.get_pos()

        screen.fill("white")

        #how to play text
        how_to_play_text = get_font(45).render("How to play", True, "#b68f40")
        how_to_play_rect = how_to_play_text.get_rect(center=(400, 50))
        screen.blit(how_to_play_text, how_to_play_rect)

        #user guide
        user_guide_text = get_font(25).render("Controls:", True, "#b68f40")
        user_guide_rect = user_guide_text.get_rect(center=(55, 150))
        screen.blit(user_guide_text, user_guide_rect)

        controls_text = get_font(25).render("'W' 'A' 'S' 'D' or you can use arrows", True, "#b68f40")
        controls_rect = controls_text.get_rect(center=(300, 150))
        screen.blit(controls_text, controls_rect)

        guide_text = get_font(25).render("Game goal:", True, "#b68f40")
        guide_rect = guide_text.get_rect(center=(65, 200))
        screen.blit(guide_text, guide_rect)

        game_info_text = get_font(25).render("Score as many points as possible", True, "#b68f40")
        game_info_rect = game_info_text.get_rect(center=(330, 200))
        screen.blit(game_info_text, game_info_rect)

        game_info_text1 = get_font(25).render("while avoiding oncoming cars", True, "#b68f40")
        game_info_rect1 = game_info_text1.get_rect(center=(180, 230))
        screen.blit(game_info_text1, game_info_rect1)

        level_info_text = get_font(25).render("Level info:", True, "#b68f40")
        level_info_rect = level_info_text.get_rect(center=(65, 280))
        screen.blit(level_info_text, level_info_rect)

        level_text = get_font(25).render("As the level increases,", True, "#b68f40")
        level_rect = level_text.get_rect(center=(260, 280))
        screen.blit(level_text, level_rect)

        level_text1 = get_font(25).render("so does the speed of the oncoming cars", True, "#b68f40")
        level_rect1 = level_text1.get_rect(center=(230, 310))
        screen.blit(level_text1, level_rect1)

        #Back Button
        back_button = Button(image=pygame.image.load("assets/image/Button.png"), pos=(400, 650),
                              text_input="Back", font=get_font(25), base_color="#d7fcd4", hovering_color="Green")

        back_button.change_color(mouse_position)
        back_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_for_input(mouse_position):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        screen = pygame.display.set_mode((800, 680))
        screen.blit(BG, (0, 0))

        mouse_position = pygame.mouse.get_pos()

        menu_text = get_font(55).render("MAIN MENU", True, "#E14212")
        menu_rect = menu_text.get_rect(center=(400, 50))

        play_button = Button(image=pygame.image.load("assets/image/Button.png"), pos=(400, 150),
                             text_input="PLAY", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        options_button = Button(image=pygame.image.load("assets/image/Button.png"), pos=(400, 200),
                                text_input="OPTIONS", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(image=pygame.image.load("assets/image/Button.png"), pos=(400, 250),
                             text_input="QUIT", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        how_to_play_button = Button(image=pygame.image.load("assets/image/Button2.png"), pos=(760, 20),
                             text_input="?", font=get_font(25), base_color="#d7fcd4", hovering_color="Blue")


        screen.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button, how_to_play_button]:
            button.change_color(mouse_position)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(mouse_position):
                    gaming.play()
                if options_button.check_for_input(mouse_position):
                    options()
                if how_to_play_button.check_for_input(mouse_position):
                    how_to_play()
                if quit_button.check_for_input(mouse_position):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()

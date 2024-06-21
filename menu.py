import pygame
import sys
from opciones import *

def main_menu():
    options = ["Jugar", "Opciones", "Salir"]
    selected_option = 0

    while True:
        screen.fill(BLACK)
        screen.blit(BACKGROUND_IMAGE, [0, 0])
        title_text = FONT.render("Rompe Bloques", True, WHITE)
        footer_text = SMALL_FONT.render("UCSM-TIMS", True, WHITE)

        screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, 100))
        screen.blit(footer_text, (10, SCREEN_HEIGHT - 30))

        for i, option in enumerate(options):
            if i == selected_option:
                option_text = SMALL_FONT.render(option, True, BLUE)
            else:
                option_text = SMALL_FONT.render(option, True, WHITE)
            screen.blit(option_text, (SCREEN_WIDTH//2 - option_text.get_width()//2, 250 + i * 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                    set_sound_volume(menu_move_sound, volume)
                    play_sound(menu_move_sound)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                    set_sound_volume(menu_move_sound, volume)
                    play_sound(menu_move_sound)
                elif event.key == pygame.K_RETURN:
                    print(f"Selected option: {options[selected_option]}")
                    if options[selected_option] == "Jugar":
                        return 'play'
                    elif options[selected_option] == "Opciones":
                        return 'options'
                    elif options[selected_option] == "Salir":
                        pygame.quit()
                        sys.exit()


def options_menu():
    global volume
    selected_option = 0
    options = ["Volumen General", "Volver"]

    while True:
        screen.fill(BLACK)
        screen.blit(BACKGROUND_IMAGE, [0, 0])

        for i, option in enumerate(options):
            if i == selected_option:
                option_text = SMALL_FONT.render(option, True, BLUE)
            else:
                option_text = SMALL_FONT.render(option, True, WHITE)
            screen.blit(option_text, (SCREEN_WIDTH//2 - option_text.get_width()//2, 250 + i * 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                    play_sound(menu_move_sound)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                    play_sound(menu_move_sound)
                elif event.key == pygame.K_RETURN:
                    if options[selected_option] == "Volumen General":
                        adjust_volume('general')
                    elif options[selected_option] == "Volver":
                        return 'back'

def adjust_volume(volume_type):
    global volume
    running = True
    while running:
        screen.fill(BLACK)
        screen.blit(BACKGROUND_IMAGE, [0, 0])

        title_text = FONT.render(f"Ajustar Volumen: {volume_type.capitalize()}", True, WHITE)
        screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, 100))

        volume_text = FONT.render(f"Volumen: {volume*100:.0f}%", True, WHITE)
        screen.blit(volume_text, (SCREEN_WIDTH//2 - volume_text.get_width()//2, 200))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                elif event.key == pygame.K_RIGHT:
                    volume = min(volume + 0.1, 1.0)
                elif event.key == pygame.K_LEFT:
                    volume = max(volume - 0.1, 0.0)

def difficulty_menu():
    options = ["Facil", "Normal", "Dificil"]
    selected_option = 0

    while True:
        screen.fill(BLACK)
        screen.blit(BACKGROUND_IMAGE, [0, 0])
        title_text = FONT.render("Elige tu dificultad", True, WHITE)
        screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, 100))

        for i, option in enumerate(options):
            if i == selected_option:
                option_text = SMALL_FONT.render(option, True, BLUE)
            else:
                option_text = SMALL_FONT.render(option, True, WHITE)
            screen.blit(option_text, (SCREEN_WIDTH//2 - option_text.get_width()//2, 250 + i * 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                    set_sound_volume(menu_move_sound, volume)
                    play_sound(menu_move_sound)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                    set_sound_volume(menu_move_sound, volume)
                    play_sound(menu_move_sound)
                elif event.key == pygame.K_RETURN:
                    difficulties = ["easy", "normal", "hard"]
                    return difficulties[selected_option]

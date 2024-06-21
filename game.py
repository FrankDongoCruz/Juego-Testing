import pygame
import sys
from opciones import *
from levels import load_level
from menu import options_menu

def draw_score(screen, score):
    font = pygame.font.Font(None, 100)
    score_text = font.render(f"{score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def game_loop(difficulty, level):
    paddle = pygame.Rect(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT - 30, 150, 20)
    ball = pygame.Rect(SCREEN_WIDTH // 2 - 15, SCREEN_HEIGHT // 2 - 15, 30, 30)
    ball_dx, ball_dy = BALL_SPEED[difficulty], -BALL_SPEED[difficulty]
    in_play = False
    
    score = 0
    
    bricks = load_level(level)

    pygame.mixer.music.play(-1)

    while True:
        screen.fill(BLACK)
        screen.blit(BACKGROUND_IMAGE, [0, 0])
        screen.blit(PADDLE_IMAGE, paddle.topleft)
        screen.blit(BALL_IMAGE, ball.topleft)

        for brick_rect, brick_texture in bricks:
            screen.blit(brick_texture, brick_rect.topleft)
            
        draw_score(screen, score)

        pygame.draw.rect(screen, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 10)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if pause_menu() == 'quit':
                        return 'game_over'
                elif event.key == pygame.K_SPACE:
                    in_play = True
                elif event.key == pygame.K_w:
                    return 'next_level'

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 10:
            paddle.move_ip(-PADDLE_SPEED, 0)
        if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH - 10:
            paddle.move_ip(PADDLE_SPEED, 0)

        if in_play:
            ball.move_ip(ball_dx, ball_dy)

            if ball.left <= 10 or ball.right >= SCREEN_WIDTH - 10:
                ball_dx = -ball_dx
                set_sound_volume(bounce_sound, volume)
                play_sound(bounce_sound)
            if ball.top <= 10:
                ball_dy = -ball_dy
                set_sound_volume(bounce_sound, volume)
                play_sound(bounce_sound)
            if ball.colliderect(paddle):
                ball_dy = -ball_dy
                set_sound_volume(bounce_sound, volume)
                play_sound(bounce_sound)
            if ball.bottom >= SCREEN_HEIGHT:
                set_sound_volume(bounce_sound, volume)
                play_sound(bounce_sound)                
                return 'game_over'

            brick_collision = ball.collidelistall([brick[0] for brick in bricks])
            if brick_collision:
                ball_dy = -ball_dy
                
                for index in sorted(brick_collision, reverse=True):
                    bricks.pop(index)
                    set_sound_volume(break_sound, volume)
                    play_sound(break_sound)

            if not bricks:
                return 'next_level'

def game_win():
    while True:
        screen.fill(BLACK)
        screen.blit(WIN_SCREEN_IMAGE, (0, 0))

        win_text = FONT.render("Ganaste", True, WHITE)
        continue_text = SMALL_FONT.render("Presiona Enter para continuar", True, WHITE)

        screen.blit(win_text, (SCREEN_WIDTH//2 - win_text.get_width()//2, 200))
        screen.blit(continue_text, (SCREEN_WIDTH//2 - continue_text.get_width()//2, 300))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                elif event.key == pygame.K_ESCAPE:
                    return

def game_over():
    while True:
        screen.fill(BLACK)
        screen.blit(GAME_OVER_IMAGE, (0, 0))

        over_text = FONT.render("GAME OVER", True, WHITE)
        continue_text = SMALL_FONT.render("Presiona Enter para continuar o Esc para salir", True, WHITE)

        screen.blit(over_text, (SCREEN_WIDTH//2 - over_text.get_width()//2, 200))
        screen.blit(continue_text, (SCREEN_WIDTH//2 - continue_text.get_width()//2, 300))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def pause_menu():
    options = ["Reanudar", "Opciones", "Volver al Menú Principal", "Salir"]
    selected_option = 0

    while True:
        screen.fill(BLACK)
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
                    if options[selected_option] == "Reanudar":
                        return
                    elif options[selected_option] == "Opciones":
                        options_menu()
                    elif options[selected_option] == "Volver al Menú Principal":
                        return 'quit'
                    elif options[selected_option] == "Salir":
                        pygame.quit()
                        sys.exit()

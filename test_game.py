import pygame
import pytest
from game import game_loop
from levels import load_level
from opciones import *

@pytest.fixture(scope='module')
def pygame_setup():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    yield screen
    pygame.quit()

def test_adjust_volume():
    from opciones import volume, adjust_volume
    adjust_volume(0.8)
    assert volume == 0.8

def test_game_loop_next_level(pygame_setup):
    result = game_loop('easy', 1)
    assert result == 'next_level'

def test_ball_paddle_collision(pygame_setup):
    paddle = pygame.Rect(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT - 30, 150, 20)
    ball = pygame.Rect(SCREEN_WIDTH // 2 - 15, SCREEN_HEIGHT - 45, 30, 30)
    ball_dy = -5
    ball.y += ball_dy
    if ball.colliderect(paddle):
        ball_dy = -ball_dy
    assert ball_dy == 5

def test_ball_hits_left_edge_of_paddle(pygame_setup):
    paddle = pygame.Rect(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT - 30, 150, 20)
    ball = pygame.Rect(SCREEN_WIDTH // 2 - 90, SCREEN_HEIGHT - 45, 30, 30)
    ball_dy = -5
    ball.y += ball_dy
    if ball.colliderect(paddle):
        ball_dy = -ball_dy
    assert ball_dy == 5

def test_ball_hits_right_edge_of_paddle(pygame_setup):
    paddle = pygame.Rect(SCREEN_WIDTH // 2 + 75 - 75, SCREEN_HEIGHT - 30, 150, 20)
    ball = pygame.Rect(SCREEN_WIDTH // 2 + 60 - 75, SCREEN_HEIGHT - 45, 30, 30)
    ball_dy = -5
    ball.y += ball_dy
    if ball.colliderect(paddle):
        ball_dy = -ball_dy
    assert ball_dy == 5

def test_load_level():
    level_2_bricks = load_level(2)
    assert len(level_2_bricks) == 43

def test_load_level_invalid_level():
    with pytest.raises(ValueError):
        load_level(3)

def test_load_level_level2_brick_positions(pygame_setup):
    level_2_bricks = load_level(2)
    for brick, _ in level_2_bricks:
        assert brick.right <= SCREEN_WIDTH

import pygame
import pytest
from menu import main_menu, options_menu, difficulty_menu
from opciones import *

@pytest.fixture(scope='module')
def pygame_setup():
    pygame.init()
    global screen, FONT, SMALL_FONT, BACKGROUND_IMAGE, BLACK, WHITE, BLUE, GRAY
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Test Menu')
    FONT = pygame.font.Font(None, 74)
    SMALL_FONT = pygame.font.Font(None, 50)
    BACKGROUND_IMAGE = pygame.Surface(screen.get_size())
    BACKGROUND_IMAGE.fill((0, 0, 0))
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GRAY = (128, 128, 128)
    yield
    pygame.quit()

def test_main_menu(pygame_setup):
    result = main_menu()
    assert result is not None

def test_main_menu_play(pygame_setup):
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN))
    pygame.time.delay(500)
    result = main_menu()
    assert result == 'play'

def test_options_menu(pygame_setup):
    result = options_menu()
    assert result == 'back'

def test_options_menu_back(pygame_setup):
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN))
    pygame.time.delay(500)
    result = options_menu()
    assert result == 'back'

def test_difficulty_menu_easy(pygame_setup):
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN))
    pygame.time.delay(500)
    result = difficulty_menu()
    assert result == 'easy'

def test_difficulty_menu_normal(pygame_setup):
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN))
    pygame.time.delay(500)
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN))
    pygame.time.delay(500)
    result = difficulty_menu()
    assert result == 'normal'

def test_difficulty_menu_hard(pygame_setup):
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN))
    pygame.time.delay(500)
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN))
    pygame.time.delay(500)
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN))
    pygame.time.delay(500)
    result = difficulty_menu()
    assert result == 'hard'

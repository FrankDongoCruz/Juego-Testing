import pytest
import pygame
from menu import main_menu, options_menu, difficulty_menu

@pytest.fixture(scope="function", autouse=True)
def setup_pygame():
    pygame.init()
    pygame.display.set_mode((800, 600))
    yield
    pygame.quit()

def test_main_menu(monkeypatch):
    monkeypatch.setattr('pygame.event.get', lambda: [pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RETURN})])
    assert main_menu() == 'play'

def test_options_menu(monkeypatch):
    monkeypatch.setattr('pygame.event.get', lambda: [pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RETURN})])
    options_menu()

def test_difficulty_menu(monkeypatch):
    events = [
        pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_DOWN}),
        pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RETURN})
    ]
    monkeypatch.setattr('pygame.event.get', lambda: events)
    assert difficulty_menu() == 'normal'
